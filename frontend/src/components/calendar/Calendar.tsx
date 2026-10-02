import React, { useState, useEffect } from 'react';
import { format, addMonths, subMonths, startOfMonth, endOfMonth, eachDayOfInterval, isSameMonth, isToday, parseISO } from 'date-fns';
import { Link } from 'react-router-dom';

interface CalendarDay {
  day: number;
  hasEntry: boolean;
  title?: string;
  mood?: string;
  favorite: boolean;
  date: Date;
}

interface CalendarProps {
  onDateSelect: (date: Date) => void;
  currentMonth: Date;
  setCurrentMonth: React.Dispatch<React.SetStateAction<Date>>;
  selectedDate: Date | null;
}

const Calendar: React.FC<CalendarProps> = ({ 
  onDateSelect, 
  currentMonth, 
  setCurrentMonth,
  selectedDate
}) => {
  const [days, setDays] = useState<CalendarDay[]>([]);
  
  useEffect(() => {
    // Generate calendar days for current month
    const start = startOfMonth(currentMonth);
    const end = endOfMonth(currentMonth);
    
    const daysArray = eachDayOfInterval({ start, end }).map(day => {
      return {
        day: day.getDate(),
        hasEntry: false, // This would come from API in real implementation
        date: day,
        favorite: false,
        mood: null
      };
    });
    
    setDays(daysArray);
  }, [currentMonth]);
  
  const navigateMonth = (direction: 'prev' | 'next') => {
    setCurrentMonth(prev => 
      direction === 'prev' 
        ? subMonths(prev, 1) 
        : addMonths(prev, 1)
    );
  };
  
  const handleDayClick = (day: CalendarDay) => {
    onDateSelect(day.date);
  };
  
  return (
    <div className="calendar">
      <div className="calendar-header">
        <button onClick={() => navigateMonth('prev')} className="nav-btn">&lt;</button>
        <h2>{format(currentMonth, 'MMMM yyyy')}</h2>
        <button onClick={() => navigateMonth('next')} className="nav-btn">&gt;</button>
      </div>
      
      <div className="calendar-grid">
        {/* Days of week header */}
        {['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'].map(day => (
          <div key={day} className="day-header">{day}</div>
        ))}
        
        {/* Calendar days */}
        {days.map((day, index) => {
          const isCurrentMonth = isSameMonth(day.date, currentMonth);
          const isTodayDate = isToday(day.date);
          const isSelected = selectedDate && day.date.toDateString() === selectedDate.toDateString();
          
          return (
            <div 
              key={index}
              onClick={() => handleDayClick(day)}
              className={`calendar-day ${
                !isCurrentMonth ? 'other-month' : ''
              } ${
                isTodayDate ? 'today' : ''
              } ${
                isSelected ? 'selected' : ''
              }`}
            >
              <span className="day-number">{day.day}</span>
              {day.hasEntry && (
                <div className="entry-indicator">
                  {day.mood && <span className={`mood-${day.mood.toLowerCase()}`}>{day.mood.charAt(0)}</span>}
                  {day.favorite && <span className="favorite">★</span>}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Calendar;