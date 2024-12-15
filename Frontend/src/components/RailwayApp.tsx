import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useNavigate, useLocation } from 'react-router-dom';
import { Train, Search, User, Calendar, MapPin } from 'lucide-react';
import { Button } from './ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';


// Main Train List Component
interface Train {
  tripNumber: string;
  date: string;
  stations: string[];
  times: string[];
}

const TrainList = () => {
  const [trains, setTrains] = useState<Train[]>([]);
  const [searchParams, setSearchParams] = useState({
    source: '',
    destination: '',
    date: ''
  });

  useEffect(() => {
    fetchTrains();
  }, []);

  const fetchTrains = async () => {
    try {
      const response = await fetch('http://localhost:5000/trip/allFuture');
      const data = await response.json();
      console.log('Fetched trains:', data.Trips);
      setTrains(data.Trips);
    } catch (error) {
      console.error('Error fetching trains:', error);
    }
  };

  const filteredTrains = trains.filter(train => {
    const matchSource = !searchParams.source || 
      train.stations[0].toLowerCase().includes(searchParams.source.toLowerCase());
    const matchDestination = !searchParams.destination || 
      train.stations[train.stations.length - 1].toLowerCase().includes(searchParams.destination.toLowerCase());
    const matchDate = !searchParams.date || 
      new Date(train.date).toDateString() === new Date(searchParams.date).toDateString();
    
    return matchSource && matchDestination && matchDate;
  });

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4 flex items-center">
        <Train className="mr-2" /> Railway Booking System
      </h1>
      
      {/* Search Inputs */}
      <div className="flex space-x-2 mb-4">
        <div className="flex items-center space-x-2">
          <MapPin />
          <Input 
            placeholder="Source" 
            value={searchParams.source}
            onChange={(e) => setSearchParams({...searchParams, source: e.target.value})}
          />
        </div>
        <div className="flex items-center space-x-2">
          <MapPin />
          <Input 
            placeholder="Destination" 
            value={searchParams.destination}
            onChange={(e) => setSearchParams({...searchParams, destination: e.target.value})}
          />
        </div>
        <div className="flex items-center space-x-2">
          <Calendar />
          <Input 
            type="date" 
            value={searchParams.date}
            onChange={(e) => setSearchParams({...searchParams, date: e.target.value})}
          />
        </div>
      </div>

      {/* Train List */}
      <div className="grid gap-4">
        {filteredTrains.map((train) => (
          <TrainCard key={`${train.tripNumber}-${train.date}`} train={train} />
        ))}
      </div>
    </div>
  );
};

// Train Card Component
const TrainCard = ({ train }: { train: Train }) => {
  const navigate = useNavigate();

  const handleBooking = async () => {
    const passengerId = localStorage.getItem('passengerId');
    if (!passengerId) {
      alert('Please login first');
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/trip/book', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          passengerId,
          tripNumber: train.tripNumber,
          date: new Date(train.date).toLocaleDateString().replace(/\//g, '-')
        })
      });

      const result = await response.json();

      if (result.status === 'reserved') {
        navigate('/payment', { 
          state: { 
            train, 
            dependants: [] 
          } 
        });
      } else if (result.status === 'waitlisted') {
        navigate('/profile');
      } else {
        alert('Booking failed: ' + result.message);
      }
    } catch (error) {
      console.error('Booking error:', error);
      alert('Booking failed');
    }
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle>Train #{train.tripNumber}</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex justify-between items-center">
          <div>
            <p className="font-bold">
              {train.stations[0]} → {train.stations[train.stations.length - 1]}
            </p>
            <p>{new Date(train.date).toLocaleDateString()}</p>
            <p>Departure: {train.times[0]}</p>
          </div>
          <Button onClick={handleBooking}>Book Now</Button>
        </div>
      </CardContent>
    </Card>
  );
};

// Payment Component


// Main App Component with Routing
const RailwayApp = () => {
  return (
    // <Router>
    //   <Routes>
    //     <Route path="/" element={<TrainList />} />
    //     <Route path="/payment" element={<PaymentPage />} />
    //   </Routes>
    // </Router>
    <TrainList />
  );
};

export default RailwayApp;