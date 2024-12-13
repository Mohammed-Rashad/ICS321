// import Message from "./message"
import ListGroup from "./components/ListGroup";
import LoginPage from "./components/LoginPage";
import RailwayMainPage from "./components/home";
import { Routes, Route } from 'react-router-dom';
import UserProfile from "./components/UserProfile";
import Main from "./components/Main";
import AdminLoginPage from "./components/AdminLogin";
// you can use the components in other components
function App() { 
  return (
    <Routes>
      <Route path="/" element={<Main />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/profile" element={<UserProfile />} />
      <Route path="/adminLogin" element={<AdminLoginPage />} />
    </Routes>
  )
}

export default App;