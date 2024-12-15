// import Message from "./message"
import ListGroup from "./components/ListGroup";
import LoginPage from "./components/LoginPage";
import RailwayMainPage from "./components/home";
import { Routes, Route, Navigate } from 'react-router-dom';
import UserProfile from "./components/UserProfile";
import Main from "./components/Main";
import AdminLoginPage from "./components/AdminLogin";
import ProtectedRoute from './components/ProtectedRoute';
import RailwayDashboard from "./components/RailWayDashboard";
import SignupForm from "./components/SignUp";
import RailwayApp from "./components/RailwayApp";
import PaymentPage from "./components/Payment";
import Profile from "./components/Profile";
// you can use the components in other components
function App() { 
  return (
    <Routes>
      <Route path="/" element={<RailwayApp />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/signup" element={<SignupForm />} />
      <Route path="/payment" element={<PaymentPage />} />
      <Route 
          path="/dashboard" 
          element={
            <ProtectedRoute>
              <RailwayDashboard />
            </ProtectedRoute>
          } 
        />
      <Route path="/profile" element={<Profile />} />
      <Route path="/adminLogin" element={<AdminLoginPage />} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}

export default App;