package com.autoshare.exception;

public class RideNotFoundException extends RuntimeException {
    public RideNotFoundException(Long id) {
        super("Ride with id " + id + " was not found.");
    }
}
