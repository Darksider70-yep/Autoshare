import React, { useState, useMemo } from 'react';
import Navbar from './components/Navbar';
import HeroSearch from './components/HeroSearch';
import RidesFeed from './components/RidesFeed';
import SidebarStats from './components/SidebarStats';
import HotspotClusters from './components/HotspotClusters';
import PostRideModal from './components/PostRideModal';
import ChatDrawer from './components/ChatDrawer';
import Toast from './components/Toast';
import Footer from './components/Footer';
import { initialRidesData, initialChatMessages } from './data/mockRides';

export default function App() {
  // Main State
  const [rides, setRides] = useState(initialRidesData);
  const [chatMessages, setChatMessages] = useState(initialChatMessages);
  
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

  const handleSelectHotspot = (destination) => {
    setSearchTo(destination);
    setAppliedFilters(prev => ({ ...prev, to: destination }));
    const element = document.getElementById('active-rides');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  // Helper for current time HH:MM
  const getCurrentTimeStr = () => {
    const now = new Date();
    const hrs = String(now.getHours()).padStart(2, '0');
    const mins = String(now.getMinutes()).padStart(2, '0');
    return `${hrs}:${mins}`;
  };

  // Join Ride Action
  const handleJoinRide = (rideId) => {
    const ride = rides.find(r => r.id === rideId);
    if (!ride || ride.seatsAvailable <= 0) return;

    // Update ride state
    setRides(prev => prev.map(r => {
      if (r.id === rideId) {
        return {
          ...r,
          seatsAvailable: r.seatsAvailable - 1,
          coTravelers: [...r.coTravelers, 'You']
        };
      }
      return r;
    }));

    // Add system message to chat
    setChatMessages(prev => ({
      ...prev,
      [rideId]: [
        ...(prev[rideId] || []),
        {
          sender: 'System',
          text: 'You joined the ride. Say hi to coordinate pickup!',
          time: getCurrentTimeStr()
        }
      ]
    }));

    triggerToast(`Successfully joined ${ride.creatorName}'s ride to ${ride.to}!`);
    setActiveChatRideId(rideId);
    
    // Automatically open coordination chat after a brief moment
    setTimeout(() => {
      setIsChatOpen(true);
    }, 500);
  };

  // Create/Post new Ride Action
  const handlePostRide = (newRideData) => {
    const newId = rides.length + 1;
    const newRide = {
      id: newId,
      ...newRideData
    };

    setRides(prev => [newRide, ...prev]);
    setActiveGroupsCount(prev => prev + 1);

    // Seed chat for new ride
    setChatMessages(prev => ({
      ...prev,
      [newId]: [
        {
          sender: 'System',
          text: `Ride created by ${newRide.creatorName}. Waiting for classmates to join!`,
          time: getCurrentTimeStr()
        }
      ]
    }));

    setIsModalOpen(false);
    triggerToast('Your TukTuk ride share offer has been published!');
  };

  // Chat Actions
  const handleOpenChat = (rideId) => {
    setActiveChatRideId(rideId);
    setIsChatOpen(true);
  };

  const handleOpenDefaultChat = () => {
    if (rides.length > 0) {
      setActiveChatRideId(rides[0].id);
    }
    setIsChatOpen(true);
  };

  const handleSendMessage = (text) => {
    if (!activeChatRideId) return;

    const timeStr = getCurrentTimeStr();
    const currentRide = rides.find(r => r.id === activeChatRideId);

    setChatMessages(prev => ({
      ...prev,
      [activeChatRideId]: [
        ...(prev[activeChatRideId] || []),
        { sender: 'You', text, time: timeStr }
      ]
    }));

    // Trigger simulated creator response
    if (currentRide) {
      setTimeout(() => {
        const replies = [
          `Awesome! I am waiting near the tea stall by ${currentRide.from}. I have a blue backpack.`,
          `Perfect, let's meet in 5 minutes! I'm heading out of lecture hall now.`,
          `Hey! I'm talking to the auto driver right now at ${currentRide.from}, see you shortly!`,
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
      {/* Top Navigation */}
      <Navbar onOpenPostModal={() => setIsModalOpen(true)} />

      {/* Hero & Search Header */}
      <main>
        <HeroSearch 
          searchFrom={searchFrom}
          setSearchFrom={setSearchFrom}
          searchTo={searchTo}
          setSearchTo={setSearchTo}
          searchTime={searchTime}
          setSearchTime={setSearchTime}
          onSearch={handleSearch}
        />

        {/* Dashboard Live Feed & Sidebar */}
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
