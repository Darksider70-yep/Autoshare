package com.autoshare.data;

import com.autoshare.model.Booking;
import com.autoshare.model.Ride;
import com.autoshare.model.RideStatus;
import com.autoshare.repository.BookingRepository;
import com.autoshare.repository.RideRepository;
import java.time.LocalDateTime;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

/**
 * Seeds initial sample data matching the React frontend mock dataset on startup.
 * AUTO-CONFIGURATION NOTE: Spring Boot detects any @Component implementing
 * CommandLineRunner and executes its run() method once the ApplicationContext is ready.
 */
@Component
public class DataInitializer implements CommandLineRunner {

    private final RideRepository rideRepository;
    private final BookingRepository bookingRepository;

    public DataInitializer(RideRepository rideRepository, BookingRepository bookingRepository) {
        this.rideRepository = rideRepository;
        this.bookingRepository = bookingRepository;
    }

    @Override
    public void run(String... args) {
        // Prevent re-seeding if data already exists
        if (rideRepository.count() > 0) {
            return;
        }

        LocalDateTime baseTime = LocalDateTime.now().plusHours(2);

        // Ride 1: Aarav Sharma (Campus Gate 2 -> Starlight Hostels, 1 seat taken, 2 available)
        Ride ride1 = new Ride("Aarav Sharma", "Campus Gate 2", "Starlight Hostels", baseTime.plusMinutes(15), 120.0, 3);
        rideRepository.save(ride1);
        Booking booking1 = new Booking(ride1, "Priya Patel", "priya.p@srmist.edu.in");
        ride1.addBooking(booking1);
        bookingRepository.save(booking1);
        rideRepository.save(ride1);

        // Ride 2: Ananya Iyer (Campus Gate 1 -> Green Meadows Flats, 2 seats taken, 1 available)
        Ride ride2 = new Ride("Ananya Iyer", "Campus Gate 1", "Green Meadows Flats", baseTime.plusMinutes(30), 150.0, 3);
        rideRepository.save(ride2);
        Booking booking2a = new Booking(ride2, "Kabir Sen", "kabir.s@srmist.edu.in");
        Booking booking2b = new Booking(ride2, "Riya Das", "riya.d@srmist.edu.in");
        ride2.addBooking(booking2a);
        ride2.addBooking(booking2b);
        bookingRepository.save(booking2a);
        bookingRepository.save(booking2b);
        rideRepository.save(ride2);

        // Ride 3: Vikram Malhotra (Library Block -> R.K. Puram PG Zone, 0 seats taken, 3 available)
        Ride ride3 = new Ride("Vikram Malhotra", "Library Block", "R.K. Puram PG Zone", baseTime.minusMinutes(15), 90.0, 3);
        rideRepository.save(ride3);

        // Ride 4: Ishaan Verma (Campus Gate 2 -> Royal Residency, 3 seats taken -> FULL)
        Ride ride4 = new Ride("Ishaan Verma", "Campus Gate 2", "Royal Residency", baseTime.plusHours(1), 120.0, 3);
        rideRepository.save(ride4);
        Booking booking4a = new Booking(ride4, "Nikhil Jha", "nikhil.j@srmist.edu.in");
        Booking booking4b = new Booking(ride4, "Amit Shah", "amit.s@srmist.edu.in");
        Booking booking4c = new Booking(ride4, "Rahul Kumar", "rahul.k@srmist.edu.in");
        ride4.addBooking(booking4a);
        ride4.addBooking(booking4b);
        ride4.addBooking(booking4c);
        bookingRepository.save(booking4a);
        bookingRepository.save(booking4b);
        bookingRepository.save(booking4c);
        rideRepository.save(ride4);
    }
}
