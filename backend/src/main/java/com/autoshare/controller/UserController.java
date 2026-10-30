package com.autoshare.controller;

import com.autoshare.dto.UserRequest;
import com.autoshare.dto.UserResponse;
import com.autoshare.dto.UserUpdateRequest;
import com.autoshare.dto.UserVerificationResponse;
import com.autoshare.model.AccountStatus;
import com.autoshare.model.UserRole;
import com.autoshare.service.UserService;
import jakarta.validation.Valid;
import java.net.URI;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Presentation Layer: REST Controller exposing full CRUD and verification APIs
 * for Campus User Records (Unit-5 Spring Data JPA).
 *
 * AUTO-CONFIGURATION NOTE:
 * Spring Boot's Web MVC auto-configures DispatcherServlet to map these REST routes,
 * integrates Jackson for JSON marshaling/unmarshaling, and validates payloads using Hibernate Validator.
 */
@RestController
@RequestMapping("/api/users")
@CrossOrigin(origins = "*")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    /**
     * GET /api/users - Retrieve all users or filter by search query, department, or role.
     */
    @GetMapping
    public ResponseEntity<List<UserResponse>> getAllUsers(
            @RequestParam(required = false) String search,
            @RequestParam(required = false) String department,
            @RequestParam(required = false) UserRole role) {

        if (search != null && !search.trim().isEmpty()) {
            return ResponseEntity.ok(userService.searchUsers(search));
        }
        if (department != null && !department.trim().isEmpty()) {
            return ResponseEntity.ok(userService.getUsersByDepartment(department));
        }
        if (role != null) {
            return ResponseEntity.ok(userService.getUsersByRole(role));
        }
        return ResponseEntity.ok(userService.getAllUsers());
    }

    /**
     * GET /api/users/{id} - Retrieve single user record by numeric ID.
     */
    @GetMapping("/{id}")
    public ResponseEntity<UserResponse> getUserById(@PathVariable Long id) {
        return ResponseEntity.ok(userService.getUserById(id));
    }

    /**
     * GET /api/users/email/{email} - Lookup user record by email address.
     */
    @GetMapping("/email/{email}")
    public ResponseEntity<UserResponse> getUserByEmail(@PathVariable String email) {
        return ResponseEntity.ok(userService.getUserByEmail(email));
    }

    /**
     * GET /api/users/reg/{registrationNumber} - Lookup user by institutional registration number.
     */
    @GetMapping("/reg/{registrationNumber}")
    public ResponseEntity<UserResponse> getUserByRegistrationNumber(@PathVariable String registrationNumber) {
        return ResponseEntity.ok(userService.getUserByRegistrationNumber(registrationNumber));
    }

    /**
     * POST /api/users - Create/Register a new user record in the relational database.
     */
    @PostMapping
    public ResponseEntity<UserResponse> createUser(@Valid @RequestBody UserRequest request) {
        UserResponse created = userService.createUser(request);
        return ResponseEntity.created(URI.create("/api/users/" + created.getId())).body(created);
    }

    /**
     * PUT /api/users/{id} - Update an existing user record.
     */
    @PutMapping("/{id}")
    public ResponseEntity<UserResponse> updateUser(
            @PathVariable Long id,
            @Valid @RequestBody UserUpdateRequest request) {
        return ResponseEntity.ok(userService.updateUser(id, request));
    }

    /**
     * PATCH /api/users/{id}/status - Update user account status (e.g. ACTIVE, SUSPENDED, VERIFIED).
     */
    @PatchMapping("/{id}/status")
    public ResponseEntity<UserResponse> updateStatus(
            @PathVariable Long id,
            @RequestParam AccountStatus status) {
        return ResponseEntity.ok(userService.updateStatus(id, status));
    }

    /**
     * DELETE /api/users/{id} - Delete a user record from the database.
     */
    @DeleteMapping("/{id}")
    public ResponseEntity<Map<String, Object>> deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        Map<String, Object> response = new HashMap<>();
        response.put("deleted", true);
        response.put("userId", id);
        response.put("message", "User record " + id + " successfully deleted from database");
        return ResponseEntity.ok(response);
    }

    /**
     * GET /api/users/verify/{email} - Inter-Service Microservice Verification REST API.
     * Queried by the Ride Microservice to verify commuter authorization.
     */
    @GetMapping("/verify/{email}")
    public ResponseEntity<UserVerificationResponse> verifyUser(@PathVariable String email) {
        return ResponseEntity.ok(userService.verifyUserForRide(email));
    }

    /**
     * GET /api/users/meta/count - Return total count of registered campus users.
     */
    @GetMapping("/meta/count")
    public ResponseEntity<Map<String, Object>> getUserCount() {
        Map<String, Object> countMap = new HashMap<>();
        countMap.put("totalUsers", userService.getUserCount());
        countMap.put("service", "User-Management-Service");
        return ResponseEntity.ok(countMap);
    }
}
