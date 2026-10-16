package com.autoshare;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Main Entry Point for Autoshare Spring Boot Backend.
 *
 * AUTO-CONFIGURATION NOTE:
 * The @SpringBootApplication annotation is a convenience meta-annotation that bundles:
 * 1. @Configuration: Tags the class as a source of bean definitions for the application context.
 * 2. @EnableAutoConfiguration: Instructs Spring Boot to begin adding beans based on classpath
 *    settings, other beans, and property settings (e.g. provisioning embedded Tomcat, H2 DataSource,
 *    and Hibernate EntityManagerFactory automatically).
 * 3. @ComponentScan: Tells Spring to scan for @Component, @Service, @Repository, and @RestController
 *    classes within the 'com.autoshare' package hierarchy.
 */
@SpringBootApplication
public class AutoshareApplication {

    public static void main(String[] args) {
        SpringApplication.run(AutoshareApplication.class, args);
    }
}
