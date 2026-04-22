import React, { useState } from 'react';
import API from '../api';

const Signup = ({ onSwitch }) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await API.post('/users/', { email, password });
            alert("Account created! You can now log in.");
            onSwitch(); // Switch back to login view
        } catch (err) {
            alert(err.response?.data?.detail || "Signup failed.");
        }
    };

    return (
        <div className="auth-card">
            <h2>Create Account</h2>
            <form onSubmit={handleSubmit}>
                <input type="email" placeholder="Email" onChange={e => setEmail(e.target.value)} required />
                <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} required />
                <button type="submit" style={{ backgroundColor: '#3498db', color: 'white' }}>Sign Up</button>
            </form>
            <p onClick={onSwitch} style={{ cursor: 'pointer', marginTop: '10px', fontSize: '0.9rem', color: '#666' }}>
                Already have an account? Login
            </p>
        </div>
    );
};

export default Signup;