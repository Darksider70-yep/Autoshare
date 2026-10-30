package com.autoshare.dto;

import com.autoshare.model.UserRole;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Pattern;

/**
 * Ingress DTO for creating new campus user records.
 * Uses Jakarta Bean Validation to validate student and commuter credentials.
 */
public class UserRequest {

    @NotBlank(message = "Full name is required")
    private String fullName;

    @NotBlank(message = "Institutional campus email is required")
    @Email(message = "Invalid email format")
    private String email;

    @NotBlank(message = "Registration number is required")
    @Pattern(regexp = "^[A-Za-z0-9]{8,25}$", message = "Registration number must be 8 to 25 alphanumeric characters")
    private String registrationNumber;

    @NotBlank(message = "Phone number is required")
    @Pattern(regexp = "^[0-9]{10}$", message = "Phone number must be exactly 10 digits")
    private String phoneNumber;

    @NotBlank(message = "Academic department is required")
    private String department;

    @NotNull(message = "User role is required")
    private UserRole role = UserRole.STUDENT_COMMUTER;

    private String campusGate;
    private String hostelOrPG;

    public UserRequest() {
    }

    public UserRequest(String fullName, String email, String registrationNumber, String phoneNumber,
                       String department, UserRole role, String campusGate, String hostelOrPG) {
        this.fullName = fullName;
        this.email = email;
        this.registrationNumber = registrationNumber;
        this.phoneNumber = phoneNumber;
        this.department = department;
        this.role = role;
        this.campusGate = campusGate;
        this.hostelOrPG = hostelOrPG;
    }

    public String getFullName() {
        return fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
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

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public UserRole getRole() {
        return role;
    }

    public void setRole(UserRole role) {
        this.role = role;
    }

    public String getCampusGate() {
        return campusGate;
    }

    public void setCampusGate(String campusGate) {
        this.campusGate = campusGate;
    }

    public String getHostelOrPG() {
        return hostelOrPG;
    }

    public void setHostelOrPG(String hostelOrPG) {
        this.hostelOrPG = hostelOrPG;
    }
}
