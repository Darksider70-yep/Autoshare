// Initial Mock Ride Offers Data
let ridesData = [
  {
    id: 1,
    creatorName: "Aarav Sharma",
    creatorBranch: "CSE, 3rd Yr",
    from: "Campus Gate 2",
    to: "Starlight Hostels",
    time: "17:15",
    seatsTotal: 3,
    seatsAvailable: 2,
    fareTotal: 120,
    coTravelers: ["Priya Patel"]
  },
  {
    id: 2,
    creatorName: "Ananya Iyer",
    creatorBranch: "Biotech, 1st Yr",
    from: "Campus Gate 1",
    to: "Green Meadows Flats",
    time: "17:30",
    seatsTotal: 3,
    seatsAvailable: 1,
    fareTotal: 150,
    coTravelers: ["Kabir Sen", "Riya Das"]
  },
  {
    id: 3,
    creatorName: "Vikram Malhotra",
    creatorBranch: "ECE, 4th Yr",
    from: "Library Block",
    to: "R.K. Puram PG Zone",
    time: "16:45",
    seatsTotal: 3,
    seatsAvailable: 3,
    fareTotal: 90,
    coTravelers: []
  },
  {
    id: 4,
    creatorName: "Ishaan Verma",
    creatorBranch: "Mechanical, 2nd Yr",
    from: "Campus Gate 2",
    to: "Starlight Hostels",
    time: "18:00",
    seatsTotal: 3,
    seatsAvailable: 0,
    fareTotal: 120,
    coTravelers: ["Nikhil Jha", "Amit Shah", "Rahul K."]
  }
];

// Active Chat History Simulation State
let activeChatRideId = null;
const simulatedMessagesByRide = {
  1: [
    { sender: "Aarav Sharma", text: "Hey! Leaving in 10 minutes. I'm near the Gate 2 Nescafe stall.", time: "17:05" },
    { sender: "Priya Patel", text: "Awesome, coming there in 2 mins. Red backpack.", time: "17:06" }
  ],
  2: [
    { sender: "Ananya Iyer", text: "Auto is booked. Waiting near Gate 1 security room.", time: "17:20" },
    { sender: "Kabir Sen", text: "Coming! I have class in Block A.", time: "17:21" },
    { sender: "Riya Das", text: "Just got my bags, heading down now.", time: "17:22" }
  ],
  3: [
    { sender: "Vikram Malhotra", text: "Created the ride. Auto will cost ₹90 total. Anyone going towards RK Puram?", time: "16:35" }
  ],
  4: [
    { sender: "Ishaan Verma", text: "We are full. Let's find an auto guys.", time: "17:50" },
    { sender: "Nikhil Jha", text: "I see one auto driver. He's asking ₹120. Standard rate.", time: "17:51" }
  ]
};

// UI Elements
const ridesFeed = document.getElementById("rides-feed");
const ridesCountBadge = document.getElementById("rides-count");
const resetFiltersBtn = document.getElementById("btn-reset-filters");

// Search Inputs
const searchFromInput = document.getElementById("search-from");
const searchToInput = document.getElementById("search-to");
const searchTimeInput = document.getElementById("search-time");
const searchBtn = document.getElementById("search-btn");

// Modals
const postRideModal = document.getElementById("post-ride-modal");
const openPostRideBtn = document.getElementById("open-post-ride-btn");
const closePostRideBtn = document.getElementById("close-post-ride-btn");
const postRideForm = document.getElementById("post-ride-form");

// Modal Seats Selector
const seatBtns = document.querySelectorAll(".seat-btn");
const rideSeatsHidden = document.getElementById("ride-seats");
const rideFareInput = document.getElementById("ride-fare");
const farePerPersonText = document.getElementById("fare-per-person");

// Chat Drawer Elements
const chatTriggerBtn = document.getElementById("chat-trigger-btn");
const chatDrawer = document.getElementById("chat-drawer");
const closeChatBtn = document.getElementById("close-chat-btn");
const chatBox = document.getElementById("chat-box");
const chatInputField = document.getElementById("chat-input-field");
const sendChatMessageBtn = document.getElementById("send-chat-message-btn");
const chatGroupTitle = document.getElementById("chat-group-title");
const chatGroupAvatar = document.getElementById("chat-group-avatar");

// Toast Elements
const appToast = document.getElementById("app-toast");
const toastMessage = document.getElementById("toast-message");

// Initialize icons and render posts on startup
document.addEventListener("DOMContentLoaded", () => {
  renderRides(ridesData);
  if (typeof lucide !== "undefined") {
    lucide.createIcons();
  }
});

// Toast notification helper
function showToast(message, duration = 3000) {
  toastMessage.textContent = message;
  appToast.classList.add("active");
  setTimeout(() => {
    appToast.classList.remove("active");
  }, duration);
}

// Render dynamic ride posts
function renderRides(rides) {
  ridesFeed.innerHTML = "";
  
  if (rides.length === 0) {
    ridesFeed.innerHTML = `
      <div style="text-align: center; padding: 3rem; background: var(--bg-secondary); border-radius: var(--border-radius-md); border: 1px solid var(--border-color);">
        <i data-lucide="info" style="width: 48px; height: 48px; color: var(--accent-gold); margin-bottom: 1rem;"></i>
        <h4 style="font-size: 1.15rem; margin-bottom: 0.5rem;">No rides found</h4>
        <p style="color: var(--text-secondary); max-width: 400px; margin: 0 auto 1.5rem auto;">Try checking other campus gates, searching general locations, or post a new ride yourself.</p>
        <button class="btn btn-primary btn-sm" onclick="resetFilters()">Reset Search filters</button>
      </div>
    `;
    ridesCountBadge.textContent = "0";
    if (typeof lucide !== "undefined") {
      lucide.createIcons();
    }
    return;
  }

  ridesCountBadge.textContent = rides.length;

  rides.forEach(ride => {
    const isFull = ride.seatsAvailable === 0;
    const splitFare = (ride.fareTotal / (ride.seatsTotal + 1 - ride.seatsAvailable)).toFixed(0);
    
    // Create status tag
    const statusClass = isFull ? 'status-full' : 'status-active';
    const statusText = isFull ? 'Full' : `${ride.seatsAvailable} seat${ride.seatsAvailable > 1 ? 's' : ''} left`;

    // Create dots for seats visual layout
    let seatDots = '';
    for (let i = 0; i < ride.seatsTotal; i++) {
      const isTaken = i >= ride.seatsAvailable;
      seatDots += `<div class="seat-dot ${isTaken ? 'taken' : ''}"></div>`;
    }

    // Co-traveler avatars
    let coTravelersHtml = '';
    ride.coTravelers.forEach(name => {
      const initials = name.split(" ").map(n => n[0]).join("").toUpperCase();
      coTravelersHtml += `<div class="co-traveler-avatar-mini" title="${name}">${initials}</div>`;
    });

    const card = document.createElement("div");
    card.className = "ride-card";
    card.innerHTML = `
      <div class="ride-card-header">
        <div class="student-info">
          <div class="student-avatar">${ride.creatorName.split(" ").map(n => n[0]).join("").toUpperCase()}</div>
          <div class="student-details">
            <h4>${ride.creatorName}</h4>
            <span>${ride.creatorBranch}</span>
          </div>
        </div>
        <span class="ride-status-badge ${statusClass}">${statusText}</span>
      </div>

      <div class="route-info">
        <div class="route-point">
          <span class="label">Pickup</span>
          <span class="loc">${ride.from}</span>
        </div>
        <div class="route-arrow">
          <i data-lucide="arrow-right" style="width: 16px; height: 16px;"></i>
        </div>
        <div class="route-point">
          <span class="label">Destination</span>
          <span class="loc">${ride.to}</span>
        </div>
      </div>

      <div class="ride-meta-grid">
        <div class="meta-item">
          <span class="label">Departure</span>
          <span class="value"><i data-lucide="clock" style="width: 14px; height: 14px; color: var(--accent-gold);"></i> ${ride.time}</span>
        </div>
        <div class="meta-item">
          <span class="label">Splitting Cost</span>
          <span class="value" style="color: var(--accent-gold);">₹${splitFare} <span style="font-size: 0.7rem; font-weight: normal; color: var(--text-muted);">/ student</span></span>
        </div>
        <div class="meta-item">
          <span class="label">Auto Capacity</span>
          <div class="seats-indicator">
            ${seatDots}
          </div>
        </div>
      </div>

      <div class="ride-card-footer">
        <div class="co-travelers-mini">
          ${coTravelersHtml}
          ${ride.coTravelers.length > 0 ? `<span style="font-size: 0.75rem; color: var(--text-muted); margin-left: 0.5rem;">+${ride.coTravelers.length} joined</span>` : '<span style="font-size: 0.75rem; color: var(--text-muted);">No co-travelers yet</span>'}
        </div>
        
        <div>
          ${isFull 
            ? `<button class="btn btn-secondary btn-sm" disabled style="padding: 0.5rem 1rem; font-size: 0.85rem;">Group Full</button>` 
            : `<button class="btn btn-outline-gold btn-sm" onclick="joinRideGroup(${ride.id})" style="padding: 0.5rem 1rem; font-size: 0.85rem;"><i data-lucide="user-plus" style="width: 14px; height: 14px; display: inline-block;"></i> Join Ride</button>`
          }
          <button class="btn btn-secondary btn-sm" onclick="openChatWithGroup(${ride.id})" style="padding: 0.5rem 1rem; font-size: 0.85rem; margin-left: 0.25rem;"><i data-lucide="message-square" style="width: 14px; height: 14px; display: inline-block;"></i> Chat</button>
        </div>
      </div>
    `;
    ridesFeed.appendChild(card);
  });

  if (typeof lucide !== "undefined") {
    lucide.createIcons();
  }
}

// Join ride activity
window.joinRideGroup = function(rideId) {
  const ride = ridesData.find(r => r.id === rideId);
  if (ride && ride.seatsAvailable > 0) {
    ride.seatsAvailable -= 1;
    ride.coTravelers.push("You");
    
    // Add simulated message to coordination chat logs
    if (!simulatedMessagesByRide[rideId]) {
      simulatedMessagesByRide[rideId] = [];
    }
    simulatedMessagesByRide[rideId].push({
      sender: "System",
      text: "You joined the ride. Say hi to coordinate pickup!",
      time: getCurrentTimeStr()
    });

    renderRides(ridesData);
    showToast(`Successfully joined ${ride.creatorName}'s ride to ${ride.to}!`);
    
    // Open chat automatically
    setTimeout(() => {
      openChatWithGroup(rideId);
    }, 600);
  }
};

// Filter search operations
function applyFilters() {
  const pickup = searchFromInput.value.toLowerCase().trim();
  const destination = searchToInput.value.toLowerCase().trim();
  const departureWindow = searchTimeInput.value;

  let filtered = ridesData.filter(ride => {
    // Pickup filter
    const matchPickup = ride.from.toLowerCase().includes(pickup);
    
    // Destination filter
    const matchDest = ride.to.toLowerCase().includes(destination);

    // Departure time window filter simulation
    let matchTime = true;
    if (departureWindow === "now") {
      // simulate matches
      matchTime = ride.time >= "16:00" && ride.time <= "18:00";
    } else if (departureWindow === "1hr") {
      matchTime = ride.time >= "16:30" && ride.time <= "18:30";
    } else if (departureWindow === "evening") {
      matchTime = ride.time >= "17:00";
    }

    return matchPickup && matchDest && matchTime;
  });

  renderRides(filtered);
  resetFiltersBtn.style.display = "inline-flex";
}

// Reset filters back to default
window.resetFilters = function() {
  searchFromInput.selectedIndex = 0;
  searchToInput.value = "";
  searchTimeInput.selectedIndex = 0;
  renderRides(ridesData);
  resetFiltersBtn.style.display = "none";
};

// Event Listeners for search
searchBtn.addEventListener("click", applyFilters);
searchToInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    applyFilters();
  }
});

// Interactive Hotspot clicks
document.querySelectorAll(".hotspot-item").forEach(item => {
  item.addEventListener("click", () => {
    const dest = item.getAttribute("data-destination");
    searchToInput.value = dest;
    applyFilters();
    
    // Smooth scroll to feed
    document.getElementById("active-rides").scrollIntoView({ behavior: 'smooth' });
  });
});

// Modal Operations
openPostRideBtn.addEventListener("click", () => {
  postRideModal.classList.add("active");
  updateFareSplitCalculator();
});

function closeModal() {
  postRideModal.classList.remove("active");
  postRideForm.reset();
  // reset selector
  seatBtns.forEach(btn => btn.classList.remove("active"));
  seatBtns[0].classList.add("active");
  rideSeatsHidden.value = "1";
}

closePostRideBtn.addEventListener("click", closeModal);
postRideModal.addEventListener("click", (e) => {
  if (e.target === postRideModal) closeModal();
});

// Seat selection UI triggers
seatBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    seatBtns.forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    rideSeatsHidden.value = btn.getAttribute("data-seats");
    updateFareSplitCalculator();
  });
});

// Fare splitting display logic
function updateFareSplitCalculator() {
  const totalFare = parseFloat(rideFareInput.value) || 0;
  const totalSeats = parseInt(rideSeatsHidden.value) || 1;
  // Cost split is divided between driver/host (1 person) and co-travelers (totalSeats)
  const splitCost = totalFare / (totalSeats + 1);
  farePerPersonText.textContent = `₹${splitCost.toFixed(2)}`;
}

rideFareInput.addEventListener("input", updateFareSplitCalculator);

// Handle new ride post form submission
postRideForm.addEventListener("submit", (e) => {
  e.preventDefault();
  
  const creator = document.getElementById("ride-name").value.trim();
  const fromLoc = document.getElementById("ride-from").value;
  const toLoc = document.getElementById("ride-to").value.trim();
  const timeVal = document.getElementById("ride-time").value;
  const seatsCount = parseInt(rideSeatsHidden.value);
  const totalFare = parseInt(rideFareInput.value);

  if (!creator || !toLoc || !timeVal) {
    showToast("Please fill all fields!");
    return;
  }

  // Create new ride offer object
  const newRide = {
    id: ridesData.length + 1,
    creatorName: creator,
    creatorBranch: "Student Guest",
    from: fromLoc,
    to: toLoc,
    time: timeVal,
    seatsTotal: seatsCount,
    seatsAvailable: seatsCount,
    fareTotal: totalFare,
    coTravelers: []
  };

  // Add to start of array
  ridesData.unshift(newRide);
  
  // Create chat history for this new ride
  simulatedMessagesByRide[newRide.id] = [
    { sender: "System", text: `Ride created by ${newRide.creatorName}. Waiting for students to join!`, time: getCurrentTimeStr() }
  ];

  renderRides(ridesData);
  closeModal();
  showToast("Your TukTuk ride share offer has been published!");

  // Increment active stats
  const statElement = document.getElementById("stat-active-groups");
  if (statElement) {
    statElement.textContent = parseInt(statElement.textContent) + 1;
  }
});

// Simulated real-time Chat Widget functionality
window.openChatWithGroup = function(rideId) {
  activeChatRideId = rideId;
  const ride = ridesData.find(r => r.id === rideId);
  if (!ride) return;

  chatGroupTitle.textContent = `${ride.creatorName}'s Ride`;
  chatGroupAvatar.textContent = ride.creatorName.split(" ").map(n => n[0]).join("").toUpperCase();

  // Populate messages
  populateChatMessages(rideId);

  // Show drawer
  chatDrawer.classList.add("active");
  chatTriggerBtn.classList.add("hidden");

  // Scroll to bottom
  chatBox.scrollTop = chatBox.scrollHeight;
};

function populateChatMessages(rideId) {
  chatBox.innerHTML = "";
  const messages = simulatedMessagesByRide[rideId] || [];

  if (messages.length === 0) {
    chatBox.innerHTML = `
      <div style="text-align: center; color: var(--text-muted); font-size: 0.85rem; padding: 2rem 1rem;">
        No coordination chat yet. Start the conversation!
      </div>
    `;
    return;
  }

  messages.forEach(msg => {
    const isSystem = msg.sender === "System";
    
    if (isSystem) {
      chatBox.innerHTML += `
        <div style="text-align: center; color: var(--text-muted); font-size: 0.75rem; margin: 0.5rem 0; font-style: italic;">
          ${msg.text}
        </div>
      `;
    } else {
      const isMe = msg.sender === "You";
      chatBox.innerHTML += `
        <div class="message ${isMe ? 'sent' : 'received'}">
          <div style="font-size: 0.7rem; font-weight: bold; margin-bottom: 2px;">${msg.sender}</div>
          <div>${msg.text}</div>
          <div class="message-time">${msg.time}</div>
        </div>
      `;
    }
  });
}

function handleSendMessage() {
  const text = chatInputField.value.trim();
  if (!text || activeChatRideId === null) return;

  // Add user message
  const chatList = simulatedMessagesByRide[activeChatRideId] || [];
  chatList.push({
    sender: "You",
    text: text,
    time: getCurrentTimeStr()
  });

  simulatedMessagesByRide[activeChatRideId] = chatList;
  populateChatMessages(activeChatRideId);
  chatInputField.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;

  // Trigger simulated response from ride creator
  simulateCreatorReply(activeChatRideId);
}

// Simulated Reply Engine based on destination context
function simulateCreatorReply(rideId) {
  const ride = ridesData.find(r => r.id === rideId);
  if (!ride) return;

  setTimeout(() => {
    // Only respond if chat is still focused on same ride
    if (activeChatRideId !== rideId) return;

    const replies = [
      `Awesome! I am waiting near the tea shop by ${ride.from}. I have a blue water bottle.`,
      `Perfect, let's meet in 5 minutes! I'm heading out of class now.`,
      `Hey! I am getting the auto rickshaw driver now, please arrive at ${ride.from} asap so we can split fare.`,
      `Got it. I'm wearing a black hoodie. Let me know when you reach.`
    ];
    
    const randomReply = replies[Math.floor(Math.random() * replies.length)];

    const chatList = simulatedMessagesByRide[rideId] || [];
    chatList.push({
      sender: ride.creatorName,
      text: randomReply,
      time: getCurrentTimeStr()
    });

    simulatedMessagesByRide[rideId] = chatList;
    populateChatMessages(rideId);
    chatBox.scrollTop = chatBox.scrollHeight;

    if (typeof lucide !== "undefined") {
      lucide.createIcons();
    }
  }, 1500);
}

// Chat Trigger events
chatTriggerBtn.addEventListener("click", () => {
  // Open with first active ride if none selected yet
  if (ridesData.length > 0) {
    openChatWithGroup(ridesData[0].id);
  } else {
    chatDrawer.classList.add("active");
    chatTriggerBtn.classList.add("hidden");
  }
});

closeChatBtn.addEventListener("click", () => {
  chatDrawer.classList.remove("active");
  chatTriggerBtn.classList.remove("hidden");
});

sendChatMessageBtn.addEventListener("click", handleSendMessage);
chatInputField.addEventListener("keypress", (e) => {
  if (e.key === "Enter") handleSendMessage();
});

// Helper for formatting current time HH:MM
function getCurrentTimeStr() {
  const now = new Date();
  const hrs = String(now.getHours()).padStart(2, '0');
  const mins = String(now.getMinutes()).padStart(2, '0');
  return `${hrs}:${mins}`;
}
