import React from 'react';

const HabitItem = ({ habit, onLog }) => {
    return (
        <div className="habit-item">
            <div className="habit-info">
                <h3>{habit.name}</h3>
                <p>Streak: <span>{habit.streak} days</span> 🔥</p>
            </div>
            <div className="habit-actions">
                <button className="btn-done" onClick={() => onLog(habit.id, 'done')}>Mark Done</button>
                <button className="btn-miss" onClick={() => onLog(habit.id, 'missed')}>Missed</button>
            </div>
        </div>
    );
};

export default HabitItem;