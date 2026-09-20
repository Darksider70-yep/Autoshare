import React from 'react';
import { MapPin, Navigation, Clock, Search, Sparkles } from 'lucide-react';

export default function HeroSearch({
  searchFrom,
  setSearchFrom,
  searchTo,
  setSearchTo,
  searchTime,
  setSearchTime,
  onSearch
}) {
  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch();
  };

  return (
    <section className="hero">
      <div className="hero-pill">
        <Sparkles size={14} />
        Campus TukTuk Pool & Ride Share
      </div>
      <h1>
        Share <span>TukTuks</span>. Split Fares. Meet Classmates.
      </h1>
      <p>
        Save money on daily commuting. Connect with students heading to the same hostels, PGs, or apartments after class and share the auto charge.
      </p>

      {/* Search Container */}
      <form className="search-container" onSubmit={handleSubmit}>
        <div className="search-grid">
          <div className="search-field">
            <label htmlFor="search-from">From</label>
            <div className="input-wrapper">
              <MapPin size={18} className="input-icon" />
              <select 
                id="search-from"
                value={searchFrom}
                onChange={(e) => setSearchFrom(e.target.value)}
              >
                <option value="">All Pickup Points</option>
                <option value="Campus Gate 1">Campus Gate 1</option>
                <option value="Campus Gate 2">Campus Gate 2</option>
                <option value="Library Block">Library Block</option>
                <option value="Academic Block C">Academic Block C</option>
              </select>
            </div>
          </div>

          <div className="search-field">
            <label htmlFor="search-to">To (Destination)</label>
            <div className="input-wrapper">
              <Navigation size={18} className="input-icon" />
              <input 
                type="text" 
                id="search-to"
                placeholder="Search Hostel, PG, Flat..."
                value={searchTo}
                onChange={(e) => setSearchTo(e.target.value)}
              />
            </div>
          </div>

          <div className="search-field">
            <label htmlFor="search-time">Departure Time</label>
            <div className="input-wrapper">
              <Clock size={18} className="input-icon" />
              <select 
                id="search-time"
                value={searchTime}
                onChange={(e) => setSearchTime(e.target.value)}
              >
                <option value="any">Any Time</option>
                <option value="now">Leaving Next 30 Mins</option>
                <option value="1hr">Leaving Next 1 Hour</option>
                <option value="evening">After 5:00 PM</option>
              </select>
            </div>
          </div>

          <button 
            type="submit" 
            className="btn btn-primary" 
            id="search-btn"
            style={{ height: '48px', borderRadius: '12px' }}
          >
            <Search size={18} />
            Search Rides
          </button>
        </div>
      </form>
    </section>
  );
}
