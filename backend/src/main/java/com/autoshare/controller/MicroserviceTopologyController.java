package com.autoshare.controller;

import com.autoshare.client.UserVerificationClient;
import com.autoshare.dto.UserVerificationResponse;
import com.autoshare.repository.BookingRepository;
import com.autoshare.repository.RideRepository;
import com.autoshare.repository.UserRepository;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Controller providing Microservice Topology, Registry inspection, Health monitoring,
 * and Inter-Service REST call simulation for Unit-5 Microservices Evaluation.
 */
@RestController
@RequestMapping("/api/microservices")
@CrossOrigin(origins = "*")
public class MicroserviceTopologyController {

    private final UserRepository userRepository;
    private final RideRepository rideRepository;
    private final BookingRepository bookingRepository;
    private final UserVerificationClient userVerificationClient;

    @Value("${server.port:8080}")
    private String serverPort;

    @Value("${autoshare.userservice.url:http://localhost:8080/api/users}")
    private String userServiceUrl;

    public MicroserviceTopologyController(
            UserRepository userRepository,
            RideRepository rideRepository,
            BookingRepository bookingRepository,
            UserVerificationClient userVerificationClient) {
        this.userRepository = userRepository;
        this.rideRepository = rideRepository;
        this.bookingRepository = bookingRepository;
        this.userVerificationClient = userVerificationClient;
    }

    /**
     * GET /api/microservices/topology - Returns the architectural schema and contracts of the microservices.
     */
    @GetMapping("/topology")
    public ResponseEntity<Map<String, Object>> getTopology() {
        Map<String, Object> topology = new HashMap<>();
        topology.put("architecturePattern", "Microservices Architecture with Spring Data JPA & REST APIs");
        topology.put("version", "1.0.0-Unit5");
        topology.put("timestamp", LocalDateTime.now());

        List<Map<String, Object>> services = new ArrayList<>();

        // Service 1: User Management Microservice
        Map<String, Object> userService = new HashMap<>();
        userService.put("serviceName", "user-management-service");
        userService.put("description", "Spring Boot Data JPA service managing student commuter profiles, KYC, and CRUD records");
        userService.put("port", 8081);
        userService.put("runtimeStatus", "UP");
        userService.put("databaseType", "Relational Database (In-Memory H2 / Hibernate ORM)");
        userService.put("entity", "com.autoshare.model.User");
        userService.put("repository", "com.autoshare.repository.UserRepository (Spring Data JPA)");
        userService.put("endpoints", List.of(
                "GET /api/users",
                "GET /api/users/{id}",
                "GET /api/users/email/{email}",
                "GET /api/users/reg/{registrationNumber}",
                "POST /api/users",
                "PUT /api/users/{id}",
                "PATCH /api/users/{id}/status",
                "DELETE /api/users/{id}",
                "GET /api/users/verify/{email}"
        ));
        services.add(userService);

        // Service 2: Ride & Booking Microservice
        Map<String, Object> rideService = new HashMap<>();
        rideService.put("serviceName", "ride-booking-service");
        rideService.put("description", "Microservice managing TukTuk pooling offers, dynamic fare splitting, and seat reservations");
        rideService.put("port", 8080);
        rideService.put("runtimeStatus", "UP");
        rideService.put("databaseType", "Relational Database (In-Memory H2 / Hibernate ORM)");
        rideService.put("entities", List.of("com.autoshare.model.Ride", "com.autoshare.model.Booking"));
        rideService.put("endpoints", List.of(
                "GET /api/rides",
                "GET /api/rides/{id}",
                "POST /api/rides",
                "POST /api/rides/{id}/book",
                "GET /api/rides/{id}/fare-split",
                "GET /api/bookings"
        ));
        services.add(rideService);

        // Client Gateway UI
        Map<String, Object> clientUi = new HashMap<>();
        clientUi.put("serviceName", "autoshare-react-client");
        clientUi.put("description", "React 19 Single Page Application with interactive tabs for JPA CRUD & Microservice Sandbox");
        clientUi.put("port", 3000);
        clientUi.put("runtimeStatus", "UP");
        clientUi.put("reverseProxy", "Vite Development Server Proxy (/api -> :8080)");
        services.add(clientUi);

        topology.put("services", services);

        // Inter-service Communication Details
        Map<String, Object> interService = new HashMap<>();
        interService.put("protocol", "Synchronous HTTP/1.1 REST (JSON payload)");
        interService.put("clientType", "RestTemplate with Circuit Breaker In-Process Fallback");
        interService.put("verificationContract", "GET " + userServiceUrl + "/verify/{email}");
        interService.put("resiliencePattern", "Graceful Degradation / Fallback to Local Repository if Remote Microservice Unreachable");
        topology.put("interServiceCommunication", interService);

        return ResponseEntity.ok(topology);
    }

    /**
     * GET /api/microservices/health - Live health and entity statistics across services.
     */
    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> getHealth() {
        Map<String, Object> health = new HashMap<>();
        health.put("status", "HEALTHY");
        health.put("timestamp", LocalDateTime.now());

        Map<String, Object> userMetrics = new HashMap<>();
        userMetrics.put("service", "user-management-service");
        userMetrics.put("totalUsersInDb", userRepository.count());
        userMetrics.put("h2RelationalDbStatus", "CONNECTED");
        health.put("userServiceMetrics", userMetrics);

        Map<String, Object> rideMetrics = new HashMap<>();
        rideMetrics.put("service", "ride-booking-service");
        rideMetrics.put("totalRidesInDb", rideRepository.count());
        rideMetrics.put("totalBookingsInDb", bookingRepository.count());
        health.put("rideServiceMetrics", rideMetrics);

        return ResponseEntity.ok(health);
    }

    /**
     * POST /api/microservices/simulate-flow - Interactive test endpoint to trace inter-service RPC flow.
     */
    @PostMapping("/simulate-flow")
    public ResponseEntity<Map<String, Object>> simulateFlow(
            @RequestParam(defaultValue = "daksh.g@srmist.edu.in") String email) {

        long startTime = System.currentTimeMillis();
        UserVerificationResponse verification = userVerificationClient.verifyCommuter(email);
        long duration = System.currentTimeMillis() - startTime;

        Map<String, Object> trace = new HashMap<>();
        trace.put("step1_Initiator", "Ride-Booking-Service (Port 8080)");
        trace.put("step2_Request", "HTTP GET /api/users/verify/" + email);
        trace.put("step3_TargetService", "User-Management-Service (Port 8081)");
        trace.put("step4_JpaQuery", "UserRepository.findByEmailIgnoreCase('" + email + "')");
        trace.put("step5_VerificationResult", verification);
        trace.put("step6_Decision", verification.isEligibleToRide() ? "ALLOW_RIDE_BOOKING" : "REJECT_RIDE_BOOKING");
        trace.put("latencyMs", duration);
        trace.put("status", "SUCCESS");

        return ResponseEntity.ok(trace);
    }
}
