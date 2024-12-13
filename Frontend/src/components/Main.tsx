import React, { useState } from 'react';
import RailwayMainPage from './home';
import Header from './header';

const Main: React.FC = () => {
  

  return (
        <>
            <Header />
            <RailwayMainPage />
        </>
  );
};

export default Main;