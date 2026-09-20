import React from 'react';
import { MapPin } from 'lucide-react';
import { popularHotspots } from '../data/mockRides';

export default function HotspotClusters({ onSelectDestination }) {
  return (
    <div className="hotspot-card">
      <h3>
        <MapPin size={18} style={{ color: 'var(--accent-gold)' }} />
        Popular Destination Clusters
      </h3>
      <div className="hotspot-list">
        {popularHotspots.map((spot, index) => (
          <div 
            key={index} 
            className="hotspot-item"
            onClick={() => onSelectDestination(spot.destination)}
          >
            <div className="hotspot-details">
              <h5>{spot.destination}</h5>
              <span>{spot.subtitle}</span>
            </div>
            <span className="hotspot-badge">{spot.activeCount} active</span>
          </div>
        ))}
      </div>
    </div>
  );
}
