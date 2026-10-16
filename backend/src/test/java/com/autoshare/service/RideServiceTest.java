package com.autoshare.service;

import com.autoshare.dto.BookingRequest;
import com.autoshare.dto.FareSplitResponse;
import com.autoshare.dto.RideResponse;
import com.autoshare.exception.DuplicateBookingException;
import com.autoshare.exception.InvalidCampusEmailException;
import com.autoshare.exception.RideFullException;
import com.autoshare.model.Ride;
import com.autoshare.model.RideStatus;
import com.autoshare.repository.BookingRepository;
import com.autoshare.repository.RideRepository;
import java.time.LocalDateTime;
import java.util.Optional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyLong;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

/**
 * Unit tests for RideService business rules using JUnit 5 and Mockito.
 */
@ExtendWith(MockitoExtension.class)
class RideServiceTest {

    @Mock
    private RideRepository rideRepository;

    @Mock
    private BookingRepository bookingRepository;

    private RideService rideService;

    private final String campusDomain = "@srmist.edu.in";

    @BeforeEach
    void setUp() {
        rideService = new RideService(rideRepository, bookingRepository, campusDomain);
    }

    @Test
    @DisplayName("Business Rule 3: Dynamic Fare Split is accurately recalculated per rider")
    void testFareSplitCalculation() {
        // Given: Total fare ₹120, 1 seat taken -> 2 total people (1 host + 1 passenger)
        Ride ride = new Ride("Aarav", "Gate 1", "Starlight Hostels", LocalDateTime.now().plusHours(1), 120.0, 3);
        ride.setId(1L);
        ride.setSeatsTaken(1);

        when(rideRepository.findById(1L)).thenReturn(Optional.of(ride));

        // When: Calculate fare split
        FareSplitResponse response = rideService.calculateFareSplit(1L);

        // Then: 120 / 2 = ₹60.0 per person
        assertNotNull(response);
        assertEquals(2, response.getTotalRiders());
        assertEquals(60.0, response.getFarePerPerson());
    }

    @Test
    @DisplayName("Business Rule 1: Attempting to book a FULL ride throws RideFullException (HTTP 409)")
    void testBookSeat_FullRideRejection() {
        // Given: A ride where totalSeats = 3 and seatsTaken = 3 (status FULL)
        Ride ride = new Ride("Ishaan", "Gate 2", "Royal Residency", LocalDateTime.now().plusHours(1), 120.0, 3);
        ride.setId(4L);
        ride.setSeatsTaken(3);
        ride.setStatus(RideStatus.FULL);

        when(rideRepository.findById(4L)).thenReturn(Optional.of(ride));

        BookingRequest request = new BookingRequest("Daksh", "daksh.g@srmist.edu.in");

        // When / Then: Expect RideFullException
        assertThrows(RideFullException.class, () -> rideService.bookSeat(4L, request));
        verify(bookingRepository, never()).save(any());
    }

    @Test
    @DisplayName("Business Rule 2: Duplicate booking with the same email throws DuplicateBookingException (HTTP 409)")
    void testBookSeat_DuplicateBookingRejection() {
        // Given: An open ride, but email already exists in repository for this ride
        Ride ride = new Ride("Aarav", "Gate 1", "Starlight Hostels", LocalDateTime.now().plusHours(1), 120.0, 3);
        ride.setId(1L);
        ride.setSeatsTaken(1);

        when(rideRepository.findById(1L)).thenReturn(Optional.of(ride));
        when(bookingRepository.existsByRideIdAndStudentEmailIgnoreCase(1L, "priya.p@srmist.edu.in")).thenReturn(true);

        BookingRequest request = new BookingRequest("Priya Patel", "priya.p@srmist.edu.in");

        // When / Then: Expect DuplicateBookingException
        assertThrows(DuplicateBookingException.class, () -> rideService.bookSeat(1L, request));
        verify(bookingRepository, never()).save(any());
    }

    @Test
    @DisplayName("Business Rule 5: Non-campus email domain throws InvalidCampusEmailException (HTTP 400)")
    void testBookSeat_NonCampusEmailRejection() {
        // Given: An open ride
        Ride ride = new Ride("Aarav", "Gate 1", "Starlight Hostels", LocalDateTime.now().plusHours(1), 120.0, 3);
        ride.setId(1L);

        when(rideRepository.findById(1L)).thenReturn(Optional.of(ride));

        // When: Trying to book with a non-campus email (e.g., gmail.com)
        BookingRequest request = new BookingRequest("Stranger", "stranger@gmail.com");

        // Then: Expect InvalidCampusEmailException
        assertThrows(InvalidCampusEmailException.class, () -> rideService.bookSeat(1L, request));
        verify(bookingRepository, never()).save(any());
    }

    @Test
    @DisplayName("Successful Seat Claim updates seats taken and recalculates fare")
    void testBookSeat_Success() {
        // Given: Ride with 0 seats taken, total seats 3, fare 120
        Ride ride = new Ride("Aarav", "Gate 1", "Starlight Hostels", LocalDateTime.now().plusHours(1), 120.0, 3);
        ride.setId(1L);

        when(rideRepository.findById(1L)).thenReturn(Optional.of(ride));
        when(bookingRepository.existsByRideIdAndStudentEmailIgnoreCase(anyLong(), anyString())).thenReturn(false);
        when(rideRepository.save(any(Ride.class))).thenAnswer(invocation -> invocation.getArgument(0));

        BookingRequest request = new BookingRequest("Daksh", "daksh.g@srmist.edu.in");

        // When: Seat is booked
        RideResponse response = rideService.bookSeat(1L, request);

        // Then: seatsTaken becomes 1, seatsAvailable becomes 2, farePerPerson = 120 / 2 = 60.0
        assertNotNull(response);
        assertEquals(1, response.getSeatsTaken());
        assertEquals(2, response.getSeatsAvailable());
        assertEquals(60.0, response.getFarePerPerson());
        assertEquals(RideStatus.OPEN, response.getStatus());
    }
}
