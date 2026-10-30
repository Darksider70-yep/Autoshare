package com.autoshare.exception;

/**
 * Thrown when attempting to register a user with an email or registration number that is already taken.
 */
public class UserAlreadyExistsException extends RuntimeException {

    public UserAlreadyExistsException(String message) {
        super(message);
    }
}
