import React from 'react';
import { PlusCircle, Users, Network, Car, Sparkles } from 'lucide-react';

export default function Navbar({ activeTab, onTabChange, onOpenPostModal }) {
  return (
    <header className="site-header">
      <div className="header-brand-group">
        <a href="#" className="logo" onClick={(e) => { e.preventDefault(); onTabChange('rides'); }}>
          <div className="logo-icon">🛺</div>
          <span>Auto</span>share
        </a>
        <div className="student-header-chip" title="Lead Student Developer - Unit 5 Submission">
          <span className="dot online"></span>
          <span className="author-name">Daksh Gehlot</span>
          <span className="reg-pill">RA2411003012297</span>
        </div>
      </div>

      <nav className="header-navigation">
        <div className="nav-tab-pills">
          <button 
            className={`tab-pill-btn ${activeTab === 'rides' ? 'active' : ''}`}
            onClick={() => onTabChange('rides')}
            id="tab-btn-rides"
          >
            <Car size={16} />
            <span>Campus Rides</span>
          </button>

          <button 
            className={`tab-pill-btn ${activeTab === 'users' ? 'active' : ''}`}
            onClick={() => onTabChange('users')}
            id="tab-btn-users"
          >
            <Users size={16} />
            <span>User Records (JPA CRUD)</span>
            <span className="unit-tag">Unit 5</span>
          </button>

          <button 
            className={`tab-pill-btn ${activeTab === 'microservices' ? 'active' : ''}`}
            onClick={() => onTabChange('microservices')}
            id="tab-btn-microservices"
          >
            <Network size={16} />
            <span>Microservices Console</span>
            <span className="unit-tag">Unit 5</span>
          </button>
        </div>

        {activeTab === 'rides' && (
          <button 
            className="btn btn-primary post-ride-btn" 
            id="open-post-ride-btn"
            onClick={onOpenPostModal}
          >
            <PlusCircle size={17} />
            <span>Post a Ride</span>
          </button>
        )}
      </nav>
    </header>
  );
}
