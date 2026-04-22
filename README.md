# 🛡️ Smart Habit Tracker Pro

An authentic, adaptive habit-tracking ecosystem built with **FastAPI** and **React**. This project features "Smart Catch-up Logic" that ensures data integrity even if the user goes offline for days.

## 🌟 Key Features
* **JWT Authentication**: Secure user sessions.
* **Trick Logic (Auto-Sync)**: Automatically backfills missed days and resets streaks upon user return.
* **Smart Reminders**: 
    * **10:00 PM Nudge**: Alerts users if a habit is almost missed.
    * **3-Day Escalation**: Specialized alerts for users who fall off track.
* **Consistency Analytics**: GitHub-style contribution grid for visual progress tracking.
* **Auto-Generated SDK**: Built-in Python SDK generated via OpenAPI.

## 🛠️ Installation & Running

### Prerequisites
* **Python 3.14+**
* **Node.js (LTS)**

### Setup
1. Run `setupdev.bat`. This will create the virtual environment and install all dependencies.
2. Ensure you have a `.env` file in the `backend/` folder if using SMTP for real emails.

### Execution
Run `runapplication.bat`. This will launch the backend and frontend simultaneously.

## 📖 API Documentation
Once the application is running, visit:
* **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **Redoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🧪 Simulation Suite
To demonstrate the business logic without waiting for real-world time:
1. **Almost Missed**: Click the ⏳ button to simulate the end-of-day check.
2. **3-Day Miss**: Click the 💀 button to inject a gap into the database. Refresh the habit list to see the auto-sync in action.
3. **Reset**: Use the 🔄 button to clear today's log for re-testing.