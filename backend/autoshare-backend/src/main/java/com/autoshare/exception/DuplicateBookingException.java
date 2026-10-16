package com.autoshare.exception;

public class DuplicateBookingException extends RuntimeException {
    public DuplicateBookingException(String email, Long rideId) {
        super("Student " + email + " has already reserved a seat on ride " + rideId + ".");
    }
}
