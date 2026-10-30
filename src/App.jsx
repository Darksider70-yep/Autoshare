import React, { useState, useMemo, useEffect } from 'react';
import Navbar from './components/Navbar';
import HeroSearch from './components/HeroSearch';
import RidesFeed from './components/RidesFeed';
import SidebarStats from './components/SidebarStats';
import HotspotClusters from './components/HotspotClusters';
import PostRideModal from './components/PostRideModal';
import ChatDrawer from './components/ChatDrawer';
import Toast from './components/Toast';
import Footer from './components/Footer';
import UserRecordsView from './components/UserRecordsView';
import MicroservicesConsole from './components/MicroservicesConsole';
import { initialRidesData, initialChatMessages } from './data/mockRides';

export default function App() {
  // Active Navigation Tab: 'rides' | 'users' | 'microservices'
  const [activeTab, setActiveTab] = useState('rides');

  // Main State
  const [rides, setRides] = useState(initialRidesData);
  const [chatMessages, setChatMessages] = useState(initialChatMessages);

  // Load from Spring Boot backend if running
  useEffect(() => {
    fetch('/api/rides')
      .then(res => res.json())
      .then(data => {
        if (Array.isArray(data) && data.length > 0) {
          const mappedRides = data.map(r => ({
            id: r.id,
            creatorName: r.hostName,
            creatorBranch: 'SRM Campus Student',
            from: r.pickupGate,
            to: r.destination,
            time: r.departureTime ? r.departureTime.substring(11, 16) : '17:00',
            seatsTotal: r.totalSeats,
            seatsAvailable: r.seatsAvailable,
            fareTotal: r.totalFare,
            coTravelers: r.bookings ? r.bookings.map(b => b.studentName) : []
          }));
          setRides(mappedRides);
        }
      })
      .catch(err => {
        console.warn('Backend not reached, using local fallback:', err);
      });
  }, []);
  
  // Search & Filter State
  const [searchFrom, setSearchFrom] = useState('');
  const [searchTo, setSearchTo] = useState('');
  const [searchTime, setSearchTime] = useState('any');
  const [appliedFilters, setAppliedFilters] = useState({ from: '', to: '', time: 'any' });

  // Modal & Drawer State
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isChatOpen, setIsChatOpen] = useState(false);
  const [activeChatRideId, setActiveChatRideId] = useState(1);
  const [activeGroupsCount, setActiveGroupsCount] = useState(14);

  // Toast Notification State
  const [toast, setToast] = useState({ show: false, message: '', type: 'success' });

  const triggerToast = (message, type = 'success') => {
    setToast({ show: true, message, type });
    setTimeout(() => {
      setToast({ show: false, message: '', type: 'success' });
    }, 3200);
  };

  // Filtered rides calculation
  const filteredRides = useMemo(() => {
    return rides.filter((ride) => {
      const matchFrom = !appliedFilters.from || ride.from.toLowerCase().includes(appliedFilters.from.toLowerCase());
      const matchTo = !appliedFilters.to || ride.to.toLowerCase().includes(appliedFilters.to.toLowerCase().trim());
      
      let matchTime = true;
      if (appliedFilters.time === 'now') {
        matchTime = ride.time >= '16:00' && ride.time <= '18:00';
      } else if (appliedFilters.time === '1hr') {
        matchTime = ride.time >= '16:30' && ride.time <= '18:30';
      } else if (appliedFilters.time === 'evening') {
        matchTime = ride.time >= '17:00';
      }

      return matchFrom && matchTo && matchTime;
    });
  }, [rides, appliedFilters]);

  const isFiltered = Boolean(appliedFilters.from || appliedFilters.to || appliedFilters.time !== 'any');

  // Search actions
  const handleSearch = () => {
    setAppliedFilters({
      from: searchFrom,
      to: searchTo,
      time: searchTime
    });
  };

  const handleResetFilters = () => {
    setSearchFrom('');
    setSearchTo('');
    setSearchTime('any');
    setAppliedFilters({ from: '', to: '', time: 'any' });
  };

  const handleSelectHotspot = (destName) => {
    setSearchTo(destName);
    setAppliedFilters(prev => ({ ...prev, to: destName }));
  };

  // Join Ride Action with Spring Boot / fallback
  const handleJoinRide = (rideId) => {
    const studentName = 'Daksh Gehlot';
    const studentEmail = 'daksh.g@srmist.edu.in';

    fetch(`/api/rides/${rideId}/book`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ studentName, studentEmail })
    })
      .then(res => {
        if (!res.ok) {
          return res.json().then(errData => { throw errData; });
        }
        return res.json();
      })
      .then(updatedRide => {
        setRides(prev => prev.map(r => {
          if (r.id === rideId) {
            return {
              ...r,
              seatsAvailable: updatedRide.seatsAvailable,
              coTravelers: updatedRide.bookings ? updatedRide.bookings.map(b => b.studentName) : [...r.coTravelers, studentName]
            };
          }
          return r;
        }));
        triggerToast(`Seat confirmed via Spring Boot backend! Fare split updated.`);
      })
      .catch(err => {
        // Fallback local update
        setRides(prevRides => 
          prevRides.map(r => {
            if (r.id === rideId && r.seatsAvailable > 0) {
              const newAvailable = r.seatsAvailable - 1;
              const newCoTravelers = r.coTravelers.includes(studentName) 
                ? r.coTravelers 
                : [...r.coTravelers, studentName];
              return {
                ...r,
                seatsAvailable: newAvailable,
                coTravelers: newCoTravelers
              };
            }
            return r;
          })
        );
        triggerToast(err?.message || `Seat claimed! Split updated.`);
      });
  };

  // Post Ride Action
  const handlePostRide = (newRide) => {
    setRides(prev => [newRide, ...prev]);
    setActiveGroupsCount(prev => prev + 1);
    triggerToast('Ride published successfully across campus network!');
  };

  // Chat Actions
  const handleOpenChat = (rideId) => {
    setActiveChatRideId(rideId);
    setIsChatOpen(true);
  };

  const handleOpenDefaultChat = () => {
    setIsChatOpen(true);
  };

  const handleSendMessage = (text) => {
    if (!text.trim()) return;

    const getCurrentTimeStr = () => {
      const now = new Date();
      return `${now.getHours() % 12 || 12}:${now.getMinutes().toString().padStart(2, '0')} ${now.getHours() >= 12 ? 'PM' : 'AM'}`;
    };

    const newMsg = {
      sender: 'You',
      text: text.trim(),
      time: getCurrentTimeStr()
    };

    setChatMessages(prev => ({
      ...prev,
      [activeChatRideId]: [...(prev[activeChatRideId] || []), newMsg]
    }));

    // Simulated Auto-Reply from Ride Host
    const currentRide = rides.find(r => r.id === activeChatRideId);
    if (currentRide) {
      setTimeout(() => {
        const replies = [
          `Hey! Sounds great. Meet me at ${currentRide.from} near the main gate steps.`,
          `Yes, auto fare will be exactly ₹${Math.round(currentRide.fareTotal / ((currentRide.seatsTotal - currentRide.seatsAvailable) + 2))} each!`,
          `Got it! I am wearing a black hoodie. Let me know when you arrive.`
        ];
        const randomReply = replies[Math.floor(Math.random() * replies.length)];

        setChatMessages(prev => ({
          ...prev,
          [activeChatRideId]: [
            ...(prev[activeChatRideId] || []),
            { sender: currentRide.creatorName, text: randomReply, time: getCurrentTimeStr() }
          ]
        }));
      }, 1200);
    }
  };

  const activeRideObj = rides.find(r => r.id === activeChatRideId) || rides[0];

  return (
    <div className="app-container">
      {/* Top Navigation Bar with Tabs */}
      <Navbar 
        activeTab={activeTab} 
        onTabChange={setActiveTab} 
        onOpenPostModal={() => setIsModalOpen(true)} 
      />

      {/* Main View Router */}
      <main className="main-content-layout">
        {activeTab === 'rides' && (
          <>
            <HeroSearch 
              searchFrom={searchFrom}
              setSearchFrom={setSearchFrom}
              searchTo={searchTo}
              setSearchTo={setSearchTo}
              searchTime={searchTime}
              setSearchTime={setSearchTime}
              onSearch={handleSearch}
            />

            <section className="dashboard" id="active-rides">
              <RidesFeed 
                rides={filteredRides}
                totalCount={filteredRides.length}
                isFiltered={isFiltered}
                onResetFilters={handleResetFilters}
                onJoinRide={handleJoinRide}
                onOpenChat={handleOpenChat}
              />

              <aside className="sidebar-panel">
                <SidebarStats activeGroupsCount={activeGroupsCount} />
                <HotspotClusters onSelectDestination={handleSelectHotspot} />
              </aside>
            </section>
          </>
        )}

        {activeTab === 'users' && (
          <UserRecordsView onTriggerToast={triggerToast} />
        )}

        {activeTab === 'microservices' && (
          <MicroservicesConsole onTriggerToast={triggerToast} />
        )}
      </main>

      {/* Footer */}
      <Footer />

      {/* Post Ride Dialog Modal */}
      <PostRideModal 
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSubmitRide={handlePostRide}
      />

      {/* Real-time Ride Coordination Chat */}
      <ChatDrawer 
        isOpen={isChatOpen}
        activeRide={activeRideObj}
        messages={chatMessages[activeChatRideId] || []}
        onClose={() => setIsChatOpen(false)}
        onOpenDefault={handleOpenDefaultChat}
        onSendMessage={handleSendMessage}
      />

      {/* Toast Notification */}
      <Toast toast={toast} />
    </div>
  );
}
