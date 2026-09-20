// Seed mock rides data
export const initialRidesData = [
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

// Initial mock chat messages indexed by ride ID
export const initialChatMessages = {
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

// Popular destination hotspot list
export const popularHotspots = [
  {
    destination: "Starlight Hostels",
    subtitle: "Student PG Hub • 2.5 km away",
    activeCount: 4
  },
  {
    destination: "Green Meadows Flats",
    subtitle: "Apartment cluster • 4.1 km away",
    activeCount: 3
  },
  {
    destination: "R.K. Puram PG Zone",
    subtitle: "PG Zone • 3.5 km away",
    activeCount: 2
  },
  {
    destination: "Royal Residency",
    subtitle: "Hostel cluster • 1.8 km away",
    activeCount: 1
  }
];
