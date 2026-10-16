package com.autoshare.exception;

public class InvalidCampusEmailException extends RuntimeException {
    public InvalidCampusEmailException(String email, String expectedDomain) {
        super("Invalid email '" + email + "'. Only official campus email addresses ending with '" + expectedDomain + "' are authorized to reserve seats.");
    }
}
