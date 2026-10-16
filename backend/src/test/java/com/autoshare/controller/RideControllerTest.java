package com.autoshare.controller;

import com.autoshare.dto.RideResponse;
import com.autoshare.model.RideStatus;
import com.autoshare.service.RideService;
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
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

/**
 * Presentation Layer MockMvc tests for RideController using @WebMvcTest.
 * AUTO-CONFIGURATION NOTE: @WebMvcTest auto-configures Spring MVC infrastructure,
 * MockMvc, and Jackson converters while isolating the web layer from database beans.
 */
@WebMvcTest(RideController.class)
class RideControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @MockBean
    private RideService rideService;

    @Test
    @DisplayName("GET /api/rides returns HTTP 200 and JSON array")
    void testGetAllRides_Returns200AndJsonArray() throws Exception {
        RideResponse mockRide = new RideResponse(
                1L,
                "Aarav Sharma",
                "Campus Gate 2",
                "Starlight Hostels",
                LocalDateTime.now().plusHours(2),
                120.0,
                3,
                1,
                2,
                60.0,
                RideStatus.OPEN,
                List.of()
        );

        when(rideService.getAllRides(null, null)).thenReturn(List.of(mockRide));

        mockMvc.perform(get("/api/rides"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$", hasSize(1)))
                .andExpect(jsonPath("$[0].id", is(1)))
                .andExpect(jsonPath("$[0].hostName", is("Aarav Sharma")))
                .andExpect(jsonPath("$[0].destination", is("Starlight Hostels")))
                .andExpect(jsonPath("$[0].farePerPerson", is(60.0)));
    }

    @Test
    @DisplayName("POST /api/rides with invalid body returns HTTP 400 Bad Request")
    void testCreateRide_WithInvalidBody_Returns400() throws Exception {
        // Invalid request payload: Missing hostName, past departureTime, empty destination
        String invalidJson = """
                {
                    "hostName": "",
                    "pickupGate": "",
                    "destination": "",
                    "departureTime": "2020-01-01T10:00:00",
                    "totalFare": 0,
                    "totalSeats": 5
                }
                """;

        mockMvc.perform(post("/api/rides")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(invalidJson))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.status", is(400)))
                .andExpect(jsonPath("$.error", is("Bad Request")));
    }
}
