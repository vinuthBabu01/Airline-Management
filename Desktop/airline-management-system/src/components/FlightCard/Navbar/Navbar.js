import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';
import { useNavigate } from 'react-router-dom';

const Navbar = () => {

   const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('authorization'));
    let navigate = useNavigate(); 
    const handleLogout = () => {
        localStorage.removeItem('userId');
        localStorage.removeItem('authorization');
        setIsLoggedIn(false)
        navigate('/');
    };

    const handleLogin = () => {
        // Perform login actions (e.g., authenticate user, store token in localStorage)
        // localStorage.setItem('token', 'your_auth_token_here');
        navigate('/user/login');
        setIsLoggedIn(true);
    };



    return (
        <div>
        <nav className="navbar navbar-expand-lg">
            <div >
                <h1 className="navbar-title">Airline Management System</h1>
            </div>
            <div className="navbar-links">

                {isLoggedIn && (
                    <div>
                        <Link to="/user/dashboard" className="navbar-link">
                            My Bookings
                        </Link>
                        <button onClick={handleLogout} className="logout-button">
                            Logout
                        </button>
                    </div>
                )}

                {!isLoggedIn && (
                    <button onClick={handleLogin} className="logout-button">
                        Log In
                    </button>
                )}


            </div>
        </nav>
        </div>
    );
};

export default Navbar;
