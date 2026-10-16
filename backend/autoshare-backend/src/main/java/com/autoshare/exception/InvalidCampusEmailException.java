package com.autoshare.exception;

public class InvalidCampusEmailException extends RuntimeException {
    public InvalidCampusEmailException(String email, String domain) {
        super("Invalid email " + email + ". Only official campus email addresses ending with "
                + domain + " can book a seat.");
    }
}
