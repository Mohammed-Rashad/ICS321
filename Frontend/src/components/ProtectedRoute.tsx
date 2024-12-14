import React from 'react';
import { Navigate } from 'react-router-dom';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  
  const role = localStorage.getItem('role');

  if (!role || role !== 'admin') {
    // Redirect to login if no token
    return <Navigate to="/adminLogin" replace />;
  }

  return <>{children}</>;
};

export default ProtectedRoute;