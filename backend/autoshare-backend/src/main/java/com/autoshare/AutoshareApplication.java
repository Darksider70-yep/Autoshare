package com.autoshare;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @SpringBootApplication = @Configuration + @ComponentScan + @EnableAutoConfiguration.
 * Scans com.autoshare.* for components and triggers Spring Boot auto-configuration.
 */
@SpringBootApplication
public class AutoshareApplication {
    public static void main(String[] args) {
        SpringApplication.run(AutoshareApplication.class, args);
    }
}
