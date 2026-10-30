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
import java.util.Optional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

/**
 * Unit 5 Service Layer tests for UserService business rules and CRUD logic using JUnit 5 & Mockito.
 */
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    private UserService userService;

    private final String campusDomain = "@srmist.edu.in";

    @BeforeEach
    void setUp() {
        userService = new UserServiceImpl(userRepository, campusDomain);
    }

    @Test
    @DisplayName("Create User: Success persists new student entity and returns DTO")
    void testCreateUser_Success() {
        UserRequest request = new UserRequest(
                "Daksh Gehlot",
                "daksh.g@srmist.edu.in",
                "RA2411003012297",
                "9876543210",
                "Computer Science & Engineering",
                UserRole.STUDENT_COMMUTER,
                "Campus Gate 2",
                "Starlight Hostels"
        );

        when(userRepository.existsByEmailIgnoreCase(anyString())).thenReturn(false);
        when(userRepository.existsByRegistrationNumberIgnoreCase(anyString())).thenReturn(false);

        User savedEntity = new User(
                "Daksh Gehlot",
                "daksh.g@srmist.edu.in",
                "RA2411003012297",
                "9876543210",
                "Computer Science & Engineering",
                UserRole.STUDENT_COMMUTER,
                AccountStatus.ACTIVE,
                "Campus Gate 2",
                "Starlight Hostels"
        );
        savedEntity.setId(1L);

        when(userRepository.save(any(User.class))).thenReturn(savedEntity);

        UserResponse response = userService.createUser(request);

        assertNotNull(response);
        assertEquals("Daksh Gehlot", response.getFullName());
        assertEquals("RA2411003012297", response.getRegistrationNumber());
        assertEquals("daksh.g@srmist.edu.in", response.getEmail());
    }

    @Test
    @DisplayName("Create User: Non-institutional email triggers InvalidCampusEmailException")
    void testCreateUser_InvalidCampusEmail_ThrowsException() {
        UserRequest request = new UserRequest(
                "External Student",
                "random.student@gmail.com",
                "RA2411003019999",
                "9876543210",
                "Computer Science & Engineering",
                UserRole.STUDENT_COMMUTER,
                "Campus Gate 1",
                "City Apartments"
        );

        assertThrows(InvalidCampusEmailException.class, () -> userService.createUser(request));
    }

    @Test
    @DisplayName("Create User: Duplicate institutional email throws UserAlreadyExistsException")
    void testCreateUser_DuplicateEmail_ThrowsException() {
        UserRequest request = new UserRequest(
                "Daksh Gehlot",
                "daksh.g@srmist.edu.in",
                "RA2411003012297",
                "9876543210",
                "Computer Science & Engineering",
                UserRole.STUDENT_COMMUTER,
                "Campus Gate 2",
                "Starlight Hostels"
        );

        when(userRepository.existsByEmailIgnoreCase("daksh.g@srmist.edu.in")).thenReturn(true);

        assertThrows(UserAlreadyExistsException.class, () -> userService.createUser(request));
    }

    @Test
    @DisplayName("Create User: Duplicate registration number throws UserAlreadyExistsException")
    void testCreateUser_DuplicateRegNo_ThrowsException() {
        UserRequest request = new UserRequest(
                "Other Student",
                "other.s@srmist.edu.in",
                "RA2411003012297",
                "9876543210",
                "Computer Science & Engineering",
                UserRole.STUDENT_COMMUTER,
                "Campus Gate 2",
                "Starlight Hostels"
        );

        when(userRepository.existsByEmailIgnoreCase("other.s@srmist.edu.in")).thenReturn(false);
        when(userRepository.existsByRegistrationNumberIgnoreCase("RA2411003012297")).thenReturn(true);

        assertThrows(UserAlreadyExistsException.class, () -> userService.createUser(request));
    }

    @Test
    @DisplayName("Update User: Updates fields and persists updated entity")
    void testUpdateUser_Success() {
        User existing = new User(
                "Daksh Gehlot",
                "daksh.g@srmist.edu.in",
                "RA2411003012297",
                "9876543210",
                "Computer Science & Engineering",
                UserRole.STUDENT_COMMUTER,
                AccountStatus.ACTIVE,
                "Campus Gate 2",
                "Starlight Hostels"
        );
        existing.setId(1L);

        when(userRepository.findById(1L)).thenReturn(Optional.of(existing));
        when(userRepository.save(any(User.class))).thenAnswer(invocation -> invocation.getArgument(0));

        UserUpdateRequest updateReq = new UserUpdateRequest();
        updateReq.setPhoneNumber("9998887776");
        updateReq.setStatus(AccountStatus.VERIFIED);

        UserResponse result = userService.updateUser(1L, updateReq);

        assertNotNull(result);
        assertEquals("9998887776", result.getPhoneNumber());
        assertEquals(AccountStatus.VERIFIED, result.getStatus());
    }

    @Test
    @DisplayName("Delete User: Successfully calls repository deleteById when user exists")
    void testDeleteUser_Success() {
        when(userRepository.existsById(1L)).thenReturn(true);

        userService.deleteUser(1L);

        verify(userRepository).deleteById(1L);
    }

    @Test
    @DisplayName("Delete User: Throws UserNotFoundException when user does not exist")
    void testDeleteUser_NotFound_ThrowsException() {
        when(userRepository.existsById(99L)).thenReturn(false);

        assertThrows(UserNotFoundException.class, () -> userService.deleteUser(99L));
    }

    @Test
    @DisplayName("Microservice Verification: Active verified user is marked eligible for rides")
    void testVerifyUserForRide_ActiveStudent() {
        User activeUser = new User(
                "Daksh Gehlot",
                "daksh.g@srmist.edu.in",
                "RA2411003012297",
                "9876543210",
                "Computer Science & Engineering",
                UserRole.STUDENT_COMMUTER,
                AccountStatus.VERIFIED,
                "Campus Gate 2",
                "Starlight Hostels"
        );

        when(userRepository.findByEmailIgnoreCase("daksh.g@srmist.edu.in")).thenReturn(Optional.of(activeUser));

        UserVerificationResponse verification = userService.verifyUserForRide("daksh.g@srmist.edu.in");

        assertTrue(verification.isVerified());
        assertTrue(verification.isEligibleToRide());
    }

    @Test
    @DisplayName("Microservice Verification: Suspended account is marked not eligible for rides")
    void testVerifyUserForRide_SuspendedUser() {
        User suspendedUser = new User(
                "Suspended Commuter",
                "suspended@srmist.edu.in",
                "RA2411003012999",
                "9876543210",
                "Computer Science & Engineering",
                UserRole.STUDENT_COMMUTER,
                AccountStatus.SUSPENDED,
                "Campus Gate 1",
                "Hostel A"
        );

        when(userRepository.findByEmailIgnoreCase("suspended@srmist.edu.in")).thenReturn(Optional.of(suspendedUser));

        UserVerificationResponse verification = userService.verifyUserForRide("suspended@srmist.edu.in");

        assertTrue(verification.isVerified());
        assertFalse(verification.isEligibleToRide());
    }
}
