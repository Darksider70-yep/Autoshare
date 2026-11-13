import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
import os
from docx_helpers import (
    add_p, add_heading_1, add_heading_2, add_heading_3, add_heading_4,
    add_image_with_caption, add_styled_table, add_code_block
)

def build_chapter_2(doc):
    add_heading_1(doc, "CHAPTER 2\nSPRINT PLANNING AND EXECUTION")
    
    p_intro = (
        "The development of Autoshare was executed using the Agile Scrum framework over three iterative two-week "
        "sprints (six weeks total elapsed time). Each sprint followed rigorous Scrum ceremonies including Sprint Planning, "
        "Daily Standup Calls, Functional and Architectural Design Reviews, Automated Test Execution, and Sprint Retrospectives. "
        "The following sections document the engineering execution, architectural models, test verifications, and burndown metrics "
        "for Sprint 1, Sprint 2, and Sprint 3."
    )
    add_p(doc, p_intro)

    # =========================================================================
    # 2.1 SPRINT 1
    # =========================================================================
    add_heading_2(doc, "2.1 Sprint 1: Core Ride-Pooling Engine & Dynamic Fare Split System")
    
    # 2.1.1
    add_heading_3(doc, "2.1.1 Sprint Goal with User Stories of Sprint 1")
    p_s1_goal = (
        "Sprint 1 focused on engineering the core transactional ride-pooling pipeline and dynamic fare calculation engine. "
        "The sprint goal was: 'Implement the foundational ride publication, discovery, dynamic fare calculation, and seat "
        "reservation engine with a responsive React 19 frontend and Spring Boot 3.3.4 REST backend, validated by unit and API tests.' "
        "Table 2.1 enumerates the user stories committed for Sprint 1."
    )
    add_p(doc, p_s1_goal)
    
    s1_us_headers = ["Story ID", "User Story Description", "Acceptance Criteria", "Story Pts"]
    s1_us_data = [
        ["US-01", "As a student host, I want to publish a ride offer specifying pickup gate, destination, total seats (1-3), total fare, and departure time.", 
         "1. Pickup gate must be an official campus gate.\n2. Total seats restricted to 1–3 passengers.\n3. Total fare must be positive.\n4. Ride initialized with OPEN status and 0 seats taken.", "5"],
        ["US-02", "As a student commuter, I want to search and filter active rides by origin gate and destination hotspot.", 
         "1. Sub-second response time.\n2. Filter by destination cluster (Estancia, Abode Valley, Potheri Stn).\n3. Only show OPEN rides with remaining capacity.", "5"],
        ["US-03", "As a student commuter, I want to book a seat on an open ride and have the dynamic fare split automatically recalculated.", 
         "1. Seat claim is atomic and increments seatsTaken.\n2. Student must provide a valid @srmist.edu.in email.\n3. Duplicate bookings on the same ride are rejected.\n4. When seatsTaken == totalSeats, status transitions to FULL.\n5. Dynamic fare is calculated as totalFare / (seatsTaken + 1).", "8"],
        ["US-10A", "As a software engineer, I want automated unit tests validating ride creation, booking logic, and fare calculation.", 
         "1. 100% pass rate across RideService and RideController.\n2. Validate domain exception handling and RFC error payloads.", "6"]
    ]
    add_styled_table(doc, s1_us_headers, s1_us_data, col_widths=[0.8, 2.5, 2.6, 0.6], 
                     caption="Table 2.1: Sprint 1 Detailed User Stories and Acceptance Criteria")

    # 2.1.2 Functional Document
    add_heading_3(doc, "2.1.2 Functional Document")
    
    add_heading_4(doc, "2.1.2.1 Introduction & Scope")
    add_p(doc, "Sprint 1 encapsulates the foundational domain models and business workflows governing auto-rickshaw pooling. "
               "It encompasses ride creation by student hosts, route discovery by commuter peers, and transactional seat reservations.")
    
    add_heading_4(doc, "2.1.2.2 Product Goal")
    add_p(doc, "Deliver a zero-defect ride publication and booking service capable of preventing race conditions and recalculating "
               "proportional transit costs instantly as co-passengers join.")
    
    add_heading_4(doc, "2.1.2.3 Demography")
    add_p(doc, "Users: SRMIST undergraduate and postgraduate students, day scholars, hostellers residing in nearby private accommodation.\n"
               "Locations: Campus pickup points: Main Gate 1, Gate 2, Tech Park Gate, Library Block; Destinations: Potheri Railway Station, "
               "Estancia Apartments, Abode Valley, Green Pearl PG, and Guduvanchery junction.")
    
    add_heading_4(doc, "2.1.2.4 Business Processes & Core Validation Rules")
    p_biz = (
        "The ride-booking business layer enforces six mandatory domain rules:\n"
        "1. Institutional Email Rule: The student commuter's email must terminate with @srmist.edu.in.\n"
        "2. Vehicle Capacity Constraint: Total seats offered cannot exceed 3 (legal passenger limit of standard Bajaj auto-rickshaws).\n"
        "3. Ride Status Enforcement: Bookings are strictly prohibited on rides marked FULL.\n"
        "4. Duplicate Booking Prevention: A student cannot book multiple seats on the same ride (checked via email and ride ID).\n"
        "5. Automatic Lifecycle Transition: When seatsTaken equals totalSeats, the ride status transitions from OPEN to FULL.\n"
        "6. Dynamic Proportional Fare Division: Fare per person is computed using the formula: "
        "Fare Per Seat = Total Fare / (seatsTaken + 1), where the '+1' accounts for the host commuter."
    )
    add_p(doc, p_biz)
    
    add_heading_4(doc, "2.1.2.5 Authorization Matrix")
    auth_s1_headers = ["User Role", "Publish Ride", "Search / View Rides", "Book Seat", "Cancel Ride", "System Admin"]
    auth_s1_data = [
        ["Guest Commuter", "Denied", "Allowed (Read Only)", "Denied (Login Required)", "Denied", "Denied"],
        ["Verified Student", "Allowed", "Allowed", "Allowed", "Own Rides Only", "Denied"],
        ["Ride Host", "Allowed", "Allowed", "Allowed", "Own Rides Only", "Denied"],
        ["System Administrator", "Allowed", "Allowed", "Allowed", "Allowed (Override)", "Full Access"]
    ]
    add_styled_table(doc, auth_s1_headers, auth_s1_data, col_widths=[1.5, 1.0, 1.3, 1.3, 1.0, 0.9], 
                     caption="Table 2.2: Sprint 1 Role-Based Access Control Authorization Matrix")
    
    add_heading_4(doc, "2.1.2.6 Assumptions")
    add_p(doc, "1. All participating auto-rickshaws operate on standard three-seat configurations.\n"
               "2. Settlement of the dynamically calculated fare is executed in person via UPI or cash upon reaching the destination.\n"
               "3. Clients maintain network connectivity to interact with the HTTP REST API.")

    # 2.1.3 Architecture Document
    add_heading_3(doc, "2.1.3 Architecture Document")
    add_p(doc, "Sprint 1 established a Three-Tier Layered Architecture within the autoshare-backend service: "
               "Presentation Layer (RideController, GlobalExceptionHandler), Business Service Layer (RideService, BookingService), "
               "and Data Access Layer (RideRepository, BookingRepository) backed by an in-memory H2 database.")
    
    add_p(doc, "The REST API Contract specification implemented in Sprint 1 is summarized in Table 2.3.")
    
    api_s1_headers = ["HTTP Verb", "Endpoint URI", "Request Body / Params", "Success Status", "Primary Function"]
    api_s1_data = [
        ["GET", "/api/rides", "Optional query params: destination, gate", "200 OK", "Fetches list of active rides matching criteria"],
        ["GET", "/api/rides/{id}", "Path variable: id (Long)", "200 OK", "Retrieves comprehensive details of a single ride"],
        ["POST", "/api/rides", "JSON: hostName, pickupGate, destination, totalFare, totalSeats, departureTime", "201 Created", "Creates a new ride offer in OPEN status"],
        ["POST", "/api/rides/{id}/book", "JSON: studentName, studentEmail", "201 Created", "Atomically reserves a seat and recalculates split fare"],
        ["GET", "/api/rides/{id}/fare-split", "Path variable: id (Long)", "200 OK", "Returns real-time dynamic fare split breakdown"]
    ]
    add_styled_table(doc, api_s1_headers, api_s1_data, col_widths=[0.9, 1.8, 1.8, 0.9, 1.6], 
                     caption="Table 2.3: Sprint 1 Core REST API Contract Specification")
    
    add_p(doc, "Relational Schema Definition:\n"
               "1. Table 'rides': id (BIGINT PRIMARY KEY AUTO_INCREMENT), host_name (VARCHAR 100), pickup_gate (VARCHAR 100), "
               "destination (VARCHAR 100), departure_time (TIMESTAMP), total_fare (DECIMAL 10,2), total_seats (INT), "
               "seats_taken (INT), status (VARCHAR 20).\n"
               "2. Table 'bookings': id (BIGINT PRIMARY KEY AUTO_INCREMENT), ride_id (BIGINT NOT NULL REFERENCES rides(id)), "
               "student_name (VARCHAR 100), student_email (VARCHAR 100), booked_at (TIMESTAMP). Unique constraint on (ride_id, student_email).")

    # 2.1.4 UI Design
    add_heading_3(doc, "2.1.4 UI Design")
    add_p(doc, "The frontend was constructed using React 19 and Vite 6, incorporating modular components styled with custom CSS variables "
               "and Lucide React iconography. The UI provides instant visual feedback through active route cards, remaining capacity badges, "
               "and an interactive modal for publishing new journeys.")
    
    add_image_with_caption(doc, 'docs/screenshots/01_app_running_successfully.png', 
                           "Figure 2.1: Autoshare React 19 Client Landing Page & Active Rides Feed", width_inches=5.6)
    add_image_with_caption(doc, 'docs/screenshots/02_rest_endpoint_output_rides.png', 
                           "Figure 2.2: REST API Response Payload for Active Campus Rides (GET /api/rides)", width_inches=5.4)
    add_image_with_caption(doc, 'docs/screenshots/03_rest_endpoint_fare_split.png', 
                           "Figure 2.3: Dynamic Fare Split Calculation JSON Endpoint (GET /api/rides/1/fare-split)", width_inches=5.4)
    add_image_with_caption(doc, 'docs/screenshots/04_h2_database_console.png', 
                           "Figure 2.4: In-Memory H2 Relational Database Web Console and Schema Tables", width_inches=5.4)

    # 2.1.5 Functional Test Cases
    add_heading_3(doc, "2.1.5 Functional Test Cases")
    add_p(doc, "Sprint 1 functional verification comprised comprehensive integration tests testing happy-path and boundary conditions. "
               "Table 2.4 details the executed test cases.")
    
    tc_s1_headers = ["Test ID", "Scenario", "Input Parameters", "Expected Result", "Actual Result", "Status"]
    tc_s1_data = [
        ["TC-S1-01", "Create Ride Valid", "Host: 'Daksh', Gate: 'Gate 1', Dest: 'Estancia', Fare: 120, Seats: 3", "HTTP 201 Created; status=OPEN; seatsTaken=0", "As expected", "PASS"],
        ["TC-S1-02", "Create Ride Invalid Capacity", "Seats: 5 (exceeds auto limit 3)", "HTTP 400 Bad Request; validation message", "As expected", "PASS"],
        ["TC-S1-03", "Atomic Seat Claim Valid", "Ride ID: 1, Name: 'Rohit', Email: 'rohit@srmist.edu.in'", "HTTP 201 Created; seatsTaken=1; farePerPerson=60.0", "As expected", "PASS"],
        ["TC-S1-04", "Invalid Domain Rejection", "Ride ID: 1, Email: 'rohit@gmail.com'", "HTTP 400 Bad Request; 'Must be @srmist.edu.in'", "As expected", "PASS"],
        ["TC-S1-05", "Duplicate Booking Rejection", "Ride ID: 1, re-booking with 'rohit@srmist.edu.in'", "HTTP 409 Conflict; DuplicateBookingException", "As expected", "PASS"],
        ["TC-S1-06", "Auto Transition to FULL", "Book remaining seats until seatsTaken == totalSeats", "HTTP 201 Created; ride status becomes FULL", "As expected", "PASS"]
    ]
    add_styled_table(doc, tc_s1_headers, tc_s1_data, col_widths=[0.8, 1.4, 1.6, 1.5, 0.8, 0.5], 
                     caption="Table 2.4: Sprint 1 Functional Test Cases (TC-S1-01 to TC-S1-06)")

    # 2.1.6 Daily Scrum Call Progress
    add_heading_3(doc, "2.1.6 Daily Call Progress")
    add_p(doc, "During the 10 working days of Sprint 1 (September 1 to September 14, 2026), daily 15-minute standup meetings tracked "
               "development progress and resolved technical blockers.")
    
    scrum_s1_headers = ["Day", "Tasks Completed Yesterday", "Planned Tasks for Today", "Impediments / Blockers Encountered & Resolutions"]
    scrum_s1_data = [
        ["Day 1", "Sprint backlog grooming; repository initialized.", "Configure Maven pom.xml and Spring Boot dependencies.", "None. Initial environment verified on Java 17."],
        ["Day 2", "Configured Spring Boot 3.3.4 project skeleton.", "Define Ride and Booking persistent entities in com.autoshare.model.", "Resolved Jakarta persistence annotation import changes in Spring Boot 3."],
        ["Day 3", "Built Ride and Booking entity models.", "Implement RideRepository and BookingRepository interfaces.", "Configured Hibernate auto-DDL in application.properties for H2."],
        ["Day 4", "Created Spring Data JPA repositories.", "Implement RideService with core booking validation logic.", "Encountered NullPointerException on null booking lists; initialized lists eagerly."],
        ["Day 5", "Implemented bookSeat() transactional method.", "Develop dynamic fare split calculation algorithm.", "Formulated exact proportional division formula (totalFare / (seatsTaken + 1))."],
        ["Day 6", "Tested fare division business logic.", "Construct RideController and BookingController REST endpoints.", "Vite client faced CORS error when calling 8080; added Vite reverse proxy."],
        ["Day 7", "Configured Vite reverse proxy in vite.config.js.", "Develop React 19 HeroSearch and RidesFeed components.", "None. Tailwind design tokens integrated smoothly."],
        ["Day 8", "Built RidesFeed and interactive RideCard.", "Implement PostRideModal and dynamic split estimator.", "Modal focus trap issue in React 19 resolved using useEffect keydown listener."],
        ["Day 9", "Completed PostRideModal and Toast alerts.", "Write JUnit 5 and Mockito unit tests for RideService.", "Configured Mockito extension to mock repository dependency calls."],
        ["Day 10", "Finalized 10 automated tests for Sprint 1.", "Sprint review and demonstration of full booking flow.", "Sprint goal met with 100% committed stories completed."]
    ]
    add_styled_table(doc, scrum_s1_headers, scrum_s1_data, col_widths=[0.6, 1.9, 1.9, 2.2], 
                     caption="Table 2.5: Sprint 1 Daily Scrum Progress & Blocker Resolution Log (10 Days)")

    # 2.1.7 Committed vs Completed
    add_heading_3(doc, "2.1.7 Committed vs Completed User Stories")
    p_s1_c = (
        "In Sprint 1, 24 story points were committed and 24 story points were successfully delivered, representing a 100% "
        "completion rate. Table 2.6 summarizes the velocity breakdown, and Figure 2.5 depicts the sprint burndown trajectory."
    )
    add_p(doc, p_s1_c)
    
    cvc_s1_headers = ["User Story ID", "Summary", "Committed Points", "Completed Points", "Completion Status"]
    cvc_s1_data = [
        ["US-01", "Publish Ride Offer", "5", "5", "COMPLETED"],
        ["US-02", "Search and Filter Active Rides", "5", "5", "COMPLETED"],
        ["US-03", "Dynamic Fare Split & Seat Claim", "8", "8", "COMPLETED"],
        ["US-10A", "Sprint 1 Automated Unit Testing", "6", "6", "COMPLETED"],
        ["Total", "Sprint 1 Velocity Summary", "24", "24", "100% DELIVERED"]
    ]
    add_styled_table(doc, cvc_s1_headers, cvc_s1_data, col_widths=[1.2, 2.7, 1.1, 1.1, 1.1], 
                     caption="Table 2.6: Sprint 1 Committed vs Completed User Stories Breakdown")
    
    add_image_with_caption(doc, 'docs/screenshots/figure_2_1_burndown.png', 
                           "Figure 2.5: Sprint 1 Burndown Chart & Story Point Realization", width_inches=5.2)

    # 2.1.8 Retrospective
    add_heading_3(doc, "2.1.8 Sprint Retrospective")
    add_p(doc, "What Went Well: The dynamic fare split engine functioned flawlessly across boundary scenarios. Vite reverse proxy "
               "eliminated frontend CORS hurdles, and React 19 hooks provided clean reactive updates.\n"
               "What Could Be Improved: In-memory ride storage lacked persistent user identity auditing; commuters could enter arbitrary names "
               "as long as email format was valid.\n"
               "Action Items for Sprint 2: Build a dedicated Spring Data JPA User Record Management module with institutional registration number "
               "validation, persistent database storage, and a comprehensive user administration interface.")

    # =========================================================================
    # 2.2 SPRINT 2
    # =========================================================================
    add_heading_2(doc, "2.2 Sprint 2: Spring Data JPA User Record Management & Institutional Identity Persistence")
    
    # 2.2.1
    add_heading_3(doc, "2.2.1 Sprint Goal with User Stories of Sprint 2")
    p_s2_goal = (
        "Sprint 2 focused on creating a persistent relational user identity management module. "
        "The sprint goal was: 'Design, implement, and test persistent domain entities, Spring Data JPA repositories with derived "
        "and custom JPQL queries, a transactional user service layer with complete CRUD operations, and an interactive React management "
        "interface for student records.' Table 2.7 outlines the Sprint 2 user stories."
    )
    add_p(doc, p_s2_goal)
    
    s2_us_headers = ["Story ID", "User Story Description", "Acceptance Criteria", "Story Pts"]
    s2_us_data = [
        ["US-04", "As a student commuter, I want to register a persistent profile with full name, SRM email, registration number, and department.", 
         "1. Email must match @srmist.edu.in.\n2. Registration number must match institutional format (^RA[0-9]{13}$).\n3. Default role set to STUDENT and status to ACTIVE.", "5"],
        ["US-05", "As a campus administrator, I want full CRUD operations on user records via Spring Data JPA.", 
         "1. Create, read, update, delete endpoints operational.\n2. Prevent duplicate email or registration number registration.\n3. Support status transitions (ACTIVE, SUSPENDED, PENDING_VERIFICATION).", "8"],
        ["US-06", "As an administrator, I want to perform multi-attribute search and filtering across user records using custom JPQL queries.", 
         "1. Case-insensitive full-text search across name, email, and registration number.\n2. Filter by department and user role.\n3. Return sorted results within 20 ms.", "5"],
        ["US-10B", "As a QA engineer, I want comprehensive unit and MockMvc integration tests for JPA repositories, services, and controllers.", 
         "1. 100% test pass rate across UserService and UserController.\n2. Verify rollback on transaction failure and custom exception mapping.", "8"]
    ]
    add_styled_table(doc, s2_us_headers, s2_us_data, col_widths=[0.8, 2.5, 2.6, 0.6], 
                     caption="Table 2.7: Sprint 2 Detailed User Stories and Acceptance Criteria")

    # 2.2.2 Functional Document
    add_heading_3(doc, "2.2.2 Functional Document")
    add_heading_4(doc, "2.2.2.1 Introduction & Scope")
    add_p(doc, "Sprint 2 introduces the User Management bounded context. It provides institutional record persistence, "
               "auditing, and role assignment to establish a verifiable user base for the campus mobility ecosystem.")
    
    add_heading_4(doc, "2.2.2.2 Product Goal")
    add_p(doc, "Maintain an accurate, ACID-compliant relational data store of verified student commuters and ride hosts, "
               "enforcing university data integrity rules.")
    
    add_heading_4(doc, "2.2.2.3 Demography")
    add_p(doc, "Departments: Computing Technologies, Information Technology, Electronics & Communication, Mechanical Engineering, "
               "Biotechnology, Management Studies; Roles: Student Commuter, Ride Host, Faculty Commuter, System Administrator.")
    
    add_heading_4(doc, "2.2.2.4 Business Processes & Lifecycle Management")
    p_bp2 = (
        "User records traverse a deterministic lifecycle managed via AccountStatus:\n"
        "1. PENDING_VERIFICATION: Default state upon self-registration pending email confirmation.\n"
        "2. ACTIVE: Full platform privileges; eligible to publish rides and book co-passenger seats.\n"
        "3. SUSPENDED: Administrative penalty for policy violations or missed ride departures; blocked from active bookings.\n"
        "Role permissions are governed by UserRole: STUDENT (standard commuter), HOST (authorized vehicle coordinator), "
        "ADMIN (complete directory administration)."
    )
    add_p(doc, p_bp2)
    
    add_heading_4(doc, "2.2.2.5 Authorization Matrix")
    auth_s2_headers = ["Operation", "Anonymous Visitor", "Student / Host", "System Administrator"]
    auth_s2_data = [
        ["Register Profile", "Allowed", "Allowed (Update Own)", "Allowed"],
        ["View Own Record", "Denied", "Allowed", "Allowed"],
        ["Search User Directory", "Denied", "Allowed (Basic Info)", "Allowed (Full Record)"],
        ["Update User Status (ACTIVE/SUSPENDED)", "Denied", "Denied", "Allowed"],
        ["Delete User Record (Hard Delete)", "Denied", "Denied", "Allowed"]
    ]
    add_styled_table(doc, auth_s2_headers, auth_s2_data, col_widths=[2.2, 1.4, 1.8, 1.8], 
                     caption="Table 2.8: Sprint 2 User Identity Authorization Matrix")
    
    add_heading_4(doc, "2.2.2.6 Assumptions")
    add_p(doc, "1. Registration numbers strictly follow the 15-character SRMIST pattern (e.g. RA2411003012297).\n"
               "2. Email uniqueness is enforced at both database constraint and application service layers.\n"
               "3. Administrative operations require privileged access tokens.")

    # 2.2.3 Architecture Document
    add_heading_3(doc, "2.2.3 Architecture Document")
    add_p(doc, "The User Management module was architected using Spring Data JPA with Hibernate as the Object-Relational Mapping (ORM) provider. "
               "Entity definitions leverage Jakarta Persistence annotations with automatic timestamping via @CreationTimestamp and @UpdateTimestamp.")
    
    add_p(doc, "The REST API Contract for the persistent User Service is outlined in Table 2.9.")
    
    api_s2_headers = ["HTTP Verb", "Endpoint URI", "Payload / Parameters", "Status Code", "Functionality"]
    api_s2_data = [
        ["GET", "/api/users", "None", "200 OK", "Returns all persistent user records"],
        ["GET", "/api/users/{id}", "Path variable: id (Long)", "200 OK", "Retrieves single user by primary key"],
        ["GET", "/api/users/search", "Query param: q (String)", "200 OK", "Executes multi-field JPQL LIKE search"],
        ["POST", "/api/users", "JSON: fullName, email, regNumber, department, role", "201 Created", "Persists new user record"],
        ["PUT", "/api/users/{id}", "JSON: updated user details", "200 OK", "Performs full entity update with validation"],
        ["DELETE", "/api/users/{id}", "Path variable: id (Long)", "204 No Content", "Deletes user record by ID"],
        ["PATCH", "/api/users/{id}/status", "JSON: status (ACTIVE/SUSPENDED)", "200 OK", "Mutates user account status"],
        ["GET", "/api/users/verify/{email}", "Path variable: email (String)", "200 OK", "Verifies student KYC eligibility"]
    ]
    add_styled_table(doc, api_s2_headers, api_s2_data, col_widths=[0.9, 1.8, 1.8, 0.9, 1.6], 
                     caption="Table 2.9: Sprint 2 Spring Data JPA User Service REST API Contract")
    
    add_p(doc, "Custom JPQL Multi-Field Search Implementation:\n"
               "In UserRepository.java, efficient multi-attribute matching is achieved via a parameterized JPQL query:\n"
               "@Query(\"SELECT u FROM User u WHERE LOWER(u.fullName) LIKE LOWER(CONCAT('%', :query, '%')) \" +\n"
               "       \"OR LOWER(u.email) LIKE LOWER(CONCAT('%', :query, '%')) \" +\n"
               "       \"OR LOWER(u.registrationNumber) LIKE LOWER(CONCAT('%', :query, '%'))\")\n"
               "List<User> searchUsers(@Param(\"query\") String query);")

    # 2.2.4 UI Design
    add_heading_3(doc, "2.2.4 UI Design")
    add_p(doc, "A dedicated 'User Records' tab was added to the React 19 frontend. It presents an administrative data table featuring "
               "live text search, role filter pills, status toggle badges (green for ACTIVE, amber for SUSPENDED), modal dialogs for "
               "creating and updating users, and quick KPI counter metrics.")
    
    add_image_with_caption(doc, 'docs/screenshots/06_unit5_spring_boot_jpa_startup.png', 
                           "Figure 2.6: Spring Boot Data JPA Microservice Startup Banner and Port Binding", width_inches=5.4)
    add_image_with_caption(doc, 'docs/screenshots/07_unit5_crud_rest_apis_execution.png', 
                           "Figure 2.7: Execution and Terminal Verification of Spring Data JPA User CRUD REST Endpoints", width_inches=5.4)
    add_image_with_caption(doc, 'docs/screenshots/10_unit5_react_ui_user_records.png', 
                           "Figure 2.8: Interactive User Record Management Dashboard in React 19 Frontend", width_inches=5.6)

    # 2.2.5 Functional Test Cases
    add_heading_3(doc, "2.2.5 Functional Test Cases")
    add_p(doc, "Functional validation in Sprint 2 verified all CRUD operations, database constraints, and JPQL search accuracy. "
               "Table 2.10 provides the test case specification.")
    
    tc_s2_headers = ["Test ID", "Scenario", "Input Parameters", "Expected Result", "Actual Result", "Status"]
    tc_s2_data = [
        ["TC-S2-01", "Create User Valid", "Daksh, daksh.g@srmist.edu.in, RA2411003012297, C.Tech", "HTTP 201 Created; id assigned; status=ACTIVE", "As expected", "PASS"],
        ["TC-S2-02", "Duplicate Email Rejection", "Re-register with same daksh.g@srmist.edu.in", "HTTP 409 Conflict; DuplicateEmailException", "As expected", "PASS"],
        ["TC-S2-03", "Invalid Reg Number Regex", "RegNumber: '12345' (invalid format)", "HTTP 400 Bad Request; validation failed", "As expected", "PASS"],
        ["TC-S2-04", "JPQL Multi-Field Search", "Query: 'RA2411' or 'daksh'", "HTTP 200 OK; returns matching User record", "As expected", "PASS"],
        ["TC-S2-05", "Update User Department", "PUT /api/users/1 with new department 'Software Eng'", "HTTP 200 OK; department updated in DB", "As expected", "PASS"],
        ["TC-S2-06", "Patch Account Status", "PATCH /api/users/1/status with SUSPENDED", "HTTP 200 OK; status=SUSPENDED in DB", "As expected", "PASS"],
        ["TC-S2-07", "Delete User by ID", "DELETE /api/users/1", "HTTP 204 No Content; record removed from DB", "As expected", "PASS"]
    ]
    add_styled_table(doc, tc_s2_headers, tc_s2_data, col_widths=[0.8, 1.4, 1.6, 1.5, 0.8, 0.5], 
                     caption="Table 2.10: Sprint 2 Functional Test Cases (TC-S2-01 to TC-S2-07)")

    # 2.2.6 Daily Scrum Call Progress
    add_heading_3(doc, "2.2.6 Daily Call Progress")
    add_p(doc, "Sprint 2 spanned September 15 to September 28, 2026. Daily standup logs document the progression of Data JPA implementation.")
    
    scrum_s2_headers = ["Day", "Tasks Completed Yesterday", "Planned Tasks for Today", "Impediments / Blockers Encountered & Resolutions"]
    scrum_s2_data = [
        ["Day 1", "Sprint 2 planning; finalized user entity attributes.", "Define User entity with Jakarta validation annotations.", "None. Requirements finalized."],
        ["Day 2", "Created User domain entity with enums.", "Configure UserRepository and derived query methods.", "Derived query findByDepartmentIgnoreCase syntax verified."],
        ["Day 3", "Tested derived queries.", "Write custom JPQL multi-field search query.", "Fixed SQL syntax error in LIKE query using LOWER() CONCAT."],
        ["Day 4", "Validated JPQL search query.", "Implement UserService and UserServiceImpl transactional methods.", "Encountered LazyInitializationException during unit test; solved via eager fetching."],
        ["Day 5", "Implemented full CRUD in UserServiceImpl.", "Develop UserController with 8 REST endpoints.", "Added @Valid annotations to handle bean validation."],
        ["Day 6", "Built UserController endpoints.", "Add GlobalExceptionHandler mapping for UserNotFoundException.", "Configured standard RFC-7807 problem details in error JSON."],
        ["Day 7", "Centralized exception handling.", "Build React 19 User Records management table.", "Table pagination layout designed with Tailwind."],
        ["Day 8", "Constructed User Records table.", "Implement Add/Edit User modal dialogs in React.", "State synchronization bug between modal form and table solved via callback."],
        ["Day 9", "Added status toggle buttons and search bar.", "Write JUnit 5 unit tests for UserService.", "Mocked UserRepository methods using Mockito when().thenReturn()."],
        ["Day 10", "Executed all 12 Spring Data JPA tests.", "Sprint review and demonstration of User Records UI.", "Sprint 2 goals met with 100% committed stories completed."]
    ]
    add_styled_table(doc, scrum_s2_headers, scrum_s2_data, col_widths=[0.6, 1.9, 1.9, 2.2], 
                     caption="Table 2.11: Sprint 2 Daily Scrum Progress & Blocker Resolution Log (10 Days)")

    # 2.2.7 Committed vs Completed
    add_heading_3(doc, "2.2.7 Committed vs Completed User Stories")
    add_p(doc, "Sprint 2 committed 26 story points and completed 26 story points (100% velocity realization). "
               "Table 2.12 outlines the completed user stories, and Figure 2.9 shows the burndown chart.")
    
    cvc_s2_headers = ["User Story ID", "Summary", "Committed Points", "Completed Points", "Completion Status"]
    cvc_s2_data = [
        ["US-04", "Student Profile Registration", "5", "5", "COMPLETED"],
        ["US-05", "Spring Data JPA CRUD Operations", "8", "8", "COMPLETED"],
        ["US-06", "JPQL Multi-Field Full-Text Search", "5", "5", "COMPLETED"],
        ["US-10B", "Sprint 2 Automated Unit & Integration Testing", "8", "8", "COMPLETED"],
        ["Total", "Sprint 2 Velocity Summary", "26", "26", "100% DELIVERED"]
    ]
    add_styled_table(doc, cvc_s2_headers, cvc_s2_data, col_widths=[1.2, 2.7, 1.1, 1.1, 1.1], 
                     caption="Table 2.12: Sprint 2 Committed vs Completed User Stories Breakdown")
    
    add_image_with_caption(doc, 'docs/screenshots/figure_2_2_burndown.png', 
                           "Figure 2.9: Sprint 2 Burndown Chart & Story Point Realization", width_inches=5.2)

    # 2.2.8 Retrospective
    add_heading_3(doc, "2.2.8 Sprint Retrospective")
    add_p(doc, "What Went Well: Spring Data JPA simplified boilerplate DAO code significantly. JPQL multi-field search proved extremely fast (< 15 ms). "
               "React modal forms integrated cleanly with backend REST endpoints.\n"
               "What Could Be Improved: Both ride-booking and user-management currently run in the same Spring Boot instance. In an enterprise campus "
               "environment, high booking traffic could degrade user registration latency.\n"
               "Action Items for Sprint 3: Decouple the monolithic service into two distinct microservices on separate ports (8080 and 8081). "
               "Establish inter-service communication with RestTemplate, implement Circuit Breaker fallback, and build a Microservices Architecture Console.")

    # =========================================================================
    # 2.3 SPRINT 3
    # =========================================================================
    add_heading_2(doc, "2.3 Sprint 3: Microservices Architecture, Inter-Service REST & Console")
    
    # 2.3.1
    add_heading_3(doc, "2.3.1 Sprint Goal with User Stories of Sprint 3")
    p_s3_goal = (
        "Sprint 3 accomplished the architectural decoupling into independent microservices and end-to-end integration. "
        "The sprint goal was: 'Decouple the application into independent microservices (user-management-service on port 8081 and "
        "ride-booking-service on port 8080), establish synchronous inter-service REST communication with circuit breaker fallback, "
        "and build an interactive system console with wire inspection in React 19.' Table 2.13 presents the Sprint 3 user stories."
    )
    add_p(doc, p_s3_goal)
    
    s3_us_headers = ["Story ID", "User Story Description", "Acceptance Criteria", "Story Pts"]
    s3_us_data = [
        ["US-07", "As an architect, I want to decouple the backend into independent microservices running on isolated ports.", 
         "1. user-management-service runs on port 8081 with its own JPA data store.\n2. ride-booking-service runs on port 8080 with its own H2 database.\n3. Reverse proxy handles routing from frontend port 3000.", "8"],
        ["US-08", "As the ride booking service, I want to verify commuter KYC via synchronous REST call to user service with fallback.", 
         "1. Invoke GET /api/users/verify/{email} before booking.\n2. Timeout set to 1500 ms.\n3. If user service is down, activate graceful fallback permitting provisional booking with warning.", "8"],
        ["US-09", "As a developer, I want an interactive Microservices Console in the UI with a 4-step execution runner and wire inspector.", 
         "1. Step-by-step pipeline visualization.\n2. Live display of request/response JSON payloads.\n3. Visual status badges for both microservices.", "5"],
        ["US-10C", "As a QA lead, I want end-to-end integration tests verifying inter-service communication and total test count >= 20.", 
         "1. Comprehensive test suite with 22 tests passing 100% across all modules.\n2. Verified fallback behavior under mocked service outage.", "7"]
    ]
    add_styled_table(doc, s3_us_headers, s3_us_data, col_widths=[0.8, 2.5, 2.6, 0.6], 
                     caption="Table 2.13: Sprint 3 Detailed User Stories and Acceptance Criteria")

    # 2.3.2 Functional Document
    add_heading_3(doc, "2.3.2 Functional Document")
    add_heading_4(doc, "2.3.2.1 Introduction & Scope")
    add_p(doc, "Sprint 3 transforms the platform into an enterprise distributed system. Bounded contexts are physically segregated: "
               "User Management handles student records and identity KYC; Ride Booking manages rides, capacity, and dynamic fare splitting.")
    
    add_heading_4(doc, "2.3.2.2 Product Goal")
    add_p(doc, "Guarantee operational resilience such that ride booking operations remain fault-tolerant and responsive even during "
               "intermittent degradation of the identity service.")
    
    add_heading_4(doc, "2.3.2.3 Demography")
    add_p(doc, "Distributed service nodes running locally and in containerized cloud environments; consumer client applications "
               "interacting through a unified reverse proxy.")
    
    add_heading_4(doc, "2.3.2.4 Business Processes & Inter-Service Contract")
    p_bp3 = (
        "The distributed booking verification flow proceeds as follows:\n"
        "1. Commuter initiates a seat booking request on port 8080: POST /api/rides/{id}/book with studentName and studentEmail.\n"
        "2. RideService dispatches a synchronous HTTP GET request via UserVerificationClient to user-management-service: "
        "http://localhost:8081/api/users/verify/{email}.\n"
        "3. User service queries its JPA repository and returns UserVerificationResponse: { verified: true, active: true, studentName: '...', department: '...' }.\n"
        "4. If verified, RideService commits the booking and recalculates dynamic fare split.\n"
        "5. If user service is unreachable or exceeds the 1500 ms connection timeout, the Circuit Breaker Graceful Fallback activates: "
        "provisional booking is permitted, an alert flag is attached to the response, and error is logged without crashing the thread."
    )
    add_p(doc, p_bp3)
    
    add_heading_4(doc, "2.3.2.5 Authorization Matrix")
    add_styled_table(doc, 
                     ["Microservice Boundary", "Port", "Database Store", "Exposed APIs", "Inter-Service Dependency"],
                     [["user-management-service", "8081", "H2 (users table)", "/api/users/**, /api/users/verify/**", "None (Self-contained)"],
                      ["ride-booking-service", "8080", "H2 (rides, bookings)", "/api/rides/**, /api/bookings/**", "Calls port 8081 for KYC"],
                      ["autoshare-react-client", "3000", "Browser Local State", "Reverse proxy /api/rides & /api/users", "Consumes both services via proxy"]],
                     col_widths=[1.6, 0.7, 1.4, 1.8, 1.5],
                     caption="Table 2.14: Sprint 3 Microservices Inter-Service REST Contract & Architecture Boundaries")
    
    add_heading_4(doc, "2.3.2.6 Assumptions")
    add_p(doc, "1. Both microservices share identical network subnets during local development.\n"
               "2. RestTemplate timeout is configured to 1500 ms for connect and read operations.\n"
               "3. Network latency between microservices remains under 10 ms.")

    # 2.3.3 Architecture Document
    add_heading_3(doc, "2.3.3 Architecture Document")
    add_p(doc, "The microservices architecture employs a reverse proxy topology. The React 19 single-page application dispatches all "
               "requests through Vite's internal development proxy, routing /api/rides and /api/bookings to port 8080 and /api/users to port 8081. "
               "Inter-service communication is governed by UserVerificationClient, an encapsulated Spring component utilizing RestTemplateBuilder.")
    
    add_p(doc, "UserVerificationClient Fallback Implementation:\n"
               "The client wraps inter-service REST calls inside a try-catch block catching ResourceAccessException and HttpStatusCodeException. "
               "Upon network timeout, it logs a warning: 'User verification service unreachable at port 8081. Applying graceful fallback: provisional verification.' "
               "and returns UserVerificationResponse.builder().verified(true).provisional(true).build(). This prevents complete transaction outage.")

    # 2.3.4 UI Design
    add_heading_3(doc, "2.3.4 UI Design")
    add_p(doc, "The interactive 'Microservices Console' tab allows developers and evaluators to execute a step-by-step distributed workflow: "
               "Step 1: Check Commuter KYC Eligibility (queries 8081); Step 2: Fetch Active Campus Rides (queries 8080); "
               "Step 3: Execute Atomic Seat Claim (triggers inter-service trace); Step 4: Live Fare Split Recalculation. "
               "A Live Wire Inspector displays the raw JSON wire payloads exchanged across network boundaries.")
    
    add_image_with_caption(doc, 'docs/screenshots/08_unit5_microservices_inter_service_trace.png', 
                           "Figure 2.10: Inter-Service HTTP REST Trace between Ride Service (8080) and User Service (8081)", width_inches=5.4)
    add_image_with_caption(doc, 'docs/screenshots/11_unit5_react_ui_microservices_console.png', 
                           "Figure 2.11: Microservices Architecture Console with Step-by-Step Pipeline Runner & Wire Inspector", width_inches=5.6)

    # 2.3.5 Functional Test Cases
    add_heading_3(doc, "2.3.5 Functional Test Cases")
    add_p(doc, "Sprint 3 testing verified inter-service REST calls, circuit breaker fallbacks, and full end-to-end multi-step flows. "
               "Table 2.15 itemizes the test results.")
    
    tc_s3_headers = ["Test ID", "Scenario", "Input Parameters", "Expected Result", "Actual Result", "Status"]
    tc_s3_data = [
        ["TC-S3-01", "Inter-Service KYC Verified", "GET /api/users/verify/daksh.g@srmist.edu.in", "HTTP 200 OK; verified=true, active=true", "As expected", "PASS"],
        ["TC-S3-02", "Inter-Service KYC Unregistered", "GET /api/users/verify/unknown@srmist.edu.in", "HTTP 404 Not Found; verified=false", "As expected", "PASS"],
        ["TC-S3-03", "Inter-Service Suspended User", "User with SUSPENDED status attempts booking", "HTTP 403 Forbidden; 'Account suspended'", "As expected", "PASS"],
        ["TC-S3-04", "Circuit Breaker Fallback on Outage", "Port 8081 stopped; book seat on port 8080", "HTTP 201 Created; provisional=true warning logged", "As expected", "PASS"],
        ["TC-S3-05", "Vite Reverse Proxy Routing 8080", "GET /api/rides through port 3000", "Proxied to :8080; HTTP 200 OK", "As expected", "PASS"],
        ["TC-S3-06", "Vite Reverse Proxy Routing 8081", "GET /api/users through port 3000", "Proxied to :8081; HTTP 200 OK", "As expected", "PASS"],
        ["TC-S3-07", "Step-by-Step Console Pipeline", "Execute all 4 steps sequentially", "All 4 steps green; JSON wire payloads displayed", "As expected", "PASS"],
        ["TC-S3-08", "Full Regression Test Suite", "Run Maven test across all modules", "22 tests executed; 0 failures; 0 errors", "As expected", "PASS"]
    ]
    add_styled_table(doc, tc_s3_headers, tc_s3_data, col_widths=[0.8, 1.4, 1.6, 1.5, 0.8, 0.5], 
                     caption="Table 2.15: Sprint 3 Functional Test Cases (TC-S3-01 to TC-S3-08)")

    # 2.3.6 Daily Scrum Call Progress
    add_heading_3(doc, "2.3.6 Daily Call Progress")
    add_p(doc, "Sprint 3 ran from September 29 to October 12, 2026. Daily standup logs document the distributed migration.")
    
    scrum_s3_headers = ["Day", "Tasks Completed Yesterday", "Planned Tasks for Today", "Impediments / Blockers Encountered & Resolutions"]
    scrum_s3_data = [
        ["Day 1", "Sprint 3 planning; finalized microservices topology.", "Decouple backend into two Maven application modules.", "Addressed pom.xml parent artifact inheritance."],
        ["Day 2", "Configured port 8081 for user-management-service.", "Verify standalone execution of both services.", "Port collision during simultaneous boot resolved by setting server.port in properties."],
        ["Day 3", "Both services booting on isolated ports.", "Create UserVerificationClient in ride-booking-service.", "Added RestTemplateBuilder bean configuration."],
        ["Day 4", "Integrated UserVerificationClient into RideService.", "Implement Circuit Breaker graceful fallback logic.", "Tested network timeout simulation using 1500 ms read timeout."],
        ["Day 5", "Verified graceful fallback handling.", "Configure multi-target reverse proxy in vite.config.js.", "Configured path rewrite rules for /api/users and /api/rides."],
        ["Day 6", "Tested proxy routing from frontend.", "Build Microservices Architecture Console tab in React.", "Designed interactive card components for service health."],
        ["Day 7", "Built step-by-step pipeline runner in UI.", "Develop Live Wire Inspector JSON viewer.", "Integrated syntax highlighting for JSON response inspection."],
        ["Day 8", "Completed Microservices Console UI.", "Write Mockito integration tests for UserVerificationClient.", "Mocked RestTemplate response using MockRestServiceServer."],
        ["Day 9", "Executed full automated test suite.", "Verify all 22 tests passing with zero failures.", "All 22 unit, service, and controller tests passed."],
        ["Day 10", "Conducted final sprint review.", "Prepare project demonstration and retrospective.", "Sprint 3 completed on schedule; all deliverables verified."]
    ]
    add_styled_table(doc, scrum_s3_headers, scrum_s3_data, col_widths=[0.6, 1.9, 1.9, 2.2], 
                     caption="Table 2.16: Sprint 3 Daily Scrum Progress & Blocker Resolution Log (10 Days)")

    # 2.3.7 Committed vs Completed
    add_heading_3(doc, "2.3.7 Committed vs Completed User Stories")
    add_p(doc, "Sprint 3 committed 28 story points and delivered 28 story points (100% velocity realization). "
               "Table 2.17 details the sprint velocity, and Figure 2.12 illustrates the burndown chart.")
    
    cvc_s3_headers = ["User Story ID", "Summary", "Committed Points", "Completed Points", "Completion Status"]
    cvc_s3_data = [
        ["US-07", "Microservices Decoupling (Ports 8080 & 8081)", "8", "8", "COMPLETED"],
        ["US-08", "Inter-Service REST KYC Client with Fallback", "8", "8", "COMPLETED"],
        ["US-09", "Microservices Console & Live Wire Inspector", "5", "5", "COMPLETED"],
        ["US-10C", "End-to-End Distributed Integration Testing", "7", "7", "COMPLETED"],
        ["Total", "Sprint 3 Velocity Summary", "28", "28", "100% DELIVERED"]
    ]
    add_styled_table(doc, cvc_s3_headers, cvc_s3_data, col_widths=[1.2, 2.7, 1.1, 1.1, 1.1], 
                     caption="Table 2.17: Sprint 3 Committed vs Completed User Stories Breakdown")
    
    add_image_with_caption(doc, 'docs/screenshots/figure_2_3_burndown.png', 
                           "Figure 2.12: Sprint 3 Burndown Chart & Story Point Realization", width_inches=5.2)

    # 2.3.8 Retrospective
    add_heading_3(doc, "2.3.8 Sprint Retrospective")
    add_p(doc, "What Went Well: Microservice decoupling cleanly separated concerns. The circuit breaker fallback demonstrated high resilience "
               "during simulated user service outages. The interactive console proved invaluable for inspecting JSON wire contracts.\n"
               "What Could Be Improved: Service discovery is currently handled through static port URLs (localhost:8080/8081). In a multi-node "
               "production cluster, a dynamic discovery server (e.g., Netflix Eureka or Consul) and an API Gateway (Spring Cloud Gateway) would be advantageous.\n"
               "Action Items for Production Roadmap: Integrate Spring Cloud Gateway, implement containerization with Docker Compose, and transition "
               "from H2 in-memory stores to managed PostgreSQL clusters.")
    
    doc.add_page_break()
    print("Chapter 2 generated successfully.")

