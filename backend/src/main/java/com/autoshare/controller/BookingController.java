package com.autoshare.controller;

import com.autoshare.dto.BookingResponse;
import com.autoshare.service.BookingService;
import java.util.List;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Presentation Layer: REST Controller for seat booking inquiries.
 */
@RestController
@RequestMapping("/api/bookings")
public class BookingController {

    private final BookingService bookingService;

    public BookingController(BookingService bookingService) {
        this.bookingService = bookingService;
    }

    /**
     * GET /api/bookings/ride/{rideId} - List all student bookings for a given ride.
     */
    @GetMapping("/ride/{rideId}")
    public ResponseEntity<List<BookingResponse>> getBookingsForRide(@PathVariable Long rideId) {
        List<BookingResponse> bookings = bookingService.getBookingsForRide(rideId);
        return ResponseEntity.ok(bookings);
    }
}
