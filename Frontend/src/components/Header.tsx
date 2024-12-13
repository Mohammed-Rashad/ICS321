import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Header: React.FC = () => {
  // Simulated login state (replace with actual auth context)
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
  const navigate = useNavigate();


  const handleLogin = () => {
    navigate('/login');
  };

  return (
      <header className="bg-blue-600 text-white p-4 shadow-md">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-bold">Railway Ticket System</h1>
          <nav className="space-x-4 flex items-center">
            <a href="#" className="hover:text-blue-200">Home</a>
            <a href="#" className="hover:text-blue-200">Bookings</a>
            <a href="#" className="hover:text-blue-200">Schedule</a>
            <a href="#" className="hover:text-blue-200">Contact</a>
            {!isLoggedIn ? (
              <button 
                onClick={handleLogin}
                className="bg-white text-blue-600 px-4 py-2 rounded-md hover:bg-blue-50"
              >
                Login
              </button>
            ) : (
              // User profile or logout option would go here
              <span>Welcome, User</span>
            )}
          </nav>
        </div>
      </header>
  );
};

export default Header;