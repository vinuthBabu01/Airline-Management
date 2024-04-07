// UserSignUp.js
import React, { useState, useEffect, useRef } from 'react';
import './UserSignUp.css'; // Import the UserSignUp.css file for styles
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import Loading from '../../components/Loading/Loading';
// import Loading from '../../Loading/Loading';
import { faCheck, faTimes, faInfoCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";


const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const PWD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$/;

const UserSignUp = () => {

  const [role, setRole] = useState('');
  
  const [email, setEmail] = useState('');
  const [ValidEmail, setValidEmail] = useState(false);
  const [userFocus, setUserFocus] = useState(false);

  const [password, setPassword] = useState('');
  const [validPwd, setValidPwd] = useState(false);
  const [pwdFocus, setPwdFocus] = useState(false);

  const [fullName, setFullName] = useState('');
  const [ValidName, setValidName] = useState(false);
  const [NameFocus, setNameFocus] = useState(false);

  const [confirmPassword, setConfirmPassword] = useState('');
  const [validMatch, setValidMatch] = useState(false);
  const [matchFocus, setMatchFocus] = useState(false);
   
  const [errMsg, setErrMsg] = useState('');
  const [success, setSuccess] = useState(false);
  const [loading, setLoading] = useState(false);
  let navigate = useNavigate();

  // const handleSubmit = (e) => {
  //   e.preventDefault();
  //   // Perform user sign-up logic here
  //   console.log('User Sign Up:', email, password, fullName, confirmPassword);
  // };
  
  useEffect(() => {
    // Check if name is not blank
    setValidName(fullName.trim() !== '');
  }, [fullName]);

  useEffect(() => {
    setValidEmail(EMAIL_REGEX.test(email));
  }, [email]);

  useEffect(() => {
    setValidPwd(PWD_REGEX.test(password));
    setValidMatch(password === confirmPassword);
  }, [password, confirmPassword]);

  useEffect(() => {
    setErrMsg('');
  }, [email, password, confirmPassword]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const v3 = fullName.trim() !== ''; // Check if name is not blank
    const v1 = EMAIL_REGEX.test(email);
    const v2 = PWD_REGEX.test(password);
    if (!v1 || !v2 || !v3) {
      setErrMsg("Invalid Entry");
      return;
    }
    try {
      // Send login data to the backend
      setLoading(true);
      const response = await axios.post('https://devrev-assessment.onrender.com/api/user/signUp', {
        name: fullName,
        email: email,
        password: password,
        passwordConfirm: confirmPassword,

      });

      // console.log(response.data.token);
      setLoading(false);
      console.log(response)
      if (response.status === 201) {
        // If signup is successful, navigate to the login page
        navigate('/user/login');
      }

      // ... (remaining code)
    } catch (error) {
      // Handle login error
      console.error('Login error:', error.response.data);
    }
  };

  return (
    <div className="user-signup-container">
      {loading && <Loading/>}
      <h2 className="user-signup-title">User Sign Up</h2>
      <form onSubmit={handleSubmit} className="user-signup-form">
        <div className="form-group">
          <label htmlFor="Role">Role:</label>
          <select placeholder="Role" required className="custom-select"
                value={role} onChange={(e) => setRole(e.target.value)}>
                <option value="" disabled>Select Role</option>
                <option value="User">User</option>
                <option value="Admin">Admin</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="fullName">Full Name:</label>
          <input
            className="custom-select"
            type="text"
            id="fullName"
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
            required
            autoComplete="off"
                aria-invalid={setFullName ? "false" : "true"}
                aria-describedby="uidnote"
                onFocus={() => setNameFocus(true)}
                onBlur={() => setNameFocus(false)}
          />
        </div>
        <p id="uidnote" className={NameFocus && fullName && !ValidName ? "instructions" : "offscreen"}>
                <FontAwesomeIcon icon={faInfoCircle} />
                Name cannot be blank
              </p>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            autoComplete="off"
                aria-invalid={setEmail ? "false" : "true"}
                aria-describedby="uidnote"
                onFocus={() => setUserFocus(true)}
                onBlur={() => setUserFocus(false)}
          />
        </div>
        <p id="uidnote" className={userFocus && email && !ValidEmail ? "instructions" : "offscreen"}>
                <FontAwesomeIcon icon={faInfoCircle} />
                4 to 24 characters.<br />
                Must begin with a letter.<br />
                Letters, numbers, underscores, hyphens allowed.
              </p>

        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            aria-invalid={validPwd ? "false" : "true"}
            aria-describedby="pwdnote"
            onFocus={() => setPwdFocus(true)}
            onBlur={() => setPwdFocus(false)}
          />
        </div>
        <p id="pwdnote" className={pwdFocus && !validPwd ? "instructions" : "offscreen"}>
                <FontAwesomeIcon icon={faInfoCircle} />
                8 to 24 characters.<br />
                Must include uppercase and lowercase letters, a number and a special character.<br />
                Allowed special characters: <span aria-label="exclamation mark">!</span> <span aria-label="at symbol">@</span> <span aria-label="hashtag">#</span> <span aria-label="dollar sign">$</span> <span aria-label="percent">%</span>
        </p>
              
        <div className="form-group">
          <label htmlFor="confirm Password">Confirm Password:</label>
          <input
            type="password"
            id="confirmPassword"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
            aria-invalid={validMatch ? "false" : "true"}
            aria-describedby="confirmnote"
            onFocus={() => setMatchFocus(true)}
            onBlur={() => setMatchFocus(false)}
          />
        </div>
        <p id="confirmnote" className={matchFocus && !validMatch ? "instructions" : "offscreen"}>
                <FontAwesomeIcon icon={faInfoCircle} />
                Must match the first password input field.
              </p>
        
        <button type="submit" className="signup-button">
          Sign Up
        </button>
      </form>
    </div>
  );
};

export default UserSignUp;
