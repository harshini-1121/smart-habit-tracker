from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Dict
from datetime import date, timedelta
from . import models, schemas, crud, auth, database

# Initialize Database tables
models.Base.metadata.create_all(bind=database.engine)

# Detailed Markdown for the API Description
description = """
## Smart Habit Tracker Pro API

This API powers a gamified habit-tracking application designed with "Smart Logic" to ensure users stay consistent.

### Core Features:
* **JWT Authentication**: Secure login and registration.
* **Trick Logic (Auto-Sync)**: The system automatically detects missed days since the last login and backfills them, resetting streaks if necessary.
* **Consistency Analytics**: Full history tracking to power GitHub-style contribution grids.
* **Smart Notifications**: Simulated email triggers for "Almost Missed" and "3-Day Miss" scenarios.

### Simulation Tools:
Use the **Simulation** tags to test time-based logic (like 3-day misses or 10 PM reminders) instantly without waiting for real-world time to pass.
"""

app = FastAPI(
    title="Smart Habit Tracker Pro",
    description=description,
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "API Support",
        "email": "support@habittracker.pro",
    },
    license_info={
        "name": "MIT License",
    },
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- AUTHENTICATION ---

@app.post(
    "/token", 
    response_model=schemas.Token, 
    tags=["Authentication"], 
    summary="Login and obtain access token"
)
def login(form_data: auth.OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    """
    Exchanges user credentials for a **JWT Access Token**.
    
    - **username**: Must be a valid registered email.
    - **password**: The plain-text password.
    
    **Returns**: A JSON object containing the `access_token` and `token_type`.
    """
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post(
    "/users/", 
    response_model=schemas.UserResponse, 
    tags=["Authentication"], 
    summary="Register a new user"
)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    """
    Creates a new user account in the system.
    
    - **email**: Unique email address used for login and reminders.
    - **password**: Password (will be hashed before storage).
    
    **Constraint**: Email must be unique.
    """
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return auth.create_user(db, user)

# --- HABIT MANAGEMENT ---

@app.get(
    "/habits/", 
    response_model=List[schemas.Habit], 
    tags=["Habit Management"], 
    summary="List all habits (Trigger Auto-Sync)"
)
def read_habits(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """
    Retrieves all habits belonging to the authenticated user.
    
    **Smart Logic Trigger**: 
    This endpoint executes the `sync_habits` logic. It checks the gap between today and the 
    `last_processed_date`. If a gap is found:
    1. It backfills the missing days as **'missed'** logs.
    2. It resets the **streak** to 0.
    3. It triggers an **escalation alert** if more than 3 days were missed.
    """
    return crud.sync_habits(db, current_user.id, current_user.email)

@app.post(
    "/habits/", 
    response_model=schemas.Habit, 
    tags=["Habit Management"], 
    summary="Create a new habit"
)
def add_habit(habit: schemas.HabitCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """
    Creates a new habit for the user to track.
    
    - **name**: The name of the habit (e.g., 'Drink Water').
    
    Initially, the habit is created with a streak of 0 and a processed date of yesterday.
    """
    return crud.create_habit(db, habit, current_user.id)

@app.patch(
    "/habits/{id}/log", 
    response_model=schemas.Habit, 
    tags=["Habit Management"], 
    summary="Log today's progress"
)
def log_habit(id: int, log_data: schemas.LogUpdate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """
    Marks a habit as **'done'** or **'missed'** for the current calendar day.
    
    - **status**: Must be either `done` or `missed`.
    
    **Rules**:
    - You can only log a habit **once per day**.
    - Marking as `done` increments the streak.
    - Marking as `missed` resets the streak to 0.
    """
    return crud.log_habit_activity(db, id, log_data.status, current_user.id)

# ---  ANALYTICS ---

@app.get(
    "/habits/{id}/history", 
    response_model=List[schemas.LogResponse], 
    tags=["Analytics"], 
    summary="Get habit log history"
)
def get_habit_history(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """
    Retrieves the entire history of logs for a specific habit.
    
    Used primarily for rendering the **GitHub-style Contribution Chart** in the frontend.
    """
    return crud.get_history(db, id, current_user.id)

# --- SIMULATION & DEBUGGING ---

@app.post(
    "/habits/simulate-reminder", 
    tags=["Simulation & Debugging"], 
    summary="Trigger Global Pending Reminder"
)
def trigger_reminder(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """
    **Simulation**: Simulates the system checking for uncompleted habits.
    
    For every habit not yet marked 'done' today, it prints a motivational reminder 
    email template to the terminal.
    """
    crud.send_pending_reminders(db, current_user.id, current_user.email)
    return {"message": "Pending reminders simulated in console"}

@app.post(
    "/habits/{id}/simulate-almost-missed", 
    tags=["Simulation & Debugging"], 
    summary="Trigger 10 PM 'Almost Missed' Reminder"
)
def trigger_almost_missed(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """
    **Simulation**: Simulates the logic that runs at 10:00 PM nightly.
    
    If the specified habit is not yet marked 'done', it sends an urgent streak-at-risk 
    email template to the console.
    """
    crud.send_almost_missed_reminder(db, id, current_user.email)
    return {"message": "Almost-missed logic triggered in console"}

@app.post(
    "/habits/{id}/simulate-gap", 
    tags=["Simulation & Debugging"], 
    summary="Inject 3-Day Absence"
)
def trigger_gap(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """
    **Simulation**: Manually modifies the database to set a habit's last processed date to 4 days ago.
    
    **How to test**:
    1. Call this endpoint.
    2. Immediately call **GET /habits/**.
    3. Observe the terminal to see the **Escalation Alert** and watch the UI reset the streak.
    """
    habit = db.query(models.Habit).filter(models.Habit.id == id, models.Habit.user_id == current_user.id).first()
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    habit.last_processed_date = date.today() - timedelta(days=4)
    db.commit()
    return {"message": "Gap simulated. Refresh the habit list to trigger sync logic."}

@app.post(
    "/habits/{id}/debug-reset", 
    tags=["Simulation & Debugging"], 
    summary="Clear Today's Log (Fresh Start)"
)
def debug_reset(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """
    **Debug**: Deletes the activity log entry for the current day.
    
    Use this if you want to re-test clicking the 'Done' or 'Missed' buttons on the 
    UI without waiting for tomorrow.
    """
    crud.debug_reset_today(db, id)
    return {"message": "Today's logs cleared."}