import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import { Box } from "@mui/material";
import Paper from "@mui/material/Paper";
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import dayjs from 'dayjs';

import "./customCss.css"; // Import your custom CSS file

function Form() {
  const navigate = useNavigate();
  const [inputs, setInputs] = useState({
    origin: "",
    destination: "",
    depart_date: null,
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setInputs((prevState) => ({ ...prevState, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
     let formatted_date = dayjs(inputs.depart_date).format('YYYY-MM-DD');
    navigate("/flights", {
      
      state: { origin: inputs.origin, destination: inputs.destination ,depart_date:formatted_date },
    });
  };

  const handleDateChange = (date) => {
    setInputs((prevState) => ({
      ...prevState,
      depart_date: date,
    }));
  };

  return (
    <Box
      component={Paper}
      elevation={5}
      sx={{ backgroundColor: "white", borderRadius: 2 }}
    >
      <form onSubmit={handleSubmit}>
        <Stack sx={{ m: 2 }} direction="row" spacing={2}>
          <TextField
            required
            autoFocus
            id="origin"
            label="From"
            name="origin"
            value={inputs.origin || ""}
            inputProps={{ pattern: "[a-zA-Z]{3,15}$" }}
            onChange={handleChange}
          />
          <TextField
            required
            id="destination"
            label="To"
            name="destination"
            value={inputs.destination || ""}
            inputProps={{ pattern: "[a-zA-Z]{3,15}$" }}
            onChange={handleChange}
          />
     
            <LocalizationProvider dateAdapter={AdapterDayjs}>
            <DatePicker value={inputs.departureDate}
            onChange={handleDateChange} />
            </LocalizationProvider>

          <Button variant="contained" type="submit">
            Search Flight
          </Button>
        </Stack>
      </form>
    </Box>
  );
}

export default Form;
