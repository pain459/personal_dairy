import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import CalendarPage from './pages/CalendarPage';
import DayPage from './pages/DayPage';
import TimelinePage from './pages/TimelinePage';
import PhotosPage from './pages/PhotosPage';
import SearchPage from './pages/SearchPage';
import SettingsPage from './pages/SettingsPage';
import Header from './components/common/Header';

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<CalendarPage />} />
            <Route path="/calendar" element={<CalendarPage />} />
            <Route path="/day/:date" element={<DayPage />} />
            <Route path="/timeline" element={<TimelinePage />} />
            <Route path="/photos" element={<PhotosPage />} />
            <Route path="/search" element={<SearchPage />} />
            <Route path="/settings" element={<SettingsPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;