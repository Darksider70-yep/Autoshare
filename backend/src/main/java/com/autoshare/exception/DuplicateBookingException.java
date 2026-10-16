package com.autoshare.exception;

public class DuplicateBookingException extends RuntimeException {
    public DuplicateBookingException(String email, Long rideId) {
        super("Student with email '" + email + "' has already reserved a seat in Ride #" + rideId + ".");
    }
}
