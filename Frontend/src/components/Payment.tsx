import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useNavigate, useLocation } from 'react-router-dom';
import { Train, Search, User, Calendar, MapPin } from 'lucide-react';
import { Button } from './ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

const PaymentPage = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const { train, dependants = [] } = location.state;
  
    const [passengerCount, setPassengerCount] = useState(1 + dependants.length);
  
    const handleAddDependant = () => {
      const name = prompt('Enter dependant name');
      const id = prompt('Enter dependant ID');
      if (name && id) {
        // In a real app, this would be more robust
        navigate('/payment', { 
          state: { 
            train, 
            dependants: [...dependants, { name, id }] 
          } 
        });
      }
      setPassengerCount(passengerCount + 1);
    };
  
    const handlePay = async () => {
      try {
        const response = await fetch('http://localhost:5000/trip/pay', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            tripNumber: train.tripNumber,
            date: new Date(train.date).toLocaleDateString().replace(/\//g, '-'),
            passengerId: localStorage.getItem('passengerId'),
            dependants: dependants
          })
        });
  
        const result = await response.json();
  
        if (response.ok) {
          alert('Payment successful!');
          navigate('/');
        } else {
          alert('Payment failed');
        }
      } catch (error) {
        console.error('Payment error:', error);
        alert('Payment failed');
      }
    };
  
    return (
      <div className="container mx-auto p-4">
        <Card>
          <CardHeader>
            <CardTitle>Payment Details</CardTitle>
          </CardHeader>
          <CardContent>
            <div>
              <p>Train: #{train.trainNumber}</p>
              <p>Route: {train.stations[0]} → {train.stations[train.stations.length - 1]}</p>
              <p>Date: {new Date(train.date).toLocaleDateString()}</p>
              
              <div className="mt-4">
                <h3 className="font-bold">Passengers</h3>
                <p>Main Passenger</p>
                {dependants.map((dep: { name: string; id: string }, index: number) => (
                  <p key={index}>Dependant: {dep.name} (ID: {dep.id})</p>
                ))}
                
                <Button 
                  variant="outline" 
                  className="mt-2" 
                  onClick={handleAddDependant}
                >
                  Add Dependant
                </Button>
              </div>
  
              <div className="mt-4">
                <p>Total Passengers: {passengerCount}</p>
                <p>Total Cost: S.R. {passengerCount * 50}</p>
                
                <Button 
                  className="mt-4 w-full" 
                  onClick={handlePay}
                >
                  Pay Now
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    );
  };

export default PaymentPage;