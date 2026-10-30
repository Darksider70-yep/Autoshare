package com.autoshare.dto;

import com.autoshare.model.AccountStatus;
import com.autoshare.model.UserRole;

/**
 * Inter-service verification response DTO used in Microservice-based interactions.
 * Ride Microservice queries User Microservice to verify commuter status and eligibility.
 */
public class UserVerificationResponse {

    private boolean verified;
    private String email;
    private String registrationNumber;
    private String fullName;
    private UserRole role;
    private AccountStatus status;
    private boolean eligibleToRide;
    private String message;

    public UserVerificationResponse() {
    }

    public UserVerificationResponse(boolean verified, String email, String registrationNumber,
                                    String fullName, UserRole role, AccountStatus status,
                                    boolean eligibleToRide, String message) {
        this.verified = verified;
        this.email = email;
        this.registrationNumber = registrationNumber;
        this.fullName = fullName;
        this.role = role;
        this.status = status;
        this.eligibleToRide = eligibleToRide;
        this.message = message;
    }

    public boolean isVerified() {
        return verified;
    }

    public void setVerified(boolean verified) {
        this.verified = verified;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getRegistrationNumber() {
        return registrationNumber;
    }

    public void setRegistrationNumber(String registrationNumber) {
        this.registrationNumber = registrationNumber;
    }

    public String getFullName() {
        return fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    public UserRole getRole() {
        return role;
    }

    public void setRole(UserRole role) {
        this.role = role;
    }

    public AccountStatus getStatus() {
        return status;
    }

    public void setStatus(AccountStatus status) {
        this.status = status;
    }

    public boolean isEligibleToRide() {
        return eligibleToRide;
    }

    public void setEligibleToRide(boolean eligibleToRide) {
        this.eligibleToRide = eligibleToRide;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
