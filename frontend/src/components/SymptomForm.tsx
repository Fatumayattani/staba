import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { TextField, Button, Box, Typography, Alert } from '@mui/material';
import { submitSymptoms } from '../api';
import type { Symptoms } from '../types';

export const SymptomForm = () => {
  const { register, handleSubmit, formState: { errors } } = useForm<Symptoms>();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const onSubmit = async (data: Symptoms) => {
    setLoading(true);
    setError(null);
    try {
      await submitSymptoms(data);
      setSuccess(true);
    } catch (err) {
      setError('Failed to submit symptoms. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit(onSubmit)} sx={{ maxWidth: 600, mx: 'auto', p: 3 }}>
      <Typography variant="h5" gutterBottom>
        Enter Your Symptoms
      </Typography>
      
      <TextField
        fullWidth
        multiline
        rows={4}
        label="Symptoms"
        {...register('symptoms', { required: 'Please enter your symptoms' })}
        error={!!errors.symptoms}
        helperText={errors.symptoms?.message}
        sx={{ mb: 2 }}
      />

      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      {success && (
        <Alert severity="success" sx={{ mb: 2 }}>
          Symptoms submitted successfully!
        </Alert>
      )}

      <Button 
        type="submit" 
        variant="contained" 
        disabled={loading}
        fullWidth
      >
        {loading ? 'Submitting...' : 'Submit Symptoms'}
      </Button>
    </Box>
  );
};