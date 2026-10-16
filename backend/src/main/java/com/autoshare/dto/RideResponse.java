package com.autoshare.dto;

import com.autoshare.model.RideStatus;
import java.time.LocalDateTime;
import java.util.List;

/**
 * DTO for outgoing ride data.
 * Includes calculated fields: seatsAvailable and farePerPerson.
 */
public class RideResponse {

    private Long id;
    private String hostName;
    private String pickupGate;
    private String destination;
    private LocalDateTime departureTime;
    private double totalFare;
    private int totalSeats;
    private int seatsTaken;
    private int seatsAvailable;
    private double farePerPerson;
    private RideStatus status;
    private List<BookingResponse> bookings;

    public RideResponse() {
    }

    public RideResponse(Long id, String hostName, String pickupGate, String destination, LocalDateTime departureTime,
                        double totalFare, int totalSeats, int seatsTaken, int seatsAvailable, double farePerPerson,
                        RideStatus status, List<BookingResponse> bookings) {
        this.id = id;
        this.hostName = hostName;
        this.pickupGate = pickupGate;
        this.destination = destination;
        this.departureTime = departureTime;
        this.totalFare = totalFare;
        this.totalSeats = totalSeats;
        this.seatsTaken = seatsTaken;
        this.seatsAvailable = seatsAvailable;
        this.farePerPerson = farePerPerson;
        this.status = status;
        this.bookings = bookings;
    }

    // Getters and Setters
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

    public int getSeatsAvailable() {
        return seatsAvailable;
    }

    public void setSeatsAvailable(int seatsAvailable) {
        this.seatsAvailable = seatsAvailable;
    }

    public double getFarePerPerson() {
        return farePerPerson;
    }

    public void setFarePerPerson(double farePerPerson) {
        this.farePerPerson = farePerPerson;
    }

    public RideStatus getStatus() {
        return status;
    }

    public void setStatus(RideStatus status) {
        this.status = status;
    }

    public List<BookingResponse> getBookings() {
        return bookings;
    }

    public void setBookings(List<BookingResponse> bookings) {
        this.bookings = bookings;
    }
}
