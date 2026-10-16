package com.autoshare.dto;

public class FareSplitResponse {
    private final Long rideId;
    private final String destination;
    private final double totalFare;
    private final int totalRiders;
    private final double farePerPerson;

    public FareSplitResponse(Long rideId, String destination, double totalFare,
                             int totalRiders, double farePerPerson) {
        this.rideId = rideId;
        this.destination = destination;
        this.totalFare = totalFare;
        this.totalRiders = totalRiders;
        this.farePerPerson = farePerPerson;
    }

    public Long getRideId() { return rideId; }
    public String getDestination() { return destination; }
    public double getTotalFare() { return totalFare; }
    public int getTotalRiders() { return totalRiders; }
    public double getFarePerPerson() { return farePerPerson; }
}
