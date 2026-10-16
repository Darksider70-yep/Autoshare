package com.autoshare.dto;

/**
 * Dedicated DTO for GET /api/rides/{id}/fare-split endpoint.
 */
public class FareSplitResponse {

    private Long rideId;
    private String destination;
    private double totalFare;
    private int totalRiders; // Co-passengers + 1 host
    private double farePerPerson;

    public FareSplitResponse() {
    }

    public FareSplitResponse(Long rideId, String destination, double totalFare, int totalRiders, double farePerPerson) {
        this.rideId = rideId;
        this.destination = destination;
        this.totalFare = totalFare;
        this.totalRiders = totalRiders;
        this.farePerPerson = farePerPerson;
    }

    public Long getRideId() {
        return rideId;
    }

    public void setRideId(Long rideId) {
        this.rideId = rideId;
    }

    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }

    public double getTotalFare() {
        return totalFare;
    }

    public void setTotalFare(double totalFare) {
        this.totalFare = totalFare;
    }

    public int getTotalRiders() {
        return totalRiders;
    }

    public void setTotalRiders(int totalRiders) {
        this.totalRiders = totalRiders;
    }

    public double getFarePerPerson() {
        return farePerPerson;
    }

    public void setFarePerPerson(double farePerPerson) {
        this.farePerPerson = farePerPerson;
    }
}
