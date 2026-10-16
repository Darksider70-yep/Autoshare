package com.autoshare.repository;

import com.autoshare.model.Ride;
import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Data Access Layer for Ride entities.
 * AUTO-CONFIGURATION NOTE: Spring Data JPA automatically generates dynamic proxy implementations
 * for JpaRepository methods (save, findById, findAll, delete) and derived query methods at runtime.
 * No manual JDBC boilerplate or DAO implementation class is required.
 */
@Repository
public interface RideRepository extends JpaRepository<Ride, Long> {

    List<Ride> findByPickupGateContainingIgnoreCaseAndDestinationContainingIgnoreCase(String pickupGate, String destination);

    List<Ride> findByPickupGateContainingIgnoreCase(String pickupGate);

    List<Ride> findByDestinationContainingIgnoreCase(String destination);
}
