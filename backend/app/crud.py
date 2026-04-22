import random
from datetime import date, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
import datetime
MOTIVATIONAL_QUOTES = [
    "It does not matter how slowly you go as long as you do not stop.",
    "The secret of getting ahead is getting started.",
    "Your habits will determine your future.",
    "Don't stop when you're tired. Stop when you're done."
]

def send_simulated_email(user_email: str, subject: str, message: str):
    """Simulates an email dispatch in the terminal console."""
    print("\n" + "🚀 " + "="*20 + " SIMULATED EMAIL " + "="*20, flush=True)
    print(f"TO      : {user_email}", flush=True)
    print(f"SUBJECT : {subject}", flush=True)
    print(f"BODY    : {message}", flush=True)
    print("="*57 + "\n", flush=True)

def sync_habits(db: Session, user_id: int, user_email: str):
    """Backfills missed days and checks for 3-day escalation."""
    habits = db.query(models.Habit).filter(models.Habit.user_id == user_id).all()
    today = date.today()
    
    for habit in habits:
        last = habit.last_processed_date
        gap_days = (today - last).days
        
        if gap_days > 1:
            missed_count = 0
            for i in range(1, gap_days):
                miss_date = last + timedelta(days=i)
                existing = db.query(models.HabitLog).filter(
                    models.HabitLog.habit_id == habit.id, 
                    models.HabitLog.date == miss_date
                ).first()
                if not existing:
                    db.add(models.HabitLog(habit_id=habit.id, date=miss_date, status="missed"))
                    missed_count += 1
            
            habit.streak = 0
            habit.last_processed_date = today - timedelta(days=1)
            db.commit()
            
            if missed_count >= 3:
                send_simulated_email(
                    user_email,
                    "Escalation Alert: 3+ Days Missed",
                    f"Warning: You've missed '{habit.name}' for {missed_count} days. Let's start again!"
                )
    return habits

def create_habit(db: Session, habit: schemas.HabitCreate, user_id: int):
    db_habit = models.Habit(**habit.dict(), user_id=user_id, last_processed_date=date.today() - timedelta(days=1))
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit

def log_habit_activity(db: Session, habit_id: int, status: str, user_id: int):
    habit = db.query(models.Habit).filter(models.Habit.id == habit_id, models.Habit.user_id == user_id).first()
    if not habit: raise HTTPException(status_code=404, detail="Habit not found")
    
    today = date.today()
    existing = db.query(models.HabitLog).filter(models.HabitLog.habit_id == habit_id, models.HabitLog.date == today).first()
    if existing: raise HTTPException(status_code=400, detail="Already logged for today")

    new_log = models.HabitLog(habit_id=habit_id, date=today, status=status)
    db.add(new_log)
    habit.streak = habit.streak + 1 if status == "done" else 0
    habit.last_processed_date = today
    db.commit()
    db.refresh(habit)
    return habit

def get_history(db: Session, habit_id: int, user_id: int):
    habit = db.query(models.Habit).filter(models.Habit.id == habit_id, models.Habit.user_id == user_id).first()
    if not habit: raise HTTPException(status_code=404, detail="Habit not found")
    return db.query(models.HabitLog).filter(models.HabitLog.habit_id == habit_id).all()

def send_pending_reminders(db: Session, user_id: int, user_email: str):
    today = date.today()
    habits = db.query(models.Habit).filter(models.Habit.user_id == user_id).all()
    for habit in habits:
        logged_today = db.query(models.HabitLog).filter(models.HabitLog.habit_id == habit.id, models.HabitLog.date == today).first()
        if not logged_today:
            quote = random.choice(MOTIVATIONAL_QUOTES)
            send_simulated_email(user_email, "Pending Habit Reminder", f"Streak at risk for '{habit.name}'! {quote}")

def send_almost_missed_reminder(db: Session, habit_id: int, user_email: str):
    """Simulates 10PM check: sends email only if NOT marked 'done' today."""
    today = date.today()
    habit = db.query(models.Habit).filter(models.Habit.id == habit_id).first()
    logged_today = db.query(models.HabitLog).filter(
        models.HabitLog.habit_id == habit_id, 
        models.HabitLog.date == today, 
        models.HabitLog.status == 'done'
    ).first()

    if not logged_today:
        quote = random.choice(MOTIVATIONAL_QUOTES)
        send_simulated_email(
            user_email, 
            "⚠️ Urgent: Streak at Risk!", 
            f"It's almost 11:59 PM! You haven't done '{habit.name}'. {quote}"
        )

def debug_reset_today(db: Session, habit_id: int):
    """
    Developer Tool: Deletes today's log and rolls back the streak 
    math so you can re-test the buttons without 'cheating' the streak.
    """
    today = datetime.date.today()
    habit = db.query(models.Habit).filter(models.Habit.id == habit_id).first()
    
    if not habit:
        return

    # 1. Find today's log before we delete it
    existing_log = db.query(models.HabitLog).filter(
        models.HabitLog.habit_id == habit_id, 
        models.HabitLog.date == today
    ).first()

    if existing_log:
        # 2. If we are resetting a 'done' day, we must 'undo' the streak increment
        if existing_log.status == "done":
            habit.streak = max(0, habit.streak - 1)
        
        # 3. Delete the log
        db.delete(existing_log)
    
    # 4. Set processed date to yesterday so the UI/API allows a new entry for today
    habit.last_processed_date = today - datetime.timedelta(days=1)
    db.commit()