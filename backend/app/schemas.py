from pydantic import BaseModel, Field
import datetime  # Changed from 'from datetime import date' to avoid name clash
from typing import List, Optional

# --- 👤 USER SCHEMAS ---

class UserCreate(BaseModel):
    """Schema for user registration."""
    email: str = Field(
        ..., 
        example="user@example.com", 
        description="The unique email address used for identity and notifications."
    )
    password: str = Field(
        ..., 
        min_length=8, 
        example="securePassword123", 
        description="User password. Must be at least 8 characters long."
    )

class UserResponse(BaseModel):
    """Schema for public-facing user information (no password)."""
    id: int = Field(..., example=1, description="The unique database ID of the user.")
    email: str = Field(..., example="user@example.com", description="The user's registered email.")

    class Config:
        from_attributes = True


# --- 🔑 AUTH SCHEMAS ---

class Token(BaseModel):
    """Schema for the JWT access token response."""
    access_token: str = Field(..., description="The encoded JWT string.")
    token_type: str = Field(..., example="bearer", description="The type of token issued.")


# --- 🏃 HABIT SCHEMAS ---

class HabitBase(BaseModel):
    """Base properties shared across habit schemas."""
    name: str = Field(
        ..., 
        min_length=1, 
        max_length=100, 
        example="Morning Meditation", 
        description="The descriptive name of the habit you want to track."
    )

class HabitCreate(HabitBase):
    """Schema for creating a new habit."""
    pass

class Habit(HabitBase):
    """Full representation of a Habit in the database."""
    id: int = Field(..., example=5, description="Unique identifier for the habit.")
    streak: int = Field(
        ..., 
        example=12, 
        description="Current consecutive days the habit has been completed."
    )
    last_processed_date: datetime.date = Field( # Updated to datetime.date
        ..., 
        description="The last date the system checked or updated this habit's streak."
    )

    class Config:
        from_attributes = True


# --- 📊 LOG & ANALYTICS SCHEMAS ---

class LogUpdate(BaseModel):
    """Schema for submitting a daily habit status."""
    status: str = Field(
        ..., 
        pattern="^(done|missed)$", 
        example="done", 
        description="The status of the habit for today. Must be exactly 'done' or 'missed'."
    )

class LogResponse(BaseModel):
    """Detailed history of a habit activity for charts."""
    id: int = Field(..., description="Unique ID of the specific log entry.")
    habit_id: int = Field(..., description="The ID of the parent habit.")
    date: datetime.date = Field(..., description="The calendar date this log refers to.") # Updated to datetime.date
    status: str = Field(..., example="done", description="Completion status ('done' or 'missed').")

    class Config:
        from_attributes = True