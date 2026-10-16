package com.autoshare.exception;

public class RideFullException extends RuntimeException {
    public RideFullException(Long id) {
        super("Ride with id " + id + " is already FULL. No seats are available.");
    }
}
