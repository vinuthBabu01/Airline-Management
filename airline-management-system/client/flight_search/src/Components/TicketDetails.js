import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
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
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
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
    const location = useLocation()
    const [ticketId, setTicketId] = useState('');
    const [ticketDetails, setTicketDetails] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [errormsg, setError] = useState(null);
    const [ticketID, setTicketID] = useState(null);
    const [open, setOpen] = React.useState(false);
    const [openwindow, setresponseReceived] = React.useState(false);

    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setOpen(false);
    };

    const handleSearch = (event) => {
        event.preventDefault();
        setIsLoading(true);
        setError(null);

        // Assuming the API endpoint for fetching ticket details is '/tickets/:ticketId'
        axios.post(`http://localhost:5000/tickets/ticketId`, {
            ticket_id: ticketId})
            .then(response => {
                setIsLoading(false);
                setresponseReceived(true)
                setTicketDetails(response.data.ticket_info);
                setTicketID(response.data.ticket_info)
    
            })
            .catch(error => {
                setIsLoading(false);
                setError(error.response.data.message);
            });
    };

    const handleChange = (event) => {
        const value = event.target.value;
        setTicketId(value);
    };    

    const handlePrintTicket = () => {
        const filename = 'ticket.pdf';
        const element = document.getElementById('ticket-details');
        try{
            html2canvas(element).then((canvas) => {
                const imgData = canvas.toDataURL('image/png');
                const pdf = new jsPDF('p', 'mm', 'a4');
                const imgWidth = 210;
                const imgHeight = canvas.height * imgWidth / canvas.width;
                pdf.addImage(imgData, 'PNG', 0, 0, imgWidth, imgHeight);
                pdf.save(filename);
            });
        }
        catch(error){
            console.log(error)
        }
        
        
    };


    const handleCancelTicket = (event) => {
        // Logic to cancel the ticket
        event.preventDefault();
        setIsLoading(true);
        setError(null);

        // Assuming the API endpoint for fetching ticket details is '/tickets/:ticketId'
        axios.post(`http://localhost:5000/ticket/cancel`, {
            ticket_id: ticketId})
            .then(response => {
                
                setTicketDetails(response.data.ticket_info);
                setIsLoading(false);
                setOpen(true); // Open the dialog window
                setresponseReceived(false);
            })
            .catch(error => {
                setIsLoading(false);
                setError(error.response.data.message);
            });
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

            {errormsg && (
                <Typography variant="body2" color="error" sx={{ mt: 2 }}>
                    Error: {errormsg}
                </Typography>
            )}

            {openwindow && ticketDetails && (
                <Box component={Paper} elevation={5} sx={{ mt: 2, p: 2 }}>
                    <Typography variant="h6" sx={{ mb: 2 }}>
                        Ticket Details
                    </Typography>
                    {ticketDetails&& <Typography variant="body1" sx={{ mb: 1 }}>
                        Ticket ID: {ticketDetails.ticket_id[0]||''}
                    </Typography>}
                    {ticketDetails&& <Typography variant="body1" sx={{ mb: 1 }}>
                        Name: {ticketDetails.passenger_name[0]||''}
                    </Typography>}
                    {ticketDetails&& <Typography variant="body1" sx={{ mb: 1 }}>
                        Origin: {ticketDetails.origin[0]||''}
                    </Typography>}
                    {ticketDetails&& <Typography variant="body1" sx={{ mb: 1 }}>
                        Destination: {ticketDetails.destination[0]||''}
                    </Typography>}
                    {ticketDetails&& <Typography variant="body1" sx={{ mb: 1 }}>
                        Travel Date: {ticketDetails.departure_date||''}
                    </Typography>}
                    {ticketDetails&& <Typography variant="body1" sx={{ mb: 1 }}>
                        Email: {ticketDetails.email[0]||''}
                    </Typography>}
                    {ticketDetails&& <Typography variant="body1" sx={{ mb: 1 }}>
                        Phone Number: {ticketDetails.phoneNo[0]||''}
                    </Typography>}
                    <Button onClick={handlePrintTicket} variant="contained" sx={{ mr: 1 }}>
                        Print Ticket
                    </Button>
                    <Button onClick={handleCancelTicket} variant="contained" color="error">
                        Cancel Ticket
                    </Button>
                </Box>
            )}
            <Dialog
                        open={open}
                        onClose={handleClose}
                        maxWidth
                        aria-labelledby="alert-dialog-title"
                        aria-describedby="alert-dialog-description"
                    >
                        <DialogTitle align='center' id="alert-dialog-title" color='red' variant='h5' gutterBottom>
                            {"Booking Cancelled!"}
                        </DialogTitle>
                        <DialogContent>
                            <DialogContentText id="alert-dialog-description" color='black'>
                                 Your Ticket is Cancelled Successfully 
                            </DialogContentText>
                            <DialogContentText id="alert-dialog-description">
                                Thank you for using SkyPlanner!
                            </DialogContentText>
                        </DialogContent>
                        <DialogActions>
                            <Button onClick={handleClose} autoFocus>
                                Close
                            </Button>
                        </DialogActions>
                    </Dialog>
        </Box>
    );
};

export default SearchTicket;
