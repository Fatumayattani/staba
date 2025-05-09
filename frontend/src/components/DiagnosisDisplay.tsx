import { useEffect, useState } from 'react';
import { Box, Typography, CircularProgress, Alert } from '@mui/material';
import { getDiagnosis } from '../api';
import { Diagnosis } from '../types';

interface DiagnosisDisplayProps {
  ipfsLink?: string;
}

export const DiagnosisDisplay = ({ ipfsLink }: DiagnosisDisplayProps) => {
  const [diagnosis, setDiagnosis] = useState<Diagnosis | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (ipfsLink) {
      const fetchDiagnosis = async () => {
        setLoading(true);
        try {
          const data = await getDiagnosis(ipfsLink);
          setDiagnosis(data);
        } catch (err) {
          setError('Failed to fetch diagnosis. Please try again later.');
        } finally {
          setLoading(false);
        }
      };

      fetchDiagnosis();
    }
  }, [ipfsLink]);

  if (!ipfsLink) {
    return null;
  }

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" p={3}>
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Alert severity="error" sx={{ mt: 2 }}>
        {error}
      </Alert>
    );
  }

  return (
    <Box sx={{ mt: 4, p: 3, bgcolor: 'background.paper', borderRadius: 1 }}>
      <Typography variant="h6" gutterBottom>
        Diagnosis Results
      </Typography>
      {diagnosis && (
        <Typography>
          {diagnosis.diagnosis}
        </Typography>
      )}
    </Box>
  );
};