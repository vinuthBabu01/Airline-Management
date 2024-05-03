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
                Keeping it simple
                </Typography>
                <Typography align="left" variant="body1" gutterBottom>
              

We come together each day to fulfill a promise of offering the single most comprehensive travel experience to users, through the best Desktop solutions, we keep customers at the center of everything we do.
                </Typography>
            </Stack>
        </Box>
    )
}