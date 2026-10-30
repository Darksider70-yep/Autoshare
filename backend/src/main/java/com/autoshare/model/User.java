package com.autoshare.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Index;
import jakarta.persistence.PrePersist;
import jakarta.persistence.PreUpdate;
import jakarta.persistence.Table;
import java.time.LocalDateTime;

/**
 * Domain Entity representing a registered campus user record.
 * Managed by Spring Data JPA and persisted in the relational database.
 *
 * AUTO-CONFIGURATION NOTE:
 * Spring Boot's Hibernate auto-configuration inspects this @Entity class and
 * automatically provisions the "users" table with indexed columns and constraints.
 */
@Entity
@Table(
    name = "users",
    indexes = {
        @Index(name = "idx_user_email", columnList = "email", unique = true),
        @Index(name = "idx_user_reg_no", columnList = "registrationNumber", unique = true),
        @Index(name = "idx_user_role", columnList = "role"),
        @Index(name = "idx_user_dept", columnList = "department")
    }
)
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String fullName;

    @Column(nullable = false, unique = true, length = 120)
    private String email;

    @Column(nullable = false, unique = true, length = 30)
    private String registrationNumber;

    @Column(nullable = false, length = 20)
    private String phoneNumber;

    @Column(nullable = false, length = 80)
    private String department;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false, length = 30)
    private UserRole role = UserRole.STUDENT_COMMUTER;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false, length = 30)
    private AccountStatus status = AccountStatus.ACTIVE;

    @Column(length = 60)
    private String campusGate;

    @Column(length = 100)
    private String hostelOrPG;

    @Column(nullable = false)
    private Double rating = 4.9;

    @Column(nullable = false)
    private Integer totalRidesCount = 0;

    @Column(nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(nullable = false)
    private LocalDateTime updatedAt;

    public User() {
    }

    public User(String fullName, String email, String registrationNumber, String phoneNumber,
                String department, UserRole role, AccountStatus status, String campusGate, String hostelOrPG) {
        this.fullName = fullName;
        this.email = email;
        this.registrationNumber = registrationNumber;
        this.phoneNumber = phoneNumber;
        this.department = department;
        this.role = role != null ? role : UserRole.STUDENT_COMMUTER;
        this.status = status != null ? status : AccountStatus.ACTIVE;
        this.campusGate = campusGate;
        this.hostelOrPG = hostelOrPG;
        this.rating = 4.9;
        this.totalRidesCount = 0;
    }

    @PrePersist
    protected void onCreate() {
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();
        if (this.rating == null) {
            this.rating = 4.9;
        }
        if (this.totalRidesCount == null) {
            this.totalRidesCount = 0;
        }
        if (this.role == null) {
            this.role = UserRole.STUDENT_COMMUTER;
        }
        if (this.status == null) {
            this.status = AccountStatus.ACTIVE;
        }
    }

    @PreUpdate
    protected void onUpdate() {
        this.updatedAt = LocalDateTime.now();
    }

    public void incrementRides() {
        this.totalRidesCount = (this.totalRidesCount == null ? 0 : this.totalRidesCount) + 1;
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
