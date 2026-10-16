package com.autoshare.dto;

import jakarta.validation.constraints.Future;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.time.LocalDateTime;

/**
 * DTO for incoming ride creation requests.
 * Uses Bean Validation annotations to enforce input constraints.
 */
public class RideRequest {

    @NotBlank(message = "Host name is required")
    private String hostName;

    @NotBlank(message = "Pickup gate is required")
    private String pickupGate;

    @NotBlank(message = "Destination is required")
    private String destination;

    @NotNull(message = "Departure time is required")
    @Future(message = "Departure time must be scheduled in the future")
    private LocalDateTime departureTime;

    @Min(value = 30, message = "Total auto fare must be at least ₹30")
    @Max(value = 1000, message = "Total auto fare cannot exceed ₹1000")
    private double totalFare;

    @Min(value = 1, message = "TukTuk must offer at least 1 co-passenger seat")
    @Max(value = 3, message = "TukTuk cannot exceed 3 co-passenger seats")
    private int totalSeats;

    public RideRequest() {
    }

    public RideRequest(String hostName, String pickupGate, String destination, LocalDateTime departureTime, double totalFare, int totalSeats) {
        this.hostName = hostName;
        this.pickupGate = pickupGate;
        this.destination = destination;
        this.departureTime = departureTime;
        this.totalFare = totalFare;
        this.totalSeats = totalSeats;
    }

    // Getters and Setters
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
}
