import React, { useState, useMemo } from 'react';
import { Train, MapPin, Calendar, DollarSign, BookOpen, CheckCircle, Search, X , } from 'lucide-react';

// Sample train data structure matching the described Flask backend
const initialTrains = [
  {
    id: 1,
    source: 'New Delhi',
    destination: 'Mumbai',
    departureDateTime: '2024-12-20 08:30',
    price: 1250
  },
  {
    id: 2,
    source: 'Bangalore',
    destination: 'Chennai',
    departureDateTime: '2024-12-21 10:45',
    price: 850
  },
  {
    id: 3,
    source: 'Kolkata',
    destination: 'Pune',
    departureDateTime: '2024-12-22 14:15',
    price: 1750
  },
  {
    id: 4,
    source: 'Mumbai',
    destination: 'Bangalore',
    departureDateTime: '2024-12-23 07:15',
    price: 1100
  },
  {
    id: 5,
    source: 'Chennai',
    destination: 'Kolkata',
    departureDateTime: '2024-12-24 11:30',
    price: 1300
  }
];

const RailwayBookingSystem = () => {
  const [trains, setTrains] = useState(initialTrains);
  const [selectedTrain, setSelectedTrain] = useState<typeof initialTrains[0] | null>(null);
  const [bookingConfirmed, setBookingConfirmed] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');

  // Memoized filtered trains based on search term
  const filteredTrains = useMemo(() => {
    if (!searchTerm) return trains;

    const searchTermLower = searchTerm.toLowerCase().trim();

    return trains.filter(train => 
      train.source.toLowerCase().includes(searchTermLower) ||
      train.destination.toLowerCase().includes(searchTermLower)
    );
  }, [trains, searchTerm]);

  const handleBookTrain = (train: any) => {
    setSelectedTrain(train);
    setBookingConfirmed(false);
  };

  const confirmBooking = () => {
    setBookingConfirmed(true);
    // In a real app, you'd make an API call here
    setTimeout(() => {
      setSelectedTrain(null);
      setBookingConfirmed(false);
    }, 2000);
  };

  const clearSearch = () => {
    setSearchTerm('');
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-6 text-center flex items-center justify-center">
          <Train className="mr-3" /> Railway Booking System
        </h1>

        {/* Search Input */}
        <div className="mb-6 relative">
          <div className="relative">
            <input 
              type="text" 
              placeholder="Search trains by source or destination"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full p-3 pl-10 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <Search 
              className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" 
              size={20} 
            />
            {searchTerm && (
              <button 
                onClick={clearSearch} 
                className="absolute right-3 top-1/2 transform -translate-y-1/2"
              >
                <X className="text-gray-400 hover:text-gray-600" size={20} />
              </button>
            )}
          </div>
          {searchTerm && filteredTrains.length === 0 && (
            <p className="text-center text-gray-500 mt-4">
              No trains found matching "{searchTerm}"
            </p>
          )}
        </div>

        <div className="space-y-4">
          {filteredTrains.map((train) => (
            <div 
              key={train.id} 
              className="bg-white shadow-md rounded-lg p-4 flex justify-between items-center"
            >
              <div className="flex-grow">
                <div className="flex items-center mb-2">
                  <MapPin className="mr-2 text-blue-600" size={20} />
                  <span className="font-semibold">{train.source} → {train.destination}</span>
                </div>
                <div className="flex items-center mb-2">
                  <Calendar className="mr-2 text-green-600" size={20} />
                  <span>{train.departureDateTime}</span>
                </div>
                <div className="flex items-center">
                  <DollarSign className="mr-2 text-purple-600" size={20} />
                  <span className="font-bold text-lg">S.R. {train.price}</span>
                </div>
              </div>
              <button 
                onClick={() => handleBookTrain(train)}
                className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 flex items-center"
              >
                <BookOpen className="mr-2" /> Book Now
              </button>
            </div>
          ))}
        </div>

        {selectedTrain && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
            <div className="bg-white p-6 rounded-lg shadow-xl w-96">
              {!bookingConfirmed ? (
                <>
                  <h2 className="text-xl font-bold mb-4">Confirm Booking</h2>
                  <div className="mb-4">
                    <p><strong>Route:</strong> {selectedTrain.source} → {selectedTrain.destination}</p>
                    <p><strong>Date:</strong> {selectedTrain.departureDateTime}</p>
                    <p className="font-bold text-lg mt-2">
                      Total Price: S.R. {selectedTrain.price}
                    </p>
                  </div>
                  <div className="flex space-x-4">
                    <button 
                      onClick={() => setSelectedTrain(null)}
                      className="bg-gray-200 text-gray-800 px-4 py-2 rounded-md flex-grow"
                    >
                      Cancel
                    </button>
                    <button 
                      onClick={confirmBooking}
                      className="bg-green-500 text-white px-4 py-2 rounded-md flex-grow"
                    >
                      Confirm Booking
                    </button>
                  </div>
                </>
              ) : (
                <div className="text-center">
                  <CheckCircle className="mx-auto text-green-500 mb-4" size={64} />
                  <h2 className="text-xl font-bold mb-2">Booking Confirmed!</h2>
                  <p>Your ticket has been booked successfully.</p>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default RailwayBookingSystem;