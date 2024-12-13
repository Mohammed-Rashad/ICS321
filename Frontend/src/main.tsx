import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './input.css'
import App from './App.tsx'
import { BrowserRouter as Router } from 'react-router-dom'
import React from 'react'
import RailwayMainPage from './components/home.tsx'

createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>,
)
