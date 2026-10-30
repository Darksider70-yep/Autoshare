package com.autoshare.controller;

import com.autoshare.dto.UserRequest;
import com.autoshare.dto.UserResponse;
import com.autoshare.dto.UserVerificationResponse;
import com.autoshare.model.AccountStatus;
import com.autoshare.model.UserRole;
import com.autoshare.service.UserService;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.time.LocalDateTime;
import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.hamcrest.Matchers.hasSize;
import static org.hamcrest.Matchers.is;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

/**
 * Unit 5 WebMvcTest for UserController verifying REST API contracts and HTTP statuses.
 */
@WebMvcTest(UserController.class)
class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @MockBean
    private UserService userService;

    private UserResponse createSampleResponse() {
        UserResponse res = new UserResponse();
        res.setId(1L);
        res.setFullName("Daksh Gehlot");
        res.setEmail("daksh.g@srmist.edu.in");
        res.setRegistrationNumber("RA2411003012297");
        res.setPhoneNumber("9876543210");
        res.setDepartment("Computer Science & Engineering");
        res.setRole(UserRole.STUDENT_COMMUTER);
        res.setStatus(AccountStatus.VERIFIED);
        res.setCampusGate("Campus Gate 2");
        res.setHostelOrPG("Starlight Hostels");
        res.setRating(5.0);
        res.setTotalRidesCount(12);
        res.setCreatedAt(LocalDateTime.now());
        res.setUpdatedAt(LocalDateTime.now());
        return res;
    }

    @Test
    @DisplayName("GET /api/users returns HTTP 200 and list of user records")
    void testGetAllUsers_Returns200() throws Exception {
        when(userService.getAllUsers()).thenReturn(List.of(createSampleResponse()));

        mockMvc.perform(get("/api/users"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$", hasSize(1)))
                .andExpect(jsonPath("$[0].fullName", is("Daksh Gehlot")))
                .andExpect(jsonPath("$[0].registrationNumber", is("RA2411003012297")));
    }

    @Test
    @DisplayName("GET /api/users/1 returns HTTP 200 and single user profile")
    void testGetUserById_Returns200() throws Exception {
        when(userService.getUserById(1L)).thenReturn(createSampleResponse());

        mockMvc.perform(get("/api/users/1"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id", is(1)))
                .andExpect(jsonPath("$.email", is("daksh.g@srmist.edu.in")));
    }

    @Test
    @DisplayName("POST /api/users with valid student DTO returns HTTP 201 Created")
    void testCreateUser_ValidInput_Returns201() throws Exception {
        UserRequest req = new UserRequest(
                "Daksh Gehlot",
                "daksh.g@srmist.edu.in",
                "RA2411003012297",
                "9876543210",
                "Computer Science & Engineering",
                UserRole.STUDENT_COMMUTER,
                "Campus Gate 2",
                "Starlight Hostels"
        );

        when(userService.createUser(any(UserRequest.class))).thenReturn(createSampleResponse());

        mockMvc.perform(post("/api/users")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.fullName", is("Daksh Gehlot")))
                .andExpect(jsonPath("$.registrationNumber", is("RA2411003012297")));
    }

    @Test
    @DisplayName("POST /api/users with blank name returns HTTP 400 Bad Request")
    void testCreateUser_BlankName_Returns400() throws Exception {
        UserRequest invalidReq = new UserRequest(
                "",
                "daksh.g@srmist.edu.in",
                "RA2411003012297",
                "9876543210",
                "Computer Science & Engineering",
                UserRole.STUDENT_COMMUTER,
                "Campus Gate 2",
                "Starlight Hostels"
        );

        mockMvc.perform(post("/api/users")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(invalidReq)))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("DELETE /api/users/1 returns HTTP 200 with confirmation")
    void testDeleteUser_Returns200() throws Exception {
        doNothing().when(userService).deleteUser(1L);

        mockMvc.perform(delete("/api/users/1"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.deleted", is(true)))
                .andExpect(jsonPath("$.userId", is(1)));
    }

    @Test
    @DisplayName("GET /api/users/verify/{email} returns inter-service verification result")
    void testVerifyUser_Returns200() throws Exception {
        UserVerificationResponse verification = new UserVerificationResponse(
                true,
                "daksh.g@srmist.edu.in",
                "RA2411003012297",
                "Daksh Gehlot",
                UserRole.STUDENT_COMMUTER,
                AccountStatus.VERIFIED,
                true,
                "User verified"
        );

        when(userService.verifyUserForRide("daksh.g@srmist.edu.in")).thenReturn(verification);

        mockMvc.perform(get("/api/users/verify/daksh.g@srmist.edu.in"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.verified", is(true)))
                .andExpect(jsonPath("$.eligibleToRide", is(true)));
    }
}
