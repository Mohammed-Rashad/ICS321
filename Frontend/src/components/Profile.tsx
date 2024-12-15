import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { User, Wallet, Train, CreditCard } from 'lucide-react';

interface PassengerProfile {
  Balance: number;
  Email: string;
  ID: number;
  Name: string;
  Phone: string;
  Trips: Trip[];
}

interface Trip {
  Date: string;
  SeatNumber: number;
  TripNumber: number;
  hasPaid: string;
}

const Profile: React.FC = () => {
  const [profile, setProfile] = useState<PassengerProfile | null>(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    // Check for passengerId in localStorage
    const passengerId = localStorage.getItem('passengerId');
    
    if (!passengerId) {
      // Redirect to login if no passengerId
      navigate('/login');
      return;
    }

    // Fetch passenger profile
    const fetchProfile = async () => {
      try {
        const response = await fetch(`http://localhost:5000/passenger/profile?passengerId=${passengerId}`, {
          method: 'GET',
        });

        if (!response.ok) {
          throw new Error('Failed to fetch profile');
        }

        const data: PassengerProfile = await response.json();
        setProfile(data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching profile:', error);
        navigate('/login');
      }
    };

    fetchProfile();
  }, [navigate]);

  const handlePaymentNavigation = (train: Trip) => {
    navigate('/payment', { 
      state: { 
        train, 
        dependants: [] 
      } 
    });
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-blue-500"></div>
      </div>
    );
  }

  if (!profile) {
    return null;
  }

  return (
    <div className="container mx-auto px-4 py-8 max-w-4xl">
      <div className="bg-white shadow-xl rounded-2xl overflow-hidden">
        {/* Profile Header */}
        <div className="bg-gradient-to-r from-blue-500 to-teal-400 p-6 text-white">
          <div className="flex items-center space-x-4">
            <div className="bg-white/20 rounded-full p-3">
              <User className="h-12 w-12" />
            </div>
            <div>
              <h1 className="text-2xl font-bold">{profile.Name}</h1>
              <p className="text-white/80">{profile.Email}</p>
            </div>
          </div>
        </div>

        {/* Profile Details */}
        <div className="p-6">
          <div className="grid md:grid-cols-2 gap-6">
            {/* Personal Info */}
            <div className="bg-gray-50 p-4 rounded-lg">
              <h2 className="text-xl font-semibold mb-4 text-gray-700 flex items-center">
                <User className="mr-2 text-blue-500" /> Personal Information
              </h2>
              <div className="space-y-2">
                <p><strong>ID:</strong> {profile.ID}</p>
                <p><strong>Phone:</strong> {profile.Phone}</p>
                <p><strong>Email:</strong> {profile.Email}</p>
              </div>
            </div>

            {/* Balance */}
            <div className="bg-gray-50 p-4 rounded-lg">
              <h2 className="text-xl font-semibold mb-4 text-gray-700 flex items-center">
                <Wallet className="mr-2 text-green-500" /> Account Balance
              </h2>
              <div className="text-3xl font-bold text-green-600">
                S.R. {profile.Balance.toFixed(2)}
              </div>
            </div>
          </div>

          {/* Upcoming Trips */}
          <div className="mt-8">
            <h2 className="text-xl font-semibold mb-4 text-gray-700 flex items-center">
              <Train className="mr-2 text-blue-500" /> Upcoming Trips
            </h2>
            {profile.Trips.length === 0 ? (
              <p className="text-gray-500">No upcoming trips</p>
            ) : (
              <div className="space-y-4">
                {profile.Trips.map((trip) => (
                  <div 
                    key={trip.TripNumber + trip.Date} 
                    className="bg-white border rounded-lg p-4 flex justify-between items-center shadow-sm"
                  >
                    <div>
                      <p className="font-medium">Trip #{trip.TripNumber}</p>
                      <p className="text-gray-600">
                        Date: {new Date(trip.Date).toLocaleDateString()}
                      </p>
                      <p className="text-gray-600">
                        Seat: {trip.SeatNumber}
                      </p>
                    </div>
                    {trip.hasPaid === "False" && (
                      <button 
                        onClick={() => handlePaymentNavigation(trip)}
                        className="bg-red-500 text-black px-4 py-2 rounded-md hover:bg-red-600 transition flex items-center"
                      >
                        <CreditCard className="mr-2" /> Pay Now
                      </button>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;