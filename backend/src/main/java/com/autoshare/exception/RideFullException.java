package com.autoshare.exception;

public class RideFullException extends RuntimeException {
    public RideFullException(Long rideId) {
        super("Ride offer #" + rideId + " is already FULL. No available seats remaining.");
    }
}
