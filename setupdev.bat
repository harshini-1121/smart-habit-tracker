@echo off
echo ====================================================
echo ✨ SMART HABIT TRACKER: DEVELOPER SETUP ✨
echo ====================================================

:: 1. Backend Setup
echo [1/4] Creating Python Virtual Environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python 3.14.
    pause
    exit /b
)

echo [2/4] Installing Backend Dependencies...
call venv\Scripts\activate
pip install --upgrade pip
:: Assumes requirements.txt is inside the backend folder
pip install -r backend/requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install backend requirements.
    pause
    exit /b
)

:: 2. SDK Setup
echo [3/4] Installing Generated Habit SDK...
pip install -e ./habit_sdk
if %errorlevel% neq 0 (
    echo ⚠️ SDK folder not found or install failed. Skipping SDK link...
)

:: 3. Frontend Setup
echo [4/4] Installing Frontend Dependencies...
cd frontend
call npm install
if %errorlevel% neq 0 (
    echo ❌ Node.js/NPM not found. Please install Node.js.
    cd ..
    pause
    exit /b
)
cd ..

echo ====================================================
echo ✅ SETUP COMPLETE!
echo Use 'runapplication.bat' to start the system.
echo ====================================================
pause