package com.autoshare.data;

import com.autoshare.model.AccountStatus;
import com.autoshare.model.Booking;
import com.autoshare.model.Ride;
import com.autoshare.model.RideStatus;
import com.autoshare.model.User;
import com.autoshare.model.UserRole;
import com.autoshare.repository.BookingRepository;
import com.autoshare.repository.RideRepository;
import com.autoshare.repository.UserRepository;
import java.time.LocalDateTime;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

/**
 * Seeds initial sample data for Users, Rides, and Bookings on startup.
 * AUTO-CONFIGURATION NOTE: Spring Boot detects any @Component implementing
 * CommandLineRunner and executes its run() method once the ApplicationContext is ready.
 */
@Component
public class DataInitializer implements CommandLineRunner {

    private final RideRepository rideRepository;
    private final BookingRepository bookingRepository;
    private final UserRepository userRepository;

    public DataInitializer(RideRepository rideRepository,
                           BookingRepository bookingRepository,
                           UserRepository userRepository) {
        this.rideRepository = rideRepository;
        this.bookingRepository = bookingRepository;
        this.userRepository = userRepository;
    }

    @Override
    public void run(String... args) {
        seedUsers();
        seedRides();
    }

    private void seedUsers() {
        if (userRepository.count() > 0) {
            return;
        }

        // Student 1: Daksh Gehlot (Author & Lead Developer)
        User u1 = new User("Daksh Gehlot", "daksh.g@srmist.edu.in", "RA2411003012297", "9876543210",
                "Computer Science & Engineering", UserRole.STUDENT_COMMUTER, AccountStatus.VERIFIED, "Campus Gate 2", "Starlight Hostels");
        u1.setRating(5.0);
        u1.setTotalRidesCount(12);
        userRepository.save(u1);

        // Host 1: Aarav Sharma
        User u2 = new User("Aarav Sharma", "aarav.s@srmist.edu.in", "RA2411003012201", "9812345678",
                "Computer Science & Engineering", UserRole.HOST_DRIVER, AccountStatus.VERIFIED, "Campus Gate 2", "Starlight Hostels");
        u2.setRating(4.9);
        u2.setTotalRidesCount(28);
        userRepository.save(u2);

        // Student 2: Priya Patel
        User u3 = new User("Priya Patel", "priya.p@srmist.edu.in", "RA2411003012202", "9823456789",
                "Information Technology", UserRole.STUDENT_COMMUTER, AccountStatus.ACTIVE, "Campus Gate 1", "Green Meadows Flats");
        u3.setRating(4.8);
        u3.setTotalRidesCount(7);
        userRepository.save(u3);

        // Host 2: Ananya Iyer
        User u4 = new User("Ananya Iyer", "ananya.i@srmist.edu.in", "RA2411003012203", "9834567890",
                "Electronics & Communication", UserRole.HOST_DRIVER, AccountStatus.VERIFIED, "Campus Gate 1", "Green Meadows Flats");
        u4.setRating(4.95);
        u4.setTotalRidesCount(42);
        userRepository.save(u4);

        // Student 3: Kabir Sen
        User u5 = new User("Kabir Sen", "kabir.s@srmist.edu.in", "RA2411003012204", "9845678901",
                "Mechanical Engineering", UserRole.STUDENT_COMMUTER, AccountStatus.ACTIVE, "Campus Gate 1", "Green Meadows Flats");
        u5.setRating(4.7);
        u5.setTotalRidesCount(5);
        userRepository.save(u5);

        // Student 4: Riya Das
        User u6 = new User("Riya Das", "riya.d@srmist.edu.in", "RA2411003012205", "9856789012",
                "Computer Science & Engineering", UserRole.STUDENT_COMMUTER, AccountStatus.ACTIVE, "Campus Gate 1", "Green Meadows Flats");
        u6.setRating(4.85);
        u6.setTotalRidesCount(9);
        userRepository.save(u6);

        // Host 3: Vikram Malhotra
        User u7 = new User("Vikram Malhotra", "vikram.m@srmist.edu.in", "RA2411003012206", "9867890123",
                "Civil Engineering", UserRole.HOST_DRIVER, AccountStatus.VERIFIED, "Library Block", "R.K. Puram PG Zone");
        u7.setRating(4.75);
        u7.setTotalRidesCount(15);
        userRepository.save(u7);

        // Admin: Dr. R. Ramanathan
        User u8 = new User("Dr. R. Ramanathan", "ramanathan.r@srmist.edu.in", "FAC20190412", "9898989898",
                "Student Affairs & Transit", UserRole.CAMPUS_ADMIN, AccountStatus.VERIFIED, "Admin Block", "Faculty Enclave");
        u8.setRating(5.0);
        u8.setTotalRidesCount(0);
        userRepository.save(u8);
    }

    private void seedRides() {
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
