import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true,
    proxy: {
      // Microservice 1: User Management Service (Port 8081)
      '/api/users': {
        target: 'http://localhost:8081',
        changeOrigin: true
      },
      // Microservice 2: Ride-Booking Service & Topology Gateway (Port 8080)
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true
      }
    }
  }
});
