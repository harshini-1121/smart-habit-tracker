import React, { useState } from 'react';
import API from '../api';

const Login = ({ setToken, onSwitch }) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // FastAPI's OAuth2PasswordBearer expects a form-data body
            const formData = new FormData();
            formData.append('username', email);
            formData.append('password', password);
            
            const res = await API.post('/token', formData);
            
            // Store token for persistence
            localStorage.setItem('token', res.data.access_token);
            
            // Update parent state to unlock the dashboard
            setToken(res.data.access_token);
        } catch (err) {
            console.error(err);
            alert("Login failed. Please check your email and password.");
        }
    };

    return (
        <div className="auth-card">
            <h2>Welcome Back</h2>
            <form onSubmit={handleSubmit}>
                <input 
                    type="email" 
                    placeholder="Email Address" 
                    value={email}
                    onChange={e => setEmail(e.target.value)} 
                    required 
                />
                <input 
                    type="password" 
                    placeholder="Password" 
                    value={password}
                    onChange={e => setPassword(e.target.value)} 
                    required 
                />
                <button type="submit">Sign In</button>
            </form>

            <p 
                onClick={onSwitch} 
                style={{ 
                    cursor: 'pointer', 
                    marginTop: '15px', 
                    fontSize: '0.9rem', 
                    color: '#3498db',
                    textDecoration: 'underline' 
                }}
            >
                Don't have an account? Sign up
            </p>
        </div>
    );
};

export default Login;