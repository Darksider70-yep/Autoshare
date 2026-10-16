package com.autoshare.service;

import com.autoshare.dto.BookingResponse;
import com.autoshare.exception.RideNotFoundException;
import com.autoshare.model.Booking;
import com.autoshare.repository.BookingRepository;
import com.autoshare.repository.RideRepository;
import java.util.List;
import java.util.stream.Collectors;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * Business Layer: Manages seat reservation inquiries.
 */
@Service
public class BookingService {

    private final BookingRepository bookingRepository;
    private final RideRepository rideRepository;

    public BookingService(BookingRepository bookingRepository, RideRepository rideRepository) {
        this.bookingRepository = bookingRepository;
        this.rideRepository = rideRepository;
    }

    @Transactional(readOnly = true)
    public List<BookingResponse> getBookingsForRide(Long rideId) {
        if (!rideRepository.existsById(rideId)) {
            throw new RideNotFoundException(rideId);
        }
        return bookingRepository.findByRideId(rideId)
                .stream()
                .map(this::mapToResponse)
                .collect(Collectors.toList());
    }

    private BookingResponse mapToResponse(Booking booking) {
        return new BookingResponse(
                booking.getId(),
                booking.getStudentName(),
                booking.getStudentEmail(),
                booking.getBookedAt()
        );
    }
}
