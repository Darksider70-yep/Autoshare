import React, { useState, useEffect } from 'react';
import { Send, X } from 'lucide-react';

export default function PostRideModal({ isOpen, onClose, onSubmitRide }) {
  const [name, setName] = useState('');
  const [fromLocation, setFromLocation] = useState('Campus Gate 1');
  const [toLocation, setToLocation] = useState('');
  const [time, setTime] = useState('');
  const [seats, setSeats] = useState(1);
  const [fareTotal, setFareTotal] = useState(120);

  // Close on Escape key press
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  // Split fare calculation: total split among host (1) + co-travelers (seats)
  const splitCost = (fareTotal / (seats + 1)).toFixed(2);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!name.trim() || !toLocation.trim() || !time) {
      return;
    }

    onSubmitRide({
      creatorName: name.trim(),
      creatorBranch: 'Student Guest',
      from: fromLocation,
      to: toLocation.trim(),
      time,
      seatsTotal: seats,
      seatsAvailable: seats,
      fareTotal: Number(fareTotal),
      coTravelers: []
    });

    // Reset form fields
    setName('');
    setToLocation('');
    setTime('');
    setSeats(1);
    setFareTotal(120);
  };

  return (
    <div 
      className={`modal-overlay ${isOpen ? 'active' : ''}`}
      onClick={(e) => {
        if (e.target === e.currentTarget) onClose();
      }}
    >
      <div className="modal-content">
        <div className="modal-header">
          <h3>Create a Ride Share</h3>
          <button className="modal-close" onClick={onClose} aria-label="Close dialog">
            <X size={18} />
          </button>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="ride-name">Your Name</label>
            <input 
              type="text" 
              id="ride-name" 
              required 
              placeholder="e.g., Daksh Gehlot"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>

          <div className="form-group">
            <label htmlFor="ride-from">Pickup Location</label>
            <select 
              id="ride-from" 
              required
              value={fromLocation}
              onChange={(e) => setFromLocation(e.target.value)}
            >
              <option value="Campus Gate 1">Campus Gate 1</option>
              <option value="Campus Gate 2">Campus Gate 2</option>
              <option value="Library Block">Library Block</option>
              <option value="Academic Block C">Academic Block C</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="ride-to">Destination (Hostel/PG/Flats)</label>
            <input 
              type="text" 
              id="ride-to" 
              required 
              placeholder="e.g., Starlight Hostels or Sector 15 Flats"
              value={toLocation}
              onChange={(e) => setToLocation(e.target.value)}
            />
          </div>

          <div className="form-group">
            <label htmlFor="ride-time">Departure Time</label>
            <input 
              type="time" 
              id="ride-time" 
              required
              value={time}
              onChange={(e) => setTime(e.target.value)}
            />
          </div>

          <div className="form-group">
            <label>Available Seats (Max in TukTuk is 3-4)</label>
            <div className="seats-selector">
              {[1, 2, 3].map((num) => (
                <button
                  type="button"
                  key={num}
                  className={`seat-btn ${seats === num ? 'active' : ''}`}
                  onClick={() => setSeats(num)}
                >
                  {num} Seat{num > 1 ? 's' : ''}
                </button>
              ))}
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="ride-fare">Estimated Total Fare (₹)</label>
            <input 
              type="number" 
              id="ride-fare" 
              min="30" 
              max="400" 
              step="10" 
              required
              value={fareTotal}
              onChange={(e) => setFareTotal(Number(e.target.value))}
            />
            <small style={{ color: 'var(--text-muted)', display: 'block', marginTop: '4px', fontSize: '0.8rem' }}>
              Standard auto charges to most hostels range between ₹80 - ₹160.
            </small>
          </div>

          <div className="cost-split-card">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span style={{ fontWeight: 600, fontSize: '0.9rem' }}>Estimated Cost Per Student:</span>
              <span style={{ color: 'var(--accent-gold)', fontWeight: 800, fontSize: '1.25rem' }}>
                ₹{splitCost}
              </span>
            </div>
            <small style={{ color: 'var(--text-muted)', display: 'block', marginTop: '4px', fontSize: '0.78rem' }}>
              Divided equally among the rider and co-travelers.
            </small>
          </div>

          <button 
            type="submit" 
            className="btn btn-primary" 
            style={{ width: '100%', padding: '0.9rem', marginTop: '0.5rem' }}
          >
            <Send size={18} />
            Post Ride Share
          </button>
        </form>
      </div>
    </div>
  );
}
