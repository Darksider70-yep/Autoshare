package com.autoshare.service;

import com.autoshare.dto.UserRequest;
import com.autoshare.dto.UserResponse;
import com.autoshare.dto.UserUpdateRequest;
import com.autoshare.dto.UserVerificationResponse;
import com.autoshare.model.AccountStatus;
import com.autoshare.model.UserRole;
import java.util.List;

/**
 * Service Layer Interface declaring business operations and CRUD contracts for User records.
 */
public interface UserService {

    List<UserResponse> getAllUsers();

    UserResponse getUserById(Long id);

    UserResponse getUserByEmail(String email);

    UserResponse getUserByRegistrationNumber(String registrationNumber);

    List<UserResponse> searchUsers(String query);

    List<UserResponse> getUsersByDepartment(String department);

    List<UserResponse> getUsersByRole(UserRole role);

    UserResponse createUser(UserRequest request);

    UserResponse updateUser(Long id, UserUpdateRequest request);

    UserResponse updateStatus(Long id, AccountStatus status);

    void deleteUser(Long id);

    UserVerificationResponse verifyUserForRide(String email);

    long getUserCount();
}
