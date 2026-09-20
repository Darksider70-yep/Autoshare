import React from 'react';
import { CheckCircle, AlertCircle } from 'lucide-react';

export default function Toast({ toast }) {
  if (!toast) return null;

  return (
    <div className={`toast ${toast.show ? 'active' : ''}`} id="app-toast">
      {toast.type === 'error' ? (
        <AlertCircle size={18} style={{ color: 'var(--color-danger)' }} />
      ) : (
        <CheckCircle size={18} style={{ color: 'var(--color-success)' }} />
      )}
      <span id="toast-message">{toast.message}</span>
    </div>
  );
}
