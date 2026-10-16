package com.autoshare.exception;

public class RideNotFoundException extends RuntimeException {
    public RideNotFoundException(Long rideId) {
        super("Ride offer with ID " + rideId + " was not found.");
    }
}
