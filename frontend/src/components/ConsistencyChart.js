import React from 'react';

const ConsistencyChart = ({ logs }) => {
    // Generate an array of the last 14 days
    const days = [...Array(14).keys()].map(i => {
        const d = new Date();
        d.setDate(d.getDate() - i);
        return d.toISOString().split('T')[0];
    }).reverse();

    const getStatusColor = (date) => {
        const log = logs.find(l => l.date === date);
        if (!log) return '#ebedf0'; // No data
        return log.status === 'done' ? '#40c463' : '#f85149'; // Green or Red
    };

    const consistencyScore = () => {
        if (logs.length === 0) return 0;
        const doneCount = logs.filter(l => l.status === 'done').length;
        return ((doneCount / logs.length) * 100).toFixed(1);
    };

    return (
        <div className="chart-container">
            <p style={{ fontSize: '0.8rem', marginBottom: '5px' }}>
                Consistency: <strong>{consistencyScore()}%</strong>
            </p>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 12px)', gap: '4px' }}>
                {days.map(day => (
                    <div 
                        key={day} 
                        title={day}
                        style={{ 
                            width: '12px', height: '12px', 
                            backgroundColor: getStatusColor(day),
                            borderRadius: '2px',
                            border: '1px solid rgba(27,31,35,0.06)'
                        }} 
                    />
                ))}
            </div>
        </div>
    );
};

export default ConsistencyChart;