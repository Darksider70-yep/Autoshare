package com.autoshare.dto;

import com.autoshare.model.AccountStatus;
import com.autoshare.model.UserRole;
import jakarta.validation.constraints.Pattern;

/**
 * Ingress DTO for updating an existing campus user record.
 */
public class UserUpdateRequest {

    private String fullName;

    @Pattern(regexp = "^[0-9]{10}$", message = "Phone number must be exactly 10 digits")
    private String phoneNumber;

    private String department;
    private UserRole role;
    private AccountStatus status;
    private String campusGate;
    private String hostelOrPG;

    public UserUpdateRequest() {
    }

    public UserUpdateRequest(String fullName, String phoneNumber, String department,
                              UserRole role, AccountStatus status, String campusGate, String hostelOrPG) {
        this.fullName = fullName;
        this.phoneNumber = phoneNumber;
        this.department = department;
        this.role = role;
        this.status = status;
        this.campusGate = campusGate;
        this.hostelOrPG = hostelOrPG;
    }

    public String getFullName() {
        return fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
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

    public AccountStatus getStatus() {
        return status;
    }

    public void setStatus(AccountStatus status) {
        this.status = status;
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
