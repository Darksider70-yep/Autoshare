package com.autoshare.model;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * Domain Entity representing a shared TukTuk (auto-rickshaw) ride.
 * AUTO-CONFIGURATION NOTE: Spring Boot's Hibernate auto-configuration scans @Entity
 * classes and generates the database table schema automatically in H2.
 */
@Entity
@Table(name = "rides")
public class Ride {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String hostName;

    @Column(nullable = false)
    private String pickupGate;

    @Column(nullable = false)
    private String destination;

    @Column(nullable = false)
    private LocalDateTime departureTime;

    @Column(nullable = false)
    private double totalFare;

    @Column(nullable = false)
    private int totalSeats; // Available seats for co-passengers (1-3)

    @Column(nullable = false)
    private int seatsTaken;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private RideStatus status;

    @OneToMany(mappedBy = "ride", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Booking> bookings = new ArrayList<>();

    public Ride() {
        this.status = RideStatus.OPEN;
        this.seatsTaken = 0;
    }

    public Ride(String hostName, String pickupGate, String destination, LocalDateTime departureTime, double totalFare, int totalSeats) {
        this.hostName = hostName;
        this.pickupGate = pickupGate;
        this.destination = destination;
        this.departureTime = departureTime;
        this.totalFare = totalFare;
        this.totalSeats = totalSeats;
        this.seatsTaken = 0;
        this.status = RideStatus.OPEN;
    }

    // Helper to calculate dynamic fare per person: totalFare / (seatsTaken + 1 host)
    public double calculateFarePerPerson() {
        int totalPeople = this.seatsTaken + 1; // Co-passengers + 1 host
        return Math.round((this.totalFare / totalPeople) * 100.0) / 100.0;
    }

    public void addBooking(Booking booking) {
        bookings.add(booking);
        booking.setRide(this);
        this.seatsTaken++;
        if (this.seatsTaken >= this.totalSeats) {
            this.status = RideStatus.FULL;
        }
    }

    // Getters and Setters (Lombok-free plain Java)
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getHostName() {
        return hostName;
    }

    public void setHostName(String hostName) {
        this.hostName = hostName;
    }

    public String getPickupGate() {
        return pickupGate;
    }

    public void setPickupGate(String pickupGate) {
        this.pickupGate = pickupGate;
    }

    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }

    public LocalDateTime getDepartureTime() {
        return departureTime;
    }

    public void setDepartureTime(LocalDateTime departureTime) {
        this.departureTime = departureTime;
    }

    public double getTotalFare() {
        return totalFare;
    }

    public void setTotalFare(double totalFare) {
        this.totalFare = totalFare;
    }

    public int getTotalSeats() {
        return totalSeats;
    }

    public void setTotalSeats(int totalSeats) {
        this.totalSeats = totalSeats;
    }

    public int getSeatsTaken() {
        return seatsTaken;
    }

    public void setSeatsTaken(int seatsTaken) {
        this.seatsTaken = seatsTaken;
    }

    public RideStatus getStatus() {
        return status;
    }

    public void setStatus(RideStatus status) {
        this.status = status;
    }

    public List<Booking> getBookings() {
        return bookings;
    }

    public void setBookings(List<Booking> bookings) {
        this.bookings = bookings;
    }
}
