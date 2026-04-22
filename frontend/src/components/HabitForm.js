import React, { useState } from 'react';

const HabitForm = ({ onAdd }) => {
    const [name, setName] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (name.trim()) {
            onAdd(name);
            setName('');
        }
    };

    return (
        <form className="habit-form" onSubmit={handleSubmit}>
            <input 
                type="text" 
                value={name} 
                onChange={e => setName(e.target.value)} 
                placeholder="What habit are we starting?" 
                required
            />
            <button type="submit">Add Habit</button>
        </form>
    );
};

export default HabitForm;