import React from 'react';
import { Activity } from 'lucide-react';

export default function SidebarStats({ activeGroupsCount }) {
  return (
    <div className="stats-card">
      <h3>
        <Activity size={18} style={{ color: 'var(--accent-gold)' }} />
        Autoshare Live Info
      </h3>
      <div className="stat-row">
        <span className="stat-label">Active Groups Today</span>
        <span className="stat-val" id="stat-active-groups">{activeGroupsCount}</span>
      </div>
      <div className="stat-row">
        <span className="stat-label">Avg. Savings Per Student</span>
        <span className="stat-val">₹45 - ₹60</span>
      </div>
      <div className="stat-row">
        <span className="stat-label">Popular Pickup Point</span>
        <span className="stat-val">Campus Gate 2</span>
      </div>
    </div>
  );
}
