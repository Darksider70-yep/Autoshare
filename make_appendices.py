import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
import os
from docx_helpers import (
    add_p, add_heading_1, add_heading_2, add_heading_3, add_heading_4,
    add_styled_table, add_code_block
)

def build_appendices(doc):
    # ==========================================
    # APPENDIX A: SAMPLE CODING
    # ==========================================
    add_heading_1(doc, "APPENDIX A\nSAMPLE CODING")
    
    add_p(doc, "This appendix contains representative production source code extracts from the core backend and frontend "
               "modules of Autoshare, illustrating domain entity modeling, transactional business rules, inter-service "
               "REST integration with circuit breaker fallback, and reactive user interface state machines.", 
          size_pt=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=4, space_after=10, line_spacing=1.15)

    # 1. Ride.java
    add_heading_3(doc, "A.1 Domain Entity: Ride.java (Spring Data JPA)")
    code_ride = '''package com.autoshare.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "rides")
public class Ride {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank(message = "Host name is required")
    private String hostName;

    @NotBlank(message = "Pickup gate is required")
    private String pickupGate;

    @NotBlank(message = "Destination is required")
    private String destination;

    @NotNull(message = "Departure time is required")
    private LocalDateTime departureTime;

    @DecimalMin(value = "0.0", inclusive = false, message = "Total fare must be positive")
    private double totalFare;

    @Min(value = 1, message = "At least 1 seat must be offered")
    @Max(value = 3, message = "Cannot offer more than 3 co-passenger seats")
    private int totalSeats;

    private int seatsTaken = 0;

    @Enumerated(EnumType.STRING)
    private RideStatus status = RideStatus.OPEN;

    @OneToMany(mappedBy = "ride", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.EAGER)
    private List<Booking> bookings = new ArrayList<>();

    // Business Logic: Dynamic proportional fare split per commuter
    public double calculateFarePerPerson() {
        return totalFare / (seatsTaken + 1);
    }
    // Getters, setters, and constructors omitted for brevity
}'''
    add_code_block(doc, code_ride)

    # 2. User.java
    add_heading_3(doc, "A.2 Persistent User Entity: User.java")
    code_user = '''package com.autoshare.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;
import java.time.LocalDateTime;

@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank(message = "Full name is required")
    private String fullName;

    @Email(message = "Must be a valid email format")
    @Pattern(regexp = "^[A-Za-z0-9._%+-]+@srmist\\.edu\\.in$", message = "Must be an official @srmist.edu.in email")
    @Column(unique = true, nullable = false)
    private String email;

    @Pattern(regexp = "^RA[0-9]{13}$", message = "Registration number must follow SRM format (e.g., RA2411003012297)")
    @Column(name = "registration_number", unique = true, nullable = false)
    private String registrationNumber;

    @NotBlank(message = "Department is required")
    private String department;

    @Enumerated(EnumType.STRING)
    private UserRole role = UserRole.STUDENT;

    @Enumerated(EnumType.STRING)
    private AccountStatus status = AccountStatus.ACTIVE;

    @CreationTimestamp
    private LocalDateTime createdAt;

    @UpdateTimestamp
    private LocalDateTime updatedAt;
    // Getters, setters, and constructors omitted for brevity
}'''
    add_code_block(doc, code_user)

    # 3. RideService.java
    add_heading_3(doc, "A.3 Dynamic Fare Split Engine: RideService.java")
    code_service = '''package com.autoshare.service;

import com.autoshare.model.*;
import com.autoshare.repository.*;
import com.autoshare.exception.*;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.time.LocalDateTime;

@Service
@Transactional
public class RideService {
    private final RideRepository rideRepository;
    private final BookingRepository bookingRepository;
    private final UserVerificationClient userClient;

    public RideService(RideRepository rideRepo, BookingRepository bookRepo, UserVerificationClient client) {
        this.rideRepository = rideRepo;
        this.bookingRepository = bookRepo;
        this.userClient = client;
    }

    public synchronized BookingResponse bookSeat(Long rideId, String studentName, String studentEmail) {
        Ride ride = rideRepository.findById(rideId)
            .orElseThrow(() -> new RideNotFoundException("Ride not found with ID: " + rideId));

        if (ride.getStatus() == RideStatus.FULL || ride.getSeatsTaken() >= ride.getTotalSeats()) {
            throw new RideFullException("Ride is already at legal vehicle capacity (3 passengers)");
        }

        // Domain Rule: Prevent duplicate bookings on the same ride
        boolean alreadyBooked = bookingRepository.existsByRideIdAndStudentEmail(rideId, studentEmail);
        if (alreadyBooked) {
            throw new DuplicateBookingException("Student has already booked a seat on this ride");
        }

        // Inter-Service Verification with Circuit Breaker Fallback
        UserVerificationResponse kyc = userClient.verifyUser(studentEmail);
        if (!kyc.isVerified()) {
            throw new UnauthorizedStudentException("Commuter KYC verification failed: Unregistered student");
        }

        Booking booking = new Booking(ride, studentName, studentEmail, LocalDateTime.now());
        bookingRepository.save(booking);

        ride.setSeatsTaken(ride.getSeatsTaken() + 1);
        if (ride.getSeatsTaken() >= ride.getTotalSeats()) {
            ride.setStatus(RideStatus.FULL);
        }
        rideRepository.save(ride);

        double splitFare = ride.calculateFarePerPerson();
        return new BookingResponse(booking.getId(), ride.getId(), splitFare, ride.getSeatsTaken(), ride.getStatus());
    }
}'''
    add_code_block(doc, code_service)

    # 4. UserController.java
    add_heading_3(doc, "A.4 User REST Controller: UserController.java")
    code_ctrl = '''package com.autoshare.controller;

import com.autoshare.model.User;
import com.autoshare.service.UserService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/users")
@CrossOrigin(origins = "*")
public class UserController {
    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping
    public ResponseEntity<List<User>> getAllUsers() {
        return ResponseEntity.ok(userService.findAllUsers());
    }

    @GetMapping("/search")
    public ResponseEntity<List<User>> searchUsers(@RequestParam("q") String query) {
        return ResponseEntity.ok(userService.searchUsers(query));
    }

    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody User user) {
        User created = userService.createUser(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }

    @GetMapping("/verify/{email}")
    public ResponseEntity<UserVerificationResponse> verifyUser(@PathVariable String email) {
        return ResponseEntity.ok(userService.verifyCommuterEligibility(email));
    }
}'''
    add_code_block(doc, code_ctrl)

    # 5. App.jsx
    add_heading_3(doc, "A.5 Reactive Single-Page UI: App.jsx (React 19)")
    code_app = '''import React, { useState, useEffect } from 'react';
import HeroSearch from './components/HeroSearch';
import RidesFeed from './components/RidesFeed';
import PostRideModal from './components/PostRideModal';
import UserRecords from './components/UserRecords';
import MicroservicesConsole from './components/MicroservicesConsole';

export default function App() {
  const [activeTab, setActiveTab] = useState('rides');
  const [rides, setRides] = useState([]);
  const [filterDestination, setFilterDestination] = useState('ALL');
  const [filterGate, setFilterGate] = useState('ALL');
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    fetchRides();
  }, [filterDestination, filterGate]);

  const fetchRides = async () => {
    let url = '/api/rides?';
    if (filterDestination !== 'ALL') url += `destination=${filterDestination}&`;
    if (filterGate !== 'ALL') url += `gate=${filterGate}`;
    const res = await fetch(url);
    const data = await res.json();
    setRides(data);
  };

  const handleBookSeat = async (rideId, studentName, studentEmail) => {
    const res = await fetch(`/api/rides/${rideId}/book`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ studentName, studentEmail })
    });
    if (res.ok) {
      fetchRides();
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100">
      <header className="bg-slate-800/80 backdrop-blur border-b border-slate-700 p-4">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <h1 className="text-xl font-bold text-amber-400">Autoshare SRMIST</h1>
          <nav className="flex gap-2">
            <button onClick={() => setActiveTab('rides')} className={`px-4 py-2 rounded-lg font-medium transition ${activeTab === 'rides' ? 'bg-amber-500 text-slate-950 font-bold' : 'hover:bg-slate-700'}`}>Campus Rides</button>
            <button onClick={() => setActiveTab('users')} className={`px-4 py-2 rounded-lg font-medium transition ${activeTab === 'users' ? 'bg-amber-500 text-slate-950 font-bold' : 'hover:bg-slate-700'}`}>User Records</button>
            <button onClick={() => setActiveTab('console')} className={`px-4 py-2 rounded-lg font-medium transition ${activeTab === 'console' ? 'bg-amber-500 text-slate-950 font-bold' : 'hover:bg-slate-700'}`}>Microservices Console</button>
          </nav>
        </div>
      </header>
      <main className="max-w-7xl mx-auto p-6">
        {activeTab === 'rides' && <RidesFeed rides={rides} onBook={handleBookSeat} onOpenPostModal={() => setIsModalOpen(true)} />}
        {activeTab === 'users' && <UserRecords />}
        {activeTab === 'console' && <MicroservicesConsole />}
      </main>
      {isModalOpen && <PostRideModal onClose={() => setIsModalOpen(false)} onRideCreated={fetchRides} />}
    </div>
  );
}'''
    add_code_block(doc, code_app)

    # 6. RideBookingServiceTest.java
    add_heading_3(doc, "A.6 Automated Test Suite: RideBookingServiceTest.java (JUnit 5)")
    code_test = '''package com.autoshare.service;

import com.autoshare.model.*;
import com.autoshare.repository.*;
import com.autoshare.exception.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import java.time.LocalDateTime;
import java.util.Optional;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class RideBookingServiceTest {
    @Mock private RideRepository rideRepository;
    @Mock private BookingRepository bookingRepository;
    @Mock private UserVerificationClient userClient;
    private RideService rideService;

    @BeforeEach
    void setUp() {
        rideService = new RideService(rideRepository, bookingRepository, userClient);
    }

    @Test
    void testBookSeat_DynamicFareSplitSuccess() {
        Ride ride = new Ride("Daksh", "Gate 1", "Estancia", LocalDateTime.now(), 120.0, 3);
        when(rideRepository.findById(1L)).thenReturn(Optional.of(ride));
        when(bookingRepository.existsByRideIdAndStudentEmail(1L, "rohit@srmist.edu.in")).thenReturn(false);
        when(userClient.verifyUser("rohit@srmist.edu.in")).thenReturn(new UserVerificationResponse(true, false));

        BookingResponse response = rideService.bookSeat(1L, "Rohit", "rohit@srmist.edu.in");

        assertNotNull(response);
        assertEquals(60.0, response.getFarePerPerson(), 0.01);
        assertEquals(1, response.getSeatsTaken());
        verify(bookingRepository, times(1)).save(any(Booking.class));
    }

    @Test
    void testBookSeat_ThrowsDuplicateBookingException() {
        Ride ride = new Ride("Daksh", "Gate 1", "Estancia", LocalDateTime.now(), 120.0, 3);
        when(rideRepository.findById(1L)).thenReturn(Optional.of(ride));
        when(bookingRepository.existsByRideIdAndStudentEmail(1L, "rohit@srmist.edu.in")).thenReturn(true);

        assertThrows(DuplicateBookingException.class, () -> {
            rideService.bookSeat(1L, "Rohit", "rohit@srmist.edu.in");
        });
    }
}'''
    add_code_block(doc, code_test)

    print("Appendix A (Sample Coding) generated successfully.")
