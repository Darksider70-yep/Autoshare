package com.autoshare.dto;

import com.autoshare.model.AccountStatus;
import com.autoshare.model.User;
import com.autoshare.model.UserRole;
import java.time.LocalDateTime;

/**
 * Egress DTO representing formatted user details returned by REST APIs.
 */
public class UserResponse {

    private Long id;
    private String fullName;
    private String email;
    private String registrationNumber;
    private String phoneNumber;
    private String department;
    private UserRole role;
    private AccountStatus status;
    private String campusGate;
    private String hostelOrPG;
    private Double rating;
    private Integer totalRidesCount;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    public UserResponse() {
    }

    public static UserResponse fromEntity(User user) {
        if (user == null) {
            return null;
        }
        UserResponse dto = new UserResponse();
        dto.id = user.getId();
        dto.fullName = user.getFullName();
        dto.email = user.getEmail();
        dto.registrationNumber = user.getRegistrationNumber();
        dto.phoneNumber = user.getPhoneNumber();
        dto.department = user.getDepartment();
        dto.role = user.getRole();
        dto.status = user.getStatus();
        dto.campusGate = user.getCampusGate();
        dto.hostelOrPG = user.getHostelOrPG();
        dto.rating = user.getRating();
        dto.totalRidesCount = user.getTotalRidesCount();
        dto.createdAt = user.getCreatedAt();
        dto.updatedAt = user.getUpdatedAt();
        return dto;
    }

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
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

    public Double getRating() {
        return rating;
    }

    public void setRating(Double rating) {
        this.rating = rating;
    }

    public Integer getTotalRidesCount() {
        return totalRidesCount;
    }

    public void setTotalRidesCount(Integer totalRidesCount) {
        this.totalRidesCount = totalRidesCount;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }
}
