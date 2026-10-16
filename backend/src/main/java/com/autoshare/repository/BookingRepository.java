package com.autoshare.repository;

import com.autoshare.model.Booking;
import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Data Access Layer for Booking entities.
 * Automatically implemented by Spring Data JPA runtime proxies.
 */
@Repository
public interface BookingRepository extends JpaRepository<Booking, Long> {

    // Derived query method to enforce business rule: prevent duplicate bookings
    boolean existsByRideIdAndStudentEmailIgnoreCase(Long rideId, String studentEmail);

    List<Booking> findByRideId(Long rideId);
}
