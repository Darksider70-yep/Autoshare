import React from 'react';
import { Info, RefreshCw } from 'lucide-react';
import RideCard from './RideCard';

export default function RidesFeed({
  rides,
  totalCount,
  isFiltered,
  onResetFilters,
  onJoinRide,
  onOpenChat
}) {
  return (
    <div className="feed-container">
      <div className="feed-header">
        <h2 className="feed-title">
          Active Ride Offers <span className="badge" id="rides-count">{totalCount}</span>
        </h2>
        {isFiltered && (
          <button 
            className="btn btn-secondary btn-sm" 
            id="btn-reset-filters"
            onClick={onResetFilters}
          >
            <RefreshCw size={14} />
            Reset Filter
          </button>
        )}
      </div>

      <div className="rides-list" id="rides-feed">
        {rides.length === 0 ? (
          <div style={{
            textAlign: 'center',
            padding: '3rem 2rem',
            background: 'var(--bg-secondary)',
            borderRadius: 'var(--radius-md)',
            border: '1px solid var(--border-color)'
          }}>
            <Info size={48} style={{ color: 'var(--accent-gold)', marginBottom: '1rem' }} />
            <h4 style={{ fontSize: '1.15rem', marginBottom: '0.5rem' }}>No rides found</h4>
            <p style={{ color: 'var(--text-secondary)', maxWidth: '400px', margin: '0 auto 1.5rem auto', fontSize: '0.9rem' }}>
              Try checking other campus gates, searching broader destinations, or post a new ride offer yourself.
            </p>
            <button className="btn btn-primary btn-sm" onClick={onResetFilters}>
              Reset Search Filters
            </button>
          </div>
        ) : (
          rides.map((ride) => (
            <RideCard 
              key={ride.id} 
              ride={ride} 
              onJoinRide={onJoinRide}
              onOpenChat={onOpenChat}
            />
          ))
        )}
      </div>
    </div>
  );
}
