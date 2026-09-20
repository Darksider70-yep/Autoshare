import React from 'react';
import { PlusCircle } from 'lucide-react';

export default function Navbar({ onOpenPostModal }) {
  return (
    <header>
      <a href="#" className="logo">
        <div className="logo-icon">🛺</div>
        <span>Auto</span>share
      </a>
      <nav>
        <a href="#how-it-works">How it Works</a>
        <a href="#active-rides">Find Rides</a>
        <button 
          className="btn btn-primary" 
          id="open-post-ride-btn"
          onClick={onOpenPostModal}
        >
          <PlusCircle size={18} />
          Post a Ride
        </button>
      </nav>
    </header>
  );
}
