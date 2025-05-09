import axios from 'axios';
import { Symptoms } from '../types';

const API_BASE_URL = 'http://127.0.0.1:8000';

export const submitSymptoms = async (symptoms: Symptoms) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/symptoms`, symptoms);
    return response.data;
  } catch (error) {
    console.error('Error submitting symptoms:', error);
    throw error;
  }
};

export const getDiagnosis = async (ipfsLink: string) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/diagnosis/${ipfsLink}`);
    return response.data;
  } catch (error) {
    console.error('Error getting diagnosis:', error);
    throw error;
  }
};