package com.autoshare.dto;

import jakarta.validation.constraints.Future;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;
import java.time.LocalDateTime;

public class RideRequest {

    @NotBlank(message = "Host name is required")
    private String hostName;

    @NotBlank(message = "Pickup gate is required")
    private String pickupGate;

    @NotBlank(message = "Destination is required")
    private String destination;

    @NotNull(message = "Departure time is required")
    @Future(message = "Departure time must be in the future")
    private LocalDateTime departureTime;

    @Positive(message = "Total fare must be greater than 0")
    private double totalFare;

    @Min(value = 1, message = "At least 1 seat is required")
    @Max(value = 3, message = "At most 3 co-passenger seats are allowed")
    private int totalSeats;

    public RideRequest() { }

    public String getHostName() { return hostName; }
    public void setHostName(String hostName) { this.hostName = hostName; }
    public String getPickupGate() { return pickupGate; }
    public void setPickupGate(String pickupGate) { this.pickupGate = pickupGate; }
    public String getDestination() { return destination; }
    public void setDestination(String destination) { this.destination = destination; }
    public LocalDateTime getDepartureTime() { return departureTime; }
    public void setDepartureTime(LocalDateTime departureTime) { this.departureTime = departureTime; }
    public double getTotalFare() { return totalFare; }
    public void setTotalFare(double totalFare) { this.totalFare = totalFare; }
    public int getTotalSeats() { return totalSeats; }
    public void setTotalSeats(int totalSeats) { this.totalSeats = totalSeats; }
}
