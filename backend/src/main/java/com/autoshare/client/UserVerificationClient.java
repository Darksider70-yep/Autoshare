package com.autoshare.client;

import com.autoshare.dto.UserVerificationResponse;
import com.autoshare.service.UserService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

/**
 * Inter-Service REST Client: Communicates with the User Management Microservice.
 * Demonstrates Microservice-to-Microservice synchronous REST API interaction,
 * fault tolerance, and graceful in-process fallback (Circuit Breaker pattern).
 */
@Component
public class UserVerificationClient {

    private static final Logger log = LoggerFactory.getLogger(UserVerificationClient.class);

    private final RestTemplate restTemplate;
    private final UserService localUserService; // Fallback for unified single-port mode

    @Value("${autoshare.userservice.url:http://localhost:8080/api/users}")
    private String userServiceBaseUrl;

    public UserVerificationClient(RestTemplate restTemplate, UserService localUserService) {
        this.restTemplate = restTemplate;
        this.localUserService = localUserService;
    }

    /**
     * Verifies commuter authorization by dispatching an HTTP GET request to the User Microservice.
     * Falls back to local in-process service if the standalone microservice is unreachable.
     */
    public UserVerificationResponse verifyCommuter(String email) {
        String endpoint = userServiceBaseUrl + "/verify/" + email;
        try {
            log.info("[Microservice-Call] GET {} to verify commuter eligibility", endpoint);
            UserVerificationResponse response = restTemplate.getForObject(endpoint, UserVerificationResponse.class);
            if (response != null) {
                log.info("[Microservice-Response] Commuter {} verified={}", email, response.isVerified());
                return response;
            }
        } catch (Exception ex) {
            log.warn("[Microservice-Warning] Remote User Service call failed ({}), activating in-process fallback", ex.getMessage());
        }

        // Resilient in-process fallback
        return localUserService.verifyUserForRide(email);
    }
}
