@echo off
echo ====================================================
echo 🚀 STARTING SMART HABIT TRACKER...
echo ====================================================

:: Start Backend in a new window
echo Starting FastAPI Backend on http://localhost:8000...
start "BACKEND - FastAPI" cmd /k "venv\Scripts\activate && cd backend && uvicorn app.main:app --reload"

:: Start Frontend in a new window
echo Starting React Frontend on http://localhost:3000...
start "FRONTEND - React" cmd /k "cd frontend && npm start"

echo ====================================================
echo 🌟 SYSTEM ONLINE
echo Backend: http://localhost:8000/docs
echo Frontend: http://localhost:3000
echo ====================================================