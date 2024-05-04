import React from "react";
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { Stack } from "@mui/system";

export default function About() {
    return (
        <Box sx={{ backgroundColor: 'white', borderRadius: 2, width: '100%', maxWidth: 600 }}>
            <Stack sx={{ m: 2 }}>
                <Typography color='darkblue' align="left" variant="h2" gutterBottom>
                    About us
                </Typography>
                <Typography align="left" variant="body1" gutterBottom>
            
                </Typography>
                <Typography align="left" variant="body1" gutterBottom>
                From SkyPlanner, your one-stop shop for easy trip bookings, greetings! At SkyPlanner, we understand that traveling is just as significant as reaching a destination. Because we are passionate about providing perfect travel experiences, we have created a platform that puts you, the traveler, first in all we do.

Giving you the assurance and comfort to explore the globe is our aim. Whether you're taking an unexpected weekend journey or organizing a dream vacation, SkyQuest can help you create an amazing trip experience. Our dedicated customer care, extensive selection of flights from top airlines, and easy booking tools are just a few of the ways we strive to provide you with the convenience and peace of mind you deserve.

                </Typography>
            </Stack>
        </Box>
    )
}