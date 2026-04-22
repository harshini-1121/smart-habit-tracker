import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
import datetime

# --- Setup Test Database ---
# We use a separate sqlite file for testing to avoid wiping your real data
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    """Wipes and recreates the database before every single test."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# --- Helper Functions ---

def get_auth_headers(email="user@test.com", password="password123"):
    """Helper to register and login a user to get a bearer token."""
    client.post("/users/", json={"email": email, "password": password})
    response = client.post("/token", data={"username": email, "password": password})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

# --- Test Cases ---

def test_auth_flow():
    """Tests registration and login."""
    # Signup
    signup = client.post("/users/", json={"email": "new@test.com", "password": "password123"})
    assert signup.status_code == 200
    
    # Login
    login = client.post("/token", data={"username": "new@test.com", "password": "password123"})
    assert login.status_code == 200
    assert "access_token" in login.json()

def test_habit_creation_and_done_log():
    """Tests creating a habit and marking it as done."""
    headers = get_auth_headers()
    
    # Create Habit
    res = client.post("/habits/", json={"name": "Exercise"}, headers=headers)
    assert res.status_code == 200
    habit_id = res.json()["id"]

    # Log Done (Streak should go to 1)
    log_res = client.patch(f"/habits/{habit_id}/log", json={"status": "done"}, headers=headers)
    assert log_res.json()["streak"] == 1

    # Prevent Double-Logging for the same day
    double_log = client.patch(f"/habits/{habit_id}/log", json={"status": "done"}, headers=headers)
    assert double_log.status_code == 400
    assert "Already logged" in double_log.json()["detail"]

def test_streak_reset_on_manual_miss():
    """Tests that marking a habit as missed resets the streak to 0."""
    headers = get_auth_headers()
    res = client.post("/habits/", json={"name": "Read"}, headers=headers)
    habit_id = res.json()["id"]

    # Increment streak to 1
    client.patch(f"/habits/{habit_id}/log", json={"status": "done"}, headers=headers)
    
    # Clear the 'already logged' status for testing using our debug endpoint
    client.post(f"/habits/{habit_id}/debug-reset", headers=headers)

    # Log Missed
    log_res = client.patch(f"/habits/{habit_id}/log", json={"status": "missed"}, headers=headers)
    assert log_res.json()["streak"] == 0

def test_smart_sync_3_day_absence():
    """
    Tests the 'Trick Requirement':
    Simulates a 3-day absence. When /habits/ is called, the system should 
    automatically detect the gap and reset the streak.
    """
    headers = get_auth_headers()
    res = client.post("/habits/", json={"name": "Study"}, headers=headers)
    habit_id = res.json()["id"]

    # Set streak to 1
    client.patch(f"/habits/{habit_id}/log", json={"status": "done"}, headers=headers)
    
    # Simulate 3-Day Gap (hacks the DB date back 4 days)
    client.post(f"/habits/{habit_id}/simulate-gap", headers=headers)

    # Trigger Sync (Happens on GET)
    sync_res = client.get("/habits/", headers=headers)
    habits = sync_res.json()
    target_habit = next(h for h in habits if h["id"] == habit_id)
    
    # Streak must be 0 because the user missed days
    assert target_habit["streak"] == 0

def test_analytics_history_endpoint():
    """Tests that the analytics endpoint returns the history needed for the chart."""
    headers = get_auth_headers()
    res = client.post("/habits/", json={"name": "Meditate"}, headers=headers)
    habit_id = res.json()["id"]

    # Add a log
    client.patch(f"/habits/{habit_id}/log", json={"status": "done"}, headers=headers)
    
    # Check history
    history_res = client.get(f"/habits/{habit_id}/history", headers=headers)
    assert history_res.status_code == 200
    assert len(history_res.json()) >= 1
    assert history_res.json()[0]["status"] == "done"