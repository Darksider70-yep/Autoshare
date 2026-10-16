package com.autoshare.data;

import com.autoshare.model.Booking;
import com.autoshare.model.Ride;
import com.autoshare.repository.RideRepository;
import java.time.LocalDateTime;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

/**
 * Seeds sample rides at startup. Times are relative to "now" so the data never goes stale.
 * Ride 1: open (1/3), Ride 2: open (0/3), Ride 3: open (0/2), Ride 4: FULL (3/3).
 */
@Component
public class DataInitializer implements CommandLineRunner {

    private final RideRepository rideRepository;

    public DataInitializer(RideRepository rideRepository) {
        this.rideRepository = rideRepository;
    }

    @Override
    public void run(String... args) {
        if (rideRepository.count() > 0) {
            return;
        }
        LocalDateTime now = LocalDateTime.now();

        Ride r1 = new Ride("Aarav Sharma", "Campus Gate 2", "Starlight Hostels", now.plusHours(2), 120.0, 3);
        r1.addBooking(new Booking(r1, "Priya Patel", "priya.p@srmist.edu.in"));

        Ride r2 = new Ride("Meera Iyer", "Campus Gate 1", "Green Meadows Flats", now.plusHours(3), 150.0, 3);

        Ride r3 = new Ride("Rohan Das", "Campus Gate 3", "R.K. Puram PG", now.plusHours(4), 90.0, 2);

        Ride r4 = new Ride("Ishaan Verma", "Campus Gate 2", "Royal Residency", now.plusHours(1), 120.0, 3);
        r4.addBooking(new Booking(r4, "Ananya Rao", "ananya.r@srmist.edu.in"));
        r4.addBooking(new Booking(r4, "Karthik S", "karthik.s@srmist.edu.in"));
        r4.addBooking(new Booking(r4, "Nisha Menon", "nisha.m@srmist.edu.in"));

        rideRepository.save(r1);
        rideRepository.save(r2);
        rideRepository.save(r3);
        rideRepository.save(r4);
    }
}
