
# Smart Habit Tracker

A full-stack habit tracking application that helps users build consistency by managing daily habits, tracking progress, and maintaining structured records.

---

## Problem Statement

Maintaining habits consistently is challenging due to lack of tracking systems and progress visibility. Users often fail to stay consistent because they cannot monitor their performance effectively.

---

## Solution

This project provides a structured habit tracking system where users can create, manage, and monitor their habits. The system ensures better consistency by tracking daily progress and storing data efficiently.

---

## Features

* Create, update, and delete habits
* Track daily habit completion
* Backend API built with FastAPI
* Persistent data storage using SQLite
* Modular frontend using React
* Clean separation of frontend and backend

---

## Tech Stack

Frontend: React, JavaScript, CSS
Backend: FastAPI (Python)
Database: SQLite
API Testing: Pytest
Version Control: Git, GitHub

---

## Project Structure

```id="proj-structure"
smart-habit-tracker/

backend/
│
├── app/                  # Core backend logic
├── __pycache__/          # Python cache files
├── alembic.ini           # Database migration config
├── habit_tracker.db      # SQLite database
├── seed_data.sql         # Initial data setup
├── requirements.txt      # Python dependencies
├── test_main.py          # Backend test cases
└── test.db               # Test database

frontend/
│
├── public/               # Static files
└── src/
    ├── components/       # React components
    ├── api.js            # API integration
    ├── App.js            # Main app logic
    ├── App.css           # Styling
    ├── index.js          # Entry point
    └── other config files

habit_sdk/                # SDK or helper modules
openapitools.json         # API config
runapplication.bat        # Script to run application
README.md
```

---

## System Architecture

The application follows a client-server architecture.

Frontend (React) handles user interaction and sends requests to the backend API.
Backend (FastAPI) processes requests, interacts with the database, and returns responses.

Flow:

User → React Frontend → FastAPI Backend → SQLite Database → Response → UI

---

## Installation and Setup

### 1. Clone the repository

git clone [https://github.com/harshini-1121/smart-habit-tracker.git](https://github.com/harshini-1121/smart-habit-tracker.git)

---

### 2. Setup Backend

cd smart-habit-tracker/backend

pip install -r requirements.txt

uvicorn main:app --reload

---

### 3. Setup Frontend

cd ../frontend

npm install

npm start

---

### 4. Access the Application

Backend runs on: [http://127.0.0.1:8000](http://127.0.0.1:8000)
Frontend runs on: [http://localhost:3000](http://localhost:3000)

---

## Testing

To run backend tests:

pytest

---

## Future Enhancements

* User authentication system
* Habit reminders and notifications
* Data visualization dashboard
* AI-based habit suggestions
* Deployment on cloud platform

---

## Author

Harshini T N
Email: [harshinitn21@gmail.com](mailto:harshinitn21@gmail.com)

