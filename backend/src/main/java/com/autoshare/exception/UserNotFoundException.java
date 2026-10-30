package com.autoshare.exception;

/**
 * Thrown when a user record cannot be found by ID, email, or registration number.
 */
public class UserNotFoundException extends RuntimeException {

    public UserNotFoundException(String message) {
        super(message);
    }
}
