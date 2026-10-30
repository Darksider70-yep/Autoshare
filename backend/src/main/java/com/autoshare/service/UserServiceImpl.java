package com.autoshare.service;

import com.autoshare.dto.UserRequest;
import com.autoshare.dto.UserResponse;
import com.autoshare.dto.UserUpdateRequest;
import com.autoshare.dto.UserVerificationResponse;
import com.autoshare.exception.InvalidCampusEmailException;
import com.autoshare.exception.UserAlreadyExistsException;
import com.autoshare.exception.UserNotFoundException;
import com.autoshare.model.AccountStatus;
import com.autoshare.model.User;
import com.autoshare.model.UserRole;
import com.autoshare.repository.UserRepository;
import java.util.List;
import java.util.stream.Collectors;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * Service Implementation executing business logic and transactional CRUD for User records.
 *
 * AUTO-CONFIGURATION NOTE:
 * Spring Boot's component scan auto-detects @Service and creates a singleton Spring bean.
 * The @Transactional annotation ensures method execution takes place inside managed database
 * transactions configured by DataSourceTransactionManager.
 */
@Service
@Transactional
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final String campusEmailDomain;

    public UserServiceImpl(
            UserRepository userRepository,
            @Value("${autoshare.campus.email-domain:@srmist.edu.in}") String campusEmailDomain
    ) {
        this.userRepository = userRepository;
        this.campusEmailDomain = campusEmailDomain;
    }

    @Override
    @Transactional(readOnly = true)
    public List<UserResponse> getAllUsers() {
        return userRepository.findAll().stream()
                .map(UserResponse::fromEntity)
                .collect(Collectors.toList());
    }

    @Override
    @Transactional(readOnly = true)
    public UserResponse getUserById(Long id) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new UserNotFoundException("User record with ID " + id + " does not exist"));
        return UserResponse.fromEntity(user);
    }

    @Override
    @Transactional(readOnly = true)
    public UserResponse getUserByEmail(String email) {
        User user = userRepository.findByEmailIgnoreCase(email)
                .orElseThrow(() -> new UserNotFoundException("No user record registered with email: " + email));
        return UserResponse.fromEntity(user);
    }

    @Override
    @Transactional(readOnly = true)
    public UserResponse getUserByRegistrationNumber(String registrationNumber) {
        User user = userRepository.findByRegistrationNumberIgnoreCase(registrationNumber)
                .orElseThrow(() -> new UserNotFoundException("No user record found with registration number: " + registrationNumber));
        return UserResponse.fromEntity(user);
    }

    @Override
    @Transactional(readOnly = true)
    public List<UserResponse> searchUsers(String query) {
        if (query == null || query.trim().isEmpty()) {
            return getAllUsers();
        }
        return userRepository.searchUsers(query.trim()).stream()
                .map(UserResponse::fromEntity)
                .collect(Collectors.toList());
    }

    @Override
    @Transactional(readOnly = true)
    public List<UserResponse> getUsersByDepartment(String department) {
        return userRepository.findByDepartmentIgnoreCase(department).stream()
                .map(UserResponse::fromEntity)
                .collect(Collectors.toList());
    }

    @Override
    @Transactional(readOnly = true)
    public List<UserResponse> getUsersByRole(UserRole role) {
        return userRepository.findByRole(role).stream()
                .map(UserResponse::fromEntity)
                .collect(Collectors.toList());
    }

    @Override
    public UserResponse createUser(UserRequest request) {
        String cleanEmail = request.getEmail().trim().toLowerCase();
        String cleanRegNo = request.getRegistrationNumber().trim().toUpperCase();

        // Rule 1: Validate Institutional Campus Email Domain
        if (!cleanEmail.endsWith(campusEmailDomain)) {
            throw new InvalidCampusEmailException(
                    "Only institutional emails ending with " + campusEmailDomain + " are permitted for campus user registration"
            );
        }

        // Rule 2: Prevent Duplicate Email Registration
        if (userRepository.existsByEmailIgnoreCase(cleanEmail)) {
            throw new UserAlreadyExistsException("A user record with email " + cleanEmail + " is already registered");
        }

        // Rule 3: Prevent Duplicate Registration Number
        if (userRepository.existsByRegistrationNumberIgnoreCase(cleanRegNo)) {
            throw new UserAlreadyExistsException("A student/faculty record with Reg.No " + cleanRegNo + " already exists");
        }

        User user = new User(
                request.getFullName().trim(),
                cleanEmail,
                cleanRegNo,
                request.getPhoneNumber().trim(),
                request.getDepartment().trim(),
                request.getRole(),
                AccountStatus.ACTIVE,
                request.getCampusGate(),
                request.getHostelOrPG()
        );

        User savedUser = userRepository.save(user);
        return UserResponse.fromEntity(savedUser);
    }

    @Override
    public UserResponse updateUser(Long id, UserUpdateRequest request) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new UserNotFoundException("User record with ID " + id + " does not exist"));

        if (request.getFullName() != null && !request.getFullName().trim().isEmpty()) {
            user.setFullName(request.getFullName().trim());
        }
        if (request.getPhoneNumber() != null && !request.getPhoneNumber().trim().isEmpty()) {
            user.setPhoneNumber(request.getPhoneNumber().trim());
        }
        if (request.getDepartment() != null && !request.getDepartment().trim().isEmpty()) {
            user.setDepartment(request.getDepartment().trim());
        }
        if (request.getRole() != null) {
            user.setRole(request.getRole());
        }
        if (request.getStatus() != null) {
            user.setStatus(request.getStatus());
        }
        if (request.getCampusGate() != null) {
            user.setCampusGate(request.getCampusGate());
        }
        if (request.getHostelOrPG() != null) {
            user.setHostelOrPG(request.getHostelOrPG());
        }

        User updatedUser = userRepository.save(user);
        return UserResponse.fromEntity(updatedUser);
    }

    @Override
    public UserResponse updateStatus(Long id, AccountStatus status) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new UserNotFoundException("User record with ID " + id + " does not exist"));
        user.setStatus(status);
        User updatedUser = userRepository.save(user);
        return UserResponse.fromEntity(updatedUser);
    }

    @Override
    public void deleteUser(Long id) {
        if (!userRepository.existsById(id)) {
            throw new UserNotFoundException("User record with ID " + id + " does not exist");
        }
        userRepository.deleteById(id);
    }

    @Override
    @Transactional(readOnly = true)
    public UserVerificationResponse verifyUserForRide(String email) {
        return userRepository.findByEmailIgnoreCase(email)
                .map(u -> {
                    boolean active = u.getStatus() == AccountStatus.ACTIVE || u.getStatus() == AccountStatus.VERIFIED;
                    return new UserVerificationResponse(
                            true,
                            u.getEmail(),
                            u.getRegistrationNumber(),
                            u.getFullName(),
                            u.getRole(),
                            u.getStatus(),
                            active,
                            active ? "User verified and authorized for campus ride-sharing" : "Account is suspended or pending KYC"
                    );
                })
                .orElseGet(() -> new UserVerificationResponse(
                        false,
                        email,
                        null,
                        null,
                        null,
                        null,
                        false,
                        "User not found in institutional directory"
                ));
    }

    @Override
    @Transactional(readOnly = true)
    public long getUserCount() {
        return userRepository.count();
    }
}
