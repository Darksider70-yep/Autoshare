package com.autoshare.dto;

import com.autoshare.model.RideStatus;
import java.time.LocalDateTime;
import java.util.List;

public class RideResponse {
    private final Long id;
    private final String hostName;
    private final String pickupGate;
    private final String destination;
    private final LocalDateTime departureTime;
    private final double totalFare;
    private final int totalSeats;
    private final int seatsTaken;
    private final int seatsAvailable;
    private final double farePerPerson;
    private final RideStatus status;
    private final List<BookingResponse> bookings;

    public RideResponse(Long id, String hostName, String pickupGate, String destination,
                        LocalDateTime departureTime, double totalFare, int totalSeats,
                        int seatsTaken, int seatsAvailable, double farePerPerson,
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

    public Long getId() { return id; }
    public String getHostName() { return hostName; }
    public String getPickupGate() { return pickupGate; }
    public String getDestination() { return destination; }
    public LocalDateTime getDepartureTime() { return departureTime; }
    public double getTotalFare() { return totalFare; }
    public int getTotalSeats() { return totalSeats; }
    public int getSeatsTaken() { return seatsTaken; }
    public int getSeatsAvailable() { return seatsAvailable; }
    public double getFarePerPerson() { return farePerPerson; }
    public RideStatus getStatus() { return status; }
    public List<BookingResponse> getBookings() { return bookings; }
}
