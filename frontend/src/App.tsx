import { Container, CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import { SymptomForm } from './components/SymptomForm';
import { DiagnosisDisplay } from './components/DiagnosisDisplay';
import { useState } from 'react';

const theme = createTheme();

function App() {
  const [ipfsLink, setIpfsLink] = useState<string>();

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container>
        <SymptomForm />
        <DiagnosisDisplay ipfsLink={ipfsLink} />
      </Container>
    </ThemeProvider>
  );
}

export default App;