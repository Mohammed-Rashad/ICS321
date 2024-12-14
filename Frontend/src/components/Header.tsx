import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Header: React.FC = () => {
  // Simulated login state (replace with actual auth context)
  // const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
  const navigate = useNavigate();
  // get loggedIn from local storage
  const loggedIn = localStorage.getItem('loggedIn');
  
  // setIsLoggedIn(loggedIn == 'true');
  const name = localStorage.getItem('username');
  const handleLogin = () => {
    navigate('/login');
  };
  const handleSignUp = () => {
    navigate('/signup');
  };
  const signout = async () => {
    // clear local storage
    localStorage.clear();
    await fetch('http://localhost:5000/auth/userLogout', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    });
    navigate('/login');
    // redirect to login
    // window.location.href = '/login';
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
            {!loggedIn ? (
              // put margin between buttons
              <div className="space-x-4 mx-auto">
              <button 
                onClick={handleLogin}
                className="bg-white text-blue-600 px-4 py-2 rounded-md hover:bg-blue-50"
              >
                Login
              </button>
              <button 
                onClick={handleSignUp}
                className="bg-white text-blue-600 px-4 py-2 rounded-md hover:bg-blue-50"
              >
                Sing Up
              </button>
              </div>
              
            ) : (
              // User profile or logout option would go here
              <div>
              <span>Welcome, {name}</span>
              <button onClick={signout} className={"bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 flex items-center text-xs"}>Sign Out</button>
              </div>
              
            )}
          </nav>
        </div>
      </header>
  );
};

export default Header;