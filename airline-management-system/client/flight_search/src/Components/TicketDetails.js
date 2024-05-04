import React, { useState } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Paper from '@mui/material/Paper';
import CircularProgress from '@mui/material/CircularProgress';
import { styled } from '@mui/material/styles';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableRow from '@mui/material/TableRow';
import { blue } from '@mui/material/colors';
import { Box, Stack, Typography } from '@mui/material';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

const StyledTableCell = styled(TableCell)(({ theme }) => ({
    [`&.${tableCellClasses.head}`]: {
        backgroundColor: blue[800],
        color: theme.palette.common.white,
    },
    [`&.${tableCellClasses.body}`]: {
        fontSize: 14,
    },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
    '&:nth-of-type(odd)': {
        backgroundColor: theme.palette.action.hover,
    },
    '&:last-child td, &:last-child th': {
        border: 0,
    },
}));

const SearchTicket = () => {
    const [ticketId, setTicketId] = useState('');
    const [ticketDetails, setTicketDetails] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleSearch = (event) => {
        event.preventDefault();
        setIsLoading(true);
        setError(null);

        // Assuming the API endpoint for fetching ticket details is '/tickets/:ticketId'
        axios.get(`/tickets/${ticketId}`)
            .then(response => {
                setIsLoading(false);
                setTicketDetails(response.data);
            })
            .catch(error => {
                setIsLoading(false);
                setError(error.message);
            });
    };

    const handleChange = (event) => {
        const value = event.target.value;
        setTicketId(value);
    };    

    const handlePrintTicket = () => {
        const filename = 'ticket.pdf';
        const element = document.getElementById('ticket-details');

        html2canvas(element).then((canvas) => {
            const imgData = canvas.toDataURL('image/png');
            const pdf = new jsPDF('p', 'mm', 'a4');
            const imgWidth = 210;
            const imgHeight = canvas.height * imgWidth / canvas.width;
            pdf.addImage(imgData, 'PNG', 0, 0, imgWidth, imgHeight);
            pdf.save(filename);
        });
    };


    const handleCancelTicket = () => {
        // Logic to cancel the ticket
        console.log('Cancelling ticket...');
    };

    return (
        <Box
            component={Paper}
            elevation={5}
            sx={{ backgroundColor: "white", borderRadius: 2 }}
        >
            <form onSubmit={handleSearch}>
                <Stack sx={{ m: 2 }} direction="row" spacing={2}>
                    <TextField
                        required
                        autoFocus
                        id="ticketId"
                        label="Enter Ticket ID"
                        value={ticketId}
                        onChange={handleChange}
                    />
    
                    <Button variant="contained" type="submit">
                        Search
                    </Button>
                </Stack>
            </form>

            {isLoading && <CircularProgress sx={{ mt: 2 }} />}

            {error && (
                <Typography variant="body2" color="error" sx={{ mt: 2 }}>
                    Error: {error}
                </Typography>
            )}

            {ticketDetails && (
                <Box component={Paper} elevation={5} sx={{ mt: 2, p: 2 }}>
                    <Typography variant="h6" sx={{ mb: 2 }}>
                        Ticket Details
                    </Typography>
                    <Typography variant="body1" sx={{ mb: 1 }}>
                        Ticket ID: {ticketDetails.ticketId}
                    </Typography>
        
                    <Button onClick={handlePrintTicket} variant="contained" sx={{ mr: 1 }}>
                        Print Ticket
                    </Button>
                    <Button onClick={handleCancelTicket} variant="contained" color="error">
                        Cancel Ticket
                    </Button>
                </Box>
            )}
        </Box>
    );
};

export default SearchTicket;
