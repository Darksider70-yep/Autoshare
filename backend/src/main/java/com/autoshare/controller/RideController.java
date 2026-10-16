package com.autoshare.controller;

import com.autoshare.dto.BookingRequest;
import com.autoshare.dto.FareSplitResponse;
import com.autoshare.dto.RideRequest;
import com.autoshare.dto.RideResponse;
import com.autoshare.service.RideService;
import jakarta.validation.Valid;
import java.net.URI;
import java.util.List;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Presentation Layer: REST Controller exposing HTTP endpoints for TukTuk rides.
 * AUTO-CONFIGURATION NOTE: Spring Boot's DispatcherServlet routes HTTP requests here.
 * Jackson auto-serializes request/response bodies between Java objects and JSON.
 * Controller strictly delegates all business rules to RideService.
 */
@RestController
@RequestMapping("/api/rides")
public class RideController {

    private final RideService rideService;

    // Constructor Injection (Spring Boot auto-injects RideService bean)
    public RideController(RideService rideService) {
        this.rideService = rideService;
    }

    /**
     * GET /api/rides - List all ride offers with optional pickup/destination filtering.
     */
    @GetMapping
    public ResponseEntity<List<RideResponse>> getAllRides(
            @RequestParam(required = false) String pickup,
            @RequestParam(required = false) String destination) {
        List<RideResponse> rides = rideService.getAllRides(pickup, destination);
        return ResponseEntity.ok(rides);
    }

    /**
     * GET /api/rides/{id} - Retrieve detailed information for a single ride.
     */
    @GetMapping("/{id}")
    public ResponseEntity<RideResponse> getRideById(@PathVariable Long id) {
        RideResponse ride = rideService.getRideById(id);
        return ResponseEntity.ok(ride);
    }

    /**
     * POST /api/rides - Publish a new ride offer with Bean Validation.
     */
    @PostMapping
    public ResponseEntity<RideResponse> createRide(@Valid @RequestBody RideRequest request) {
        RideResponse created = rideService.createRide(request);
        return ResponseEntity
                .created(URI.create("/api/rides/" + created.getId()))
                .body(created);
    }

    /**
     * POST /api/rides/{id}/book - Reserve a seat on a ride.
     */
    @PostMapping("/{id}/book")
    public ResponseEntity<RideResponse> bookSeat(
            @PathVariable Long id,
            @Valid @RequestBody BookingRequest request) {
        RideResponse updatedRide = rideService.bookSeat(id, request);
        return ResponseEntity.status(HttpStatus.CREATED).body(updatedRide);
    }

    /**
     * GET /api/rides/{id}/fare-split - Retrieve dynamic per-student fare calculation.
     */
    @GetMapping("/{id}/fare-split")
    public ResponseEntity<FareSplitResponse> getFareSplit(@PathVariable Long id) {
        FareSplitResponse fareSplit = rideService.calculateFareSplit(id);
        return ResponseEntity.ok(fareSplit);
    }
}
