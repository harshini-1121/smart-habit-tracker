import axios from 'axios';

const API = axios.create({
    baseURL: 'http://localhost:8000',
});

// Interceptor to add the JWT token to headers
API.interceptors.request.use((req) => {
    const token = localStorage.getItem('token');
    if (token) {
        req.headers.Authorization = `Bearer ${token}`;
    }
    return req;
});

export default API;