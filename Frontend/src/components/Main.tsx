import React, { useState } from 'react';
import RailwayMainPage from './home';
import Header from './Header';
import RailwayBookingSystem from './RailwayBookingSystem';

const Main: React.FC = () => {
  

  return (
        <>
            <Header />
            <RailwayBookingSystem />
        </>
  );
};

export default Main;