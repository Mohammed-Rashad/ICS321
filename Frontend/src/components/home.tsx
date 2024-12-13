import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const RailwayMainPage: React.FC = () => {
  const [from, setFrom] = useState<string>('');
  const [to, setTo] = useState<string>('');
  const [date, setDate] = useState<string>('');
  // Simulated login state (replace with actual auth context)
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
  const navigate = useNavigate();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Searching for:', { from, to, date });
  };

  const handleLogin = () => {
    navigate('/login');
  };

  return (
    <div>
     
      {/* Rest of the previous component remains the same */}
       {/* Hero Section with Search */}
       <div className="container mx-auto mt-10 px-4">
        <div className="bg-white shadow-lg rounded-lg overflow-hidden">
          <div className="p-6 bg-blue-500 text-white">
            <h2 className="text-3xl font-bold mb-4">Book Your Journey</h2>
            <p className="text-blue-100">Find and book train tickets easily</p>
          </div>

          <form onSubmit={handleSearch} className="p-6 bg-white">
            <div className="grid md:grid-cols-3 gap-4">
              <div>
                <label className="block text-gray-700 mb-2">From</label>
                <input
                  type="text"
                  value={from}
                  onChange={(e) => setFrom(e.target.value)}
                  placeholder="Departure Station"
                  className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label className="block text-gray-700 mb-2">To</label>
                <input
                  type="text"
                  value={to}
                  onChange={(e) => setTo(e.target.value)}
                  placeholder="Arrival Station"
                  className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label className="block text-gray-700 mb-2">Date</label>
                <input
                  type="date"
                  value={date}
                  onChange={(e) => setDate(e.target.value)}
                  className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
            </div>
            <button 
              type="submit" 
              className="w-full mt-6 bg-blue-600 text-white py-3 rounded-md hover:bg-blue-700 transition duration-300"
            >
              Search Trains
            </button>
          </form>
        </div>
      </div>

      {/* Features Section */}
      <div className="container mx-auto mt-10 px-4">
        <div className="grid md:grid-cols-3 gap-6">
          <div className="bg-white p-6 rounded-lg shadow-md text-center">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 mx-auto mb-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
            </svg>
            <h3 className="text-xl font-semibold mb-2">Easy Booking</h3>
            <p className="text-gray-600">Quick and simple ticket reservation process</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md text-center">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 mx-auto mb-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h3 className="text-xl font-semibold mb-2">Real-time Schedules</h3>
            <p className="text-gray-600">Up-to-date train timings and availability</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md text-center">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 mx-auto mb-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h3 className="text-xl font-semibold mb-2">Secure Payments</h3>
            <p className="text-gray-600">Safe and secure online payment methods</p>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="bg-gray-800 text-white mt-10 py-6">
        <div className="container mx-auto text-center">
          <p>&copy; 2024 Railway Ticket System. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default RailwayMainPage;