import './App.css';
import Login from './Login';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom'; // Import necessary components from React Router
import React,{useState,useEffect}from 'react'
import  Register  from './Register';

function App() {
  return (
    <Router>
      <Routes>
        {/* Set the "/" path to render the Login component */}
        <Route exact path="/" element={<Login/>}/>
        {/* Set the "/register" path to render the Register component */}
        <Route exact path="/register" element={<Register/>}/>
      </Routes>
    </Router>
  );
}

export default App;
