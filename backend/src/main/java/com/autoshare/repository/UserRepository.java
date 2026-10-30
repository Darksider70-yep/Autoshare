package com.autoshare.repository;

import com.autoshare.model.AccountStatus;
import com.autoshare.model.User;
import com.autoshare.model.UserRole;
import java.util.List;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

/**
 * Spring Data JPA Repository interface for User entities.
 *
 * AUTO-CONFIGURATION NOTE:
 * Spring Data JPA auto-configuration scans for interfaces extending JpaRepository
 * and automatically synthesizes proxy implementations backed by Hibernate EntityManager.
 * It translates both method name conventions and @Query JPQL statements into native SQL queries.
 */
@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByEmailIgnoreCase(String email);

    Optional<User> findByRegistrationNumberIgnoreCase(String registrationNumber);

    List<User> findByRole(UserRole role);

    List<User> findByDepartmentIgnoreCase(String department);

    List<User> findByStatus(AccountStatus status);

    boolean existsByEmailIgnoreCase(String email);

    boolean existsByRegistrationNumberIgnoreCase(String registrationNumber);

    /**
     * Custom JPQL query for full-text search across name, email, registration number, and department.
     */
    @Query("SELECT u FROM User u WHERE " +
           "LOWER(u.fullName) LIKE LOWER(CONCAT('%', :query, '%')) OR " +
           "LOWER(u.email) LIKE LOWER(CONCAT('%', :query, '%')) OR " +
           "LOWER(u.registrationNumber) LIKE LOWER(CONCAT('%', :query, '%')) OR " +
           "LOWER(u.department) LIKE LOWER(CONCAT('%', :query, '%')) " +
           "ORDER BY u.id ASC")
    List<User> searchUsers(@Param("query") String query);

    /**
     * Find active users in a specific department and gate cluster.
     */
    List<User> findByCampusGateIgnoreCaseAndStatus(String campusGate, AccountStatus status);
}
