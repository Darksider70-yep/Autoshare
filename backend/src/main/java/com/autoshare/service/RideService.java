package com.autoshare.service;

import com.autoshare.dto.BookingRequest;
import com.autoshare.dto.BookingResponse;
import com.autoshare.dto.FareSplitResponse;
import com.autoshare.dto.RideRequest;
import com.autoshare.dto.RideResponse;
import com.autoshare.exception.DuplicateBookingException;
import com.autoshare.exception.InvalidCampusEmailException;
import com.autoshare.exception.RideFullException;
import com.autoshare.exception.RideNotFoundException;
import com.autoshare.model.Booking;
import com.autoshare.model.Ride;
import com.autoshare.model.RideStatus;
import com.autoshare.repository.BookingRepository;
import com.autoshare.repository.RideRepository;
import java.time.LocalDateTime;
import java.util.List;
import java.util.stream.Collectors;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * Business Layer: Encapsulates all domain business rules for rides.
 * Uses constructor injection (no field @Autowired) for loose coupling and testability.
 */
@Service
public class RideService {

    private final RideRepository rideRepository;
    private final BookingRepository bookingRepository;
    private final String campusEmailDomain;

    // Constructor Injection (Spring Boot automatically injects matching Spring Beans)
    public RideService(RideRepository rideRepository,
                       BookingRepository bookingRepository,
                       @Value("${autoshare.campus.email-domain:@srmist.edu.in}") String campusEmailDomain) {
        this.rideRepository = rideRepository;
        this.bookingRepository = bookingRepository;
        this.campusEmailDomain = campusEmailDomain;
    }

    @Transactional(readOnly = true)
    public List<RideResponse> getAllRides(String pickup, String destination) {
        List<Ride> rides;
        if (pickup != null && !pickup.isBlank() && destination != null && !destination.isBlank()) {
            rides = rideRepository.findByPickupGateContainingIgnoreCaseAndDestinationContainingIgnoreCase(pickup.trim(), destination.trim());
        } else if (pickup != null && !pickup.isBlank()) {
            rides = rideRepository.findByPickupGateContainingIgnoreCase(pickup.trim());
        } else if (destination != null && !destination.isBlank()) {
            rides = rideRepository.findByDestinationContainingIgnoreCase(destination.trim());
        } else {
            rides = rideRepository.findAll();
        }
        return rides.stream().map(this::mapToResponse).collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public RideResponse getRideById(Long id) {
        Ride ride = rideRepository.findById(id)
                .orElseThrow(() -> new RideNotFoundException(id));
        return mapToResponse(ride);
    }

    @Transactional
    public RideResponse createRide(RideRequest request) {
        // Business Rule 4: Departure time must be in the future
        if (request.getDepartureTime().isBefore(LocalDateTime.now())) {
            throw new IllegalArgumentException("Ride departure time must be in the future.");
        }

        Ride ride = new Ride(
                request.getHostName().trim(),
                request.getPickupGate().trim(),
                request.getDestination().trim(),
                request.getDepartureTime(),
                request.getTotalFare(),
                request.getTotalSeats()
        );

        Ride savedRide = rideRepository.save(ride);
        return mapToResponse(savedRide);
    }

    @Transactional
    public RideResponse bookSeat(Long rideId, BookingRequest request) {
        // Find existing ride or fail with 404
        Ride ride = rideRepository.findById(rideId)
                .orElseThrow(() -> new RideNotFoundException(rideId));

        String email = request.getStudentEmail().trim().toLowerCase();

        // Business Rule 5: Only campus domain emails are authorized to book
        if (!email.endsWith(this.campusEmailDomain.toLowerCase())) {
            throw new InvalidCampusEmailException(email, this.campusEmailDomain);
        }

        // Business Rule 1: A student cannot join a ride that is already FULL
        if (ride.getStatus() == RideStatus.FULL || ride.getSeatsTaken() >= ride.getTotalSeats()) {
            throw new RideFullException(rideId);
        }

        // Business Rule 2: The same student email cannot book the same ride twice
        if (bookingRepository.existsByRideIdAndStudentEmailIgnoreCase(rideId, email)) {
            throw new DuplicateBookingException(email, rideId);
        }

        // Create booking and attach to ride (Business Rule 3 & 6 handled inside entity: seatsTaken++ & status update)
        Booking booking = new Booking(ride, request.getStudentName().trim(), email);
        ride.addBooking(booking);
        bookingRepository.save(booking);

        Ride updatedRide = rideRepository.save(ride);
        return mapToResponse(updatedRide);
    }

    @Transactional(readOnly = true)
    public FareSplitResponse calculateFareSplit(Long rideId) {
        Ride ride = rideRepository.findById(rideId)
                .orElseThrow(() -> new RideNotFoundException(rideId));

        int totalRiders = ride.getSeatsTaken() + 1; // Co-passengers + 1 host
        double farePerPerson = ride.calculateFarePerPerson();

        return new FareSplitResponse(
                ride.getId(),
                ride.getDestination(),
                ride.getTotalFare(),
                totalRiders,
                farePerPerson
        );
    }

    // Helper mapping method: Entity -> DTO
    public RideResponse mapToResponse(Ride ride) {
        int seatsAvailable = Math.max(0, ride.getTotalSeats() - ride.getSeatsTaken());
        double farePerPerson = ride.calculateFarePerPerson();

        List<BookingResponse> bookingResponses = ride.getBookings() != null
                ? ride.getBookings().stream()
                .map(b -> new BookingResponse(b.getId(), b.getStudentName(), b.getStudentEmail(), b.getBookedAt()))
                .collect(Collectors.toList())
                : List.of();

        return new RideResponse(
                ride.getId(),
                ride.getHostName(),
                ride.getPickupGate(),
                ride.getDestination(),
                ride.getDepartureTime(),
                ride.getTotalFare(),
                ride.getTotalSeats(),
                ride.getSeatsTaken(),
                seatsAvailable,
                farePerPerson,
                ride.getStatus(),
                bookingResponses
        );
    }
}
