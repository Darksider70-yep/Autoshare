import React from 'react';
import { ArrowRight, Clock, UserPlus, MessageSquare, CheckCircle } from 'lucide-react';

export default function RideCard({ ride, onJoinRide, onOpenChat }) {
  const isFull = ride.seatsAvailable === 0;
  const isJoined = ride.coTravelers.includes("You");
  
  // Calculate dynamic per-person split cost
  const totalRiders = (ride.seatsTotal + 1) - ride.seatsAvailable;
  const splitFare = totalRiders > 0 ? (ride.fareTotal / totalRiders).toFixed(0) : (ride.fareTotal / (ride.seatsTotal + 1)).toFixed(0);

  // Status tag styling
  const statusClass = isFull ? 'status-full' : 'status-active';
  const statusText = isFull ? 'Full' : `${ride.seatsAvailable} seat${ride.seatsAvailable > 1 ? 's' : ''} left`;

  // Initials generator
  const getInitials = (name) => {
    return name
      .split(' ')
      .map(n => n[0])
      .join('')
      .toUpperCase();
  };

  return (
    <div className="ride-card">
      <div className="ride-card-header">
        <div className="student-info">
          <div className="student-avatar">{getInitials(ride.creatorName)}</div>
          <div className="student-details">
            <h4>{ride.creatorName}</h4>
            <span>{ride.creatorBranch}</span>
          </div>
        </div>
        <span className={`ride-status-badge ${statusClass}`}>
          {statusText}
        </span>
      </div>

      <div className="route-info">
        <div className="route-point">
          <span className="label">Pickup</span>
          <span className="loc">{ride.from}</span>
        </div>
        <div className="route-arrow">
          <ArrowRight size={16} />
        </div>
        <div className="route-point">
          <span className="label">Destination</span>
          <span className="loc">{ride.to}</span>
        </div>
      </div>

      <div className="ride-meta-grid">
        <div className="meta-item">
          <span className="label">Departure</span>
          <span className="value">
            <Clock size={14} style={{ color: 'var(--accent-gold)' }} />
            {ride.time}
          </span>
        </div>

        <div className="meta-item">
          <span className="label">Splitting Cost</span>
          <span className="value" style={{ color: 'var(--accent-gold)' }}>
            ₹{splitFare}{' '}
            <span style={{ fontSize: '0.7rem', fontWeight: 'normal', color: 'var(--text-muted)' }}>
              / student
            </span>
          </span>
        </div>

        <div className="meta-item">
          <span className="label">Auto Capacity</span>
          <div className="seats-indicator">
            {Array.from({ length: ride.seatsTotal }).map((_, index) => {
              const isTaken = index >= ride.seatsAvailable;
              return (
                <div 
                  key={index} 
                  className={`seat-dot ${isTaken ? 'taken' : ''}`} 
                  title={isTaken ? 'Seat Occupied' : 'Seat Available'}
                />
              );
            })}
          </div>
        </div>
      </div>

      <div className="ride-card-footer">
        <div className="co-travelers-mini">
          {ride.coTravelers.map((name, index) => (
            <div 
              key={index} 
              className="co-traveler-avatar-mini" 
              title={name}
            >
              {name === 'You' ? 'ME' : getInitials(name)}
            </div>
          ))}
          {ride.coTravelers.length > 0 ? (
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginLeft: '0.5rem' }}>
              +{ride.coTravelers.length} joined
            </span>
          ) : (
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
              No co-travelers yet
            </span>
          )}
        </div>

        <div className="card-actions">
          {isJoined ? (
            <button 
              className="btn btn-secondary btn-sm" 
              disabled
              style={{ color: 'var(--color-success)' }}
            >
              <CheckCircle size={14} />
              Joined
            </button>
          ) : isFull ? (
            <button className="btn btn-secondary btn-sm" disabled>
              Group Full
            </button>
          ) : (
            <button 
              className="btn btn-outline-gold btn-sm" 
              onClick={() => onJoinRide(ride.id)}
            >
              <UserPlus size={14} />
              Join Ride
            </button>
          )}

          <button 
            className="btn btn-secondary btn-sm" 
            onClick={() => onOpenChat(ride.id)}
          >
            <MessageSquare size={14} />
            Chat
          </button>
        </div>
      </div>
    </div>
  );
}
