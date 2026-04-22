import React, { useState, useEffect } from 'react';
import API from './api';
import Login from './components/Login';
import Signup from './components/Signup';
import HabitForm from './components/HabitForm';
import HabitItem from './components/HabitItem';
import ConsistencyChart from './components/ConsistencyChart';
import './App.css';

function App() {
  const [habits, setHabits] = useState([]);
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [showLogin, setShowLogin] = useState(true);

  const fetchHabits = async () => {
    try {
      const res = await API.get('/habits/');
      const habitsWithHistory = await Promise.all(
        res.data.map(async (habit) => {
          const historyRes = await API.get(`/habits/${habit.id}/history`);
          return { ...habit, history: historyRes.data };
        })
      );
      setHabits(habitsWithHistory);
    } catch (e) {
      if (e.response?.status === 401) logout();
    }
  };

  useEffect(() => {
    if (token) fetchHabits();
  }, [token]);

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
  };

  if (!token) {
    return showLogin ? (
      <Login setToken={setToken} onSwitch={() => setShowLogin(false)} />
    ) : (
      <Signup onSwitch={() => setShowLogin(true)} />
    );
  }

  return (
    <div className="container">
      <header>
        <h1>Smart Habit Tracker</h1>
        <button className="btn-logout" onClick={logout}>Logout</button>
      </header>

      <HabitForm onAdd={async (name) => { await API.post('/habits/', { name }); fetchHabits(); }} />

      <div className="global-actions">
        <button className="btn-sim-rem" onClick={async () => { 
          await API.post(`/habits/simulate-reminder`); 
          alert("Check terminal for reminder!"); 
        }}>
          🚀 Simulate Pending Reminder (All)
        </button>
      </div>

      <div className="habit-list">
        {habits.map(h => (
          <div key={h.id} className="habit-card">
            <HabitItem 
              habit={h} 
              onLog={async (id, status) => {
                try {
                  await API.patch(`/habits/${id}/log`, { status });
                  fetchHabits();
                } catch (e) { alert(e.response?.data?.detail); }
              }} 
            />
            
            <ConsistencyChart logs={h.history || []} />

            <div className="debug-footer">
              <button className="btn-almost" onClick={async () => { 
                await API.post(`/habits/${h.id}/simulate-almost-missed`); 
                alert("Triggered 10:00 PM logic. Check terminal.");
              }}>
                ⏳ Sim Almost Missed
              </button>

              <button className="btn-gap" onClick={async () => { 
                await API.post(`/habits/${h.id}/simulate-gap`); 
                fetchHabits(); 
                alert("Gap simulated!");
              }}>
                💀 Sim 3-Day Miss
              </button>

              <button className="btn-reset" onClick={async () => { 
                await API.post(`/habits/${h.id}/debug-reset`); 
                fetchHabits(); 
              }}>
                🔄 Reset
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;