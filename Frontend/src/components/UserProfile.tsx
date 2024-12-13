import React, { useState } from 'react';
import { User, Ticket, Train } from 'lucide-react';

const UserProfile = () => {
  const [user] = useState({
    name: 'John Doe',
    email: 'john.doe@example.com',
    memberId: 'RW23456789',
    points: 1250
  });

  const [tickets] = useState([
    {
      id: 'RT12345',
      from: 'New York',
      to: 'Boston',
      date: '2024-02-15',
      time: '10:30 AM',
      status: 'Confirmed',
      type: 'One Way'
    },
    {
      id: 'RT67890',
      from: 'Boston',
      to: 'Philadelphia',
      date: '2024-03-20',
      time: '2:45 PM',
      status: 'Pending',
      type: 'Round Trip'
    }
  ]);

  return (
    
    <div className="max-w-2xl mx-auto p-6 bg-gray-100 min-h-screen">
      <div className="bg-white shadow-md rounded-lg p-6">
        {/* User Profile Section */}
        <div className="flex items-center mb-6">
          <div className="bg-blue-500 text-white rounded-full p-4 mr-4">
            <User size={48} />
          </div>
          <div>
            <h1 className="text-2xl font-bold text-gray-800">{user.name}</h1>
            <p className="text-gray-600">{user.email}</p>
            <div className="flex items-center mt-2">
              <span className="text-sm bg-green-100 text-green-800 px-2 py-1 rounded mr-2">
                Member ID: {user.memberId}
              </span>
              <span className="text-sm bg-yellow-100 text-yellow-800 px-2 py-1 rounded">
                Points: {user.points}
              </span>
            </div>
          </div>
        </div>

        {/* Tickets Section */}
        <div className="border-t pt-6">
          <h2 className="text-xl font-semibold mb-4 text-gray-700">My Tickets</h2>
          {tickets.map((ticket) => (
            <div 
              key={ticket.id} 
              className="bg-gray-50 border rounded-lg p-4 mb-4 flex items-center justify-between hover:bg-gray-100 transition-colors"
            >
              <div className="flex items-center">
                <Train size={36} className="text-blue-500 mr-4" />
                <div>
                  <p className="font-bold text-gray-800">
                    {ticket.from} → {ticket.to}
                  </p>
                  <p className="text-gray-600">
                    {ticket.date} | {ticket.time}
                  </p>
                  <span className={`
                    text-sm px-2 py-1 rounded 
                    ${ticket.status === 'Confirmed' 
                      ? 'bg-green-100 text-green-800' 
                      : 'bg-yellow-100 text-yellow-800'
                    }
                  `}>
                    {ticket.type} - {ticket.status}
                  </span>
                </div>
              </div>
              <div>
                <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition-colors">
                  View Details
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default UserProfile;