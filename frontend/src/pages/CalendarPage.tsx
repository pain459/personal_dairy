import React, { useState, useEffect } from 'react';
import Calendar from '../components/calendar/Calendar';
import { format } from 'date-fns';
import { useNavigate } from 'react-router-dom';

const CalendarPage: React.FC = () => {
  const [currentMonth, setCurrentMonth] = useState<Date>(new Date());
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);
  const navigate = useNavigate();
  
  const handleDateSelect = (date: Date) => {
    setSelectedDate(date);
    // Navigate to the day page
    const dateString = format(date, 'yyyy-MM-dd');
    navigate(`/day/${dateString}`);
  };
  
  return (
    <div className="calendar-page">
      <h1>My Diary</h1>
      <Calendar 
        onDateSelect={handleDateSelect}
        currentMonth={currentMonth}
        setCurrentMonth={setCurrentMonth}
        selectedDate={selectedDate}
      />
    </div>
  );
};

export default CalendarPage;