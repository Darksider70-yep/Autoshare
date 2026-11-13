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
        "The development of Autoshare was executed using the Agile Scrum framework across three iterative two-week "
        "sprints (six weeks total). Each sprint executed core Scrum ceremonies: Sprint Planning, Sprint Backlog Refinement, "
        "Architecture & Interface Design, Automated Test Verification, and Retrospectives. The subsequent sections document "
        "the engineering execution, data models, test cases, and velocity metrics for Sprint 1, Sprint 2, and Sprint 3."
    )
    add_p(doc, p_intro, space_before=2, space_after=6, line_spacing=1.15)

    # =========================================================================
    # 2.1 SPRINT 1
    # =========================================================================
    add_heading_2(doc, "2.1 Sprint 1: Core Ride-Pooling Engine & Dynamic Fare Split System")
    
    # 2.1.1 Sprint Goal
    add_heading_3(doc, "2.1.1 Sprint Goal with User Stories of Sprint 1")
    p_s1_goal = (
        "Sprint 1 engineered the transactional ride-pooling pipeline and dynamic fare calculation engine. "
        "Goal: 'Implement ride publication, route discovery, dynamic fare calculation, and atomic seat reservation "
        "with a responsive React 19 frontend and Spring Boot 3.3.4 REST backend, validated by automated unit and API tests.' "
        "Table 2.1 itemizes the committed user stories."
    )
    add_p(doc, p_s1_goal, space_before=2, space_after=4, line_spacing=1.15)
    
    s1_us_headers = ["Story ID", "User Story Summary", "Acceptance Criteria", "Story Pts"]
    s1_us_data = [
        ["US-01", "Publish ride offer with pickup gate, destination, total seats (1-3), total fare, and departure time.", 
         "1. Gate must be official campus gate.\n2. Total seats restricted to 1–3 passengers.\n3. Positive total fare; status defaults to OPEN.", "5"],
        ["US-02", "Search and filter active campus rides by origin gate and destination hotspot.", 
         "1. Sub-second response time.\n2. Filter by hotspot (Estancia, Abode Valley, Potheri Stn).\n3. Only show OPEN rides.", "5"],
        ["US-03", "Book a seat on an open ride with dynamic proportional fare recalculation.", 
         "1. Atomic seat increment.\n2. Require valid @srmist.edu.in email.\n3. Disallow duplicate bookings.\n4. When full, transition to FULL.\n5. Fare = totalFare / (seatsTaken + 1).", "8"],
        ["US-10A", "Automated unit and integration tests validating ride creation, booking logic, and fare math.", 
         "1. 100% pass rate across RideService and RideController.\n2. Validate custom domain exception handling.", "6"]
    ]
    add_styled_table(doc, s1_us_headers, s1_us_data, col_widths=[0.8, 2.5, 2.6, 0.6], 
                     caption="Table 2.1: Sprint 1 Detailed User Stories and Acceptance Criteria")

    # 2.1.2 Functional Document
    add_heading_3(doc, "2.1.2 Functional Document")
    add_p(doc, "Scope: Ride offering by student hosts, journey discovery by commuters, and transactional seat reservations.\n"
               "Core Business Rules:\n"
               "1. Institutional Email: Commuter email must terminate with @srmist.edu.in.\n"
               "2. Vehicle Capacity Constraint: Total seats offered is capped at 3 (Bajaj auto-rickshaw capacity limit).\n"
               "3. Concurrency Protection: Over-booking beyond vehicle capacity is blocked at transaction boundaries.\n"
               "4. Duplicate Booking Prevention: Re-booking the same ride by the same email throws DuplicateBookingException.\n"
               "5. Dynamic Fare Split: Fare per person = totalFare / (seatsTaken + 1), where '+1' accounts for the host.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    auth_s1_headers = ["User Role", "Publish Ride", "Search / View Rides", "Book Seat", "Cancel Ride", "System Admin"]
    auth_s1_data = [
        ["Guest Commuter", "Denied", "Allowed (Read Only)", "Denied (Login Required)", "Denied", "Denied"],
        ["Verified Student", "Allowed", "Allowed", "Allowed", "Own Rides Only", "Denied"],
        ["Ride Host", "Allowed", "Allowed", "Allowed", "Own Rides Only", "Denied"],
        ["Administrator", "Allowed", "Allowed", "Allowed", "Allowed (Override)", "Full Access"]
    ]
    add_styled_table(doc, auth_s1_headers, auth_s1_data, col_widths=[1.5, 1.0, 1.3, 1.3, 1.0, 0.9], 
                     caption="Table 2.2: Sprint 1 Role-Based Access Control Authorization Matrix")

    # 2.1.3 Architecture Document
    add_heading_3(doc, "2.1.3 Architecture Document")
    add_p(doc, "Sprint 1 established a Three-Tier Layered Architecture: Presentation Layer (RideController, GlobalExceptionHandler), "
               "Business Service Layer (RideService, BookingService), and Data Access Layer (RideRepository, BookingRepository) "
               "backed by an in-memory H2 database. Table 2.3 defines the REST API contract.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    api_s1_headers = ["HTTP Verb", "Endpoint URI", "Payload / Params", "Status", "Functionality"]
    api_s1_data = [
        ["GET", "/api/rides", "Optional: destination, gate", "200 OK", "Fetches active rides matching criteria"],
        ["GET", "/api/rides/{id}", "Path: id (Long)", "200 OK", "Retrieves complete details of single ride"],
        ["POST", "/api/rides", "JSON: host, gate, dest, fare, seats, time", "201 Created", "Creates new ride in OPEN status"],
        ["POST", "/api/rides/{id}/book", "JSON: studentName, studentEmail", "201 Created", "Reserves seat and recalculates fare split"],
        ["GET", "/api/rides/{id}/fare-split", "Path: id (Long)", "200 OK", "Returns dynamic fare split breakdown"]
    ]
    add_styled_table(doc, api_s1_headers, api_s1_data, col_widths=[0.9, 1.8, 1.8, 0.9, 1.6], 
                     caption="Table 2.3: Sprint 1 Core REST API Contract Specification")

    # 2.1.4 UI Design
    add_heading_3(doc, "2.1.4 UI Design")
    add_p(doc, "Constructed with React 19 and Vite 6, the user interface incorporates modular components with responsive "
               "route cards, live capacity meters, interactive post-ride modals, slide-over chat drawers, and H2 database console.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    add_image_with_caption(doc, 'docs/screenshots/real_browser_landing.png', 
                           "Figure 2.1: Autoshare Live React 19 Client Landing Page & Campus Rides Feed (Captured in Browser)", width_inches=3.8)
    add_image_with_caption(doc, 'docs/screenshots/real_browser_post_ride_modal.png', 
                           "Figure 2.2: Live Post Ride Modal with Real-Time Proportional Fare Split Estimator (Captured in Browser)", width_inches=3.8)
    add_image_with_caption(doc, 'docs/screenshots/real_browser_chat_drawer.png', 
                           "Figure 2.3: Live Peer Coordination Chat Drawer for Real-Time Commuter Communication (Captured in Browser)", width_inches=3.8)
    add_image_with_caption(doc, 'docs/screenshots/04_h2_database_console.png', 
                           "Figure 2.4: In-Memory H2 Relational Database Web Console and Schema Tables", width_inches=3.8)

    # 2.1.5 Functional Test Cases
    add_heading_3(doc, "2.1.5 Functional Test Cases")
    add_p(doc, "Functional validation in Sprint 1 covered boundary checks and transaction rules. Table 2.4 summarizes the test results.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    tc_s1_headers = ["Test ID", "Scenario", "Input Parameters", "Expected Result", "Actual", "Status"]
    tc_s1_data = [
        ["TC-S1-01", "Create Ride Valid", "Host: 'Daksh', Gate 1, Dest: Estancia, Fare: 120, Seats: 3", "HTTP 201 Created; status=OPEN", "As expected", "PASS"],
        ["TC-S1-02", "Invalid Capacity", "Seats: 5 (exceeds vehicle limit 3)", "HTTP 400 Bad Request; validation failed", "As expected", "PASS"],
        ["TC-S1-03", "Atomic Seat Claim", "Ride ID: 1, 'rohit@srmist.edu.in'", "HTTP 201 Created; seatsTaken=1; fare=60.0", "As expected", "PASS"],
        ["TC-S1-04", "Invalid Domain", "Ride ID: 1, 'rohit@gmail.com'", "HTTP 400 Bad Request; invalid campus domain", "As expected", "PASS"],
        ["TC-S1-05", "Duplicate Booking", "Ride ID: 1, re-booking same student", "HTTP 409 Conflict; DuplicateBookingException", "As expected", "PASS"],
        ["TC-S1-06", "Auto Transition FULL", "Book remaining seats until capacity exhausted", "HTTP 201 Created; ride status becomes FULL", "As expected", "PASS"]
    ]
    add_styled_table(doc, tc_s1_headers, tc_s1_data, col_widths=[0.8, 1.4, 1.6, 1.5, 0.8, 0.5], 
                     caption="Table 2.4: Sprint 1 Functional Test Cases (TC-S1-01 to TC-S1-06)")

    # 2.1.6 Daily Call Progress
    add_heading_3(doc, "2.1.6 Daily Call Progress")
    add_p(doc, "Sprint 1 execution spanned 10 working days, tracked through daily standup meetings. Table 2.5 outlines the key milestones.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    scrum_s1_headers = ["Sprint Phase", "Days", "Core Tasks Completed", "Impediments Encountered & Resolutions"]
    scrum_s1_data = [
        ["Phase 1: Environment & Modeling", "Days 1–2", "Configured Spring Boot 3.3.4, defined Ride and Booking JPA models.", "Resolved Jakarta persistence package imports in Spring Boot 3."],
        ["Phase 2: Repositories & Services", "Days 3–4", "Implemented RideRepository, BookingRepository, and RideServiceImpl.", "Initialized child collection lists eagerly to eliminate NullPointerExceptions."],
        ["Phase 3: Fare Split Algorithm", "Days 5–6", "Developed dynamic proportional fare division formula and REST endpoints.", "Vite CORS blocked by backend port 8080; resolved via Vite proxy."],
        ["Phase 4: Client Componentry", "Days 7–8", "Constructed React 19 HeroSearch, RidesFeed, and PostRideModal.", "Modal focus trap resolved using keydown event listener in useEffect."],
        ["Phase 5: Testing & Review", "Days 9–10", "Wrote 10 JUnit 5 / Mockito unit tests; conducted sprint demo.", "Sprint goal achieved with 100% velocity realization (24/24 pts)."]
    ]
    add_styled_table(doc, scrum_s1_headers, scrum_s1_data, col_widths=[1.5, 0.8, 2.7, 2.0], 
                     caption="Table 2.5: Sprint 1 Agile Execution Milestones and Blocker Resolution Log")

    # 2.1.7 Committed vs Completed
    add_heading_3(doc, "2.1.7 Committed vs Completed User Stories")
    add_p(doc, "Sprint 1 committed 24 story points and delivered 24 story points (100% velocity realization). "
               "Table 2.6 summarizes velocity metrics, and Figure 2.5 displays the terminal wire trace of the dynamic fare API.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    cvc_s1_headers = ["User Story ID", "Summary", "Committed Pts", "Completed Pts", "Status"]
    cvc_s1_data = [
        ["US-01", "Publish Ride Offer", "5", "5", "COMPLETED"],
        ["US-02", "Search and Filter Active Rides", "5", "5", "COMPLETED"],
        ["US-03", "Dynamic Fare Split & Seat Claim", "8", "8", "COMPLETED"],
        ["US-10A", "Sprint 1 Automated Unit Testing", "6", "6", "COMPLETED"],
        ["Total", "Sprint 1 Velocity Summary", "24", "24", "100% DELIVERED"]
    ]
    add_styled_table(doc, cvc_s1_headers, cvc_s1_data, col_widths=[1.2, 2.7, 1.1, 1.1, 1.1], 
                     caption="Table 2.6: Sprint 1 Committed vs Completed User Stories Breakdown")
    
    add_image_with_caption(doc, 'docs/screenshots/terminal_rest_api_wire_trace.png', 
                           "Figure 2.5: Terminal Wire Trace of Sprint 1 HTTP REST Booking and Dynamic Fare Recalculation API", width_inches=3.8)

    # 2.1.8 Retrospective
    add_heading_3(doc, "2.1.8 Sprint Retrospective")
    add_p(doc, "• What Went Well: Dynamic split engine demonstrated mathematical precision; React 19 hooks provided reactive updates.\n"
               "• What Could Be Improved: In-memory store lacked persistent user profile auditing across restarts.\n"
               "• Action Items for Sprint 2: Engineer Spring Data JPA User Record Management with institutional registration number verification.",
          space_before=2, space_after=6, line_spacing=1.15)

    # =========================================================================
    # 2.2 SPRINT 2
    # =========================================================================
    add_heading_2(doc, "2.2 Sprint 2: Spring Data JPA User Record Management & Persistence")
    
    # 2.2.1 Sprint Goal
    add_heading_3(doc, "2.2.1 Sprint Goal with User Stories of Sprint 2")
    p_s2_goal = (
        "Sprint 2 focused on creating a persistent relational user identity management module. "
        "Goal: 'Design, implement, and test persistent domain entities, Spring Data JPA repositories with custom JPQL queries, "
        "a transactional user service layer with full CRUD, and an interactive React management interface.' Table 2.7 outlines Sprint 2 stories."
    )
    add_p(doc, p_s2_goal, space_before=2, space_after=4, line_spacing=1.15)
    
    s2_us_headers = ["Story ID", "User Story Summary", "Acceptance Criteria", "Story Pts"]
    s2_us_data = [
        ["US-04", "Register persistent profile with full name, SRM email, registration number, department.", 
         "1. Email must match @srmist.edu.in.\n2. Registration regex (^RA[0-9]{13}$).\n3. Default status ACTIVE.", "5"],
        ["US-05", "Campus administrator full CRUD operations on user records via Spring Data JPA.", 
         "1. Complete CRUD endpoints.\n2. Disallow duplicate email or reg number.\n3. AccountStatus lifecycle management.", "8"],
        ["US-06", "Multi-attribute search across user records using custom JPQL queries.", 
         "1. Case-insensitive search across name, email, reg number.\n2. Filter by department.\n3. Sub-20 ms latency.", "5"],
        ["US-10B", "Comprehensive unit and MockMvc integration tests for JPA repositories, services, and controllers.", 
         "1. 100% test pass rate across UserService and UserController.\n2. Verify rollback on transaction failure.", "8"]
    ]
    add_styled_table(doc, s2_us_headers, s2_us_data, col_widths=[0.8, 2.5, 2.6, 0.6], 
                     caption="Table 2.7: Sprint 2 Detailed User Stories and Acceptance Criteria")

    # 2.2.2 Functional Document
    add_heading_3(doc, "2.2.2 Functional Document")
    add_p(doc, "Scope: Persistent student and host profiles, institutional KYC auditing, and role-based permissions.\n"
               "Account Lifecycle Management: PENDING_VERIFICATION -> ACTIVE -> SUSPENDED.\n"
               "Authorization: Verified students may read and update own profile; Administrators have full CRUD and status mutation rights.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    auth_s2_headers = ["Operation", "Anonymous Visitor", "Student / Host", "Administrator"]
    auth_s2_data = [
        ["Register Profile", "Allowed", "Allowed (Self Update)", "Allowed"],
        ["View Own Record", "Denied", "Allowed", "Allowed"],
        ["Search User Directory", "Denied", "Allowed (Basic Info)", "Allowed (Full Record)"],
        ["Update Status (ACTIVE/SUSPENDED)", "Denied", "Denied", "Allowed"],
        ["Delete User Record", "Denied", "Denied", "Allowed"]
    ]
    add_styled_table(doc, auth_s2_headers, auth_s2_data, col_widths=[2.2, 1.4, 1.8, 1.8], 
                     caption="Table 2.8: Sprint 2 User Identity Authorization Matrix")

    # 2.2.3 Architecture Document
    add_heading_3(doc, "2.2.3 Architecture Document")
    add_p(doc, "Architected using Spring Data JPA with Hibernate ORM, automatic auditing (@CreationTimestamp, @UpdateTimestamp), "
               "and parameterized JPQL search. Table 2.9 details the User Service REST contract.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    api_s2_headers = ["HTTP Verb", "Endpoint URI", "Payload / Params", "Status", "Functionality"]
    api_s2_data = [
        ["GET", "/api/users", "None", "200 OK", "Returns all persistent user records"],
        ["GET", "/api/users/{id}", "Path: id (Long)", "200 OK", "Retrieves single user by primary key"],
        ["GET", "/api/users/search", "Query: q (String)", "200 OK", "Executes multi-field JPQL LIKE search"],
        ["POST", "/api/users", "JSON: fullName, email, regNumber, department", "201 Created", "Persists new user record"],
        ["PUT", "/api/users/{id}", "JSON: updated user details", "200 OK", "Performs entity update with validation"],
        ["DELETE", "/api/users/{id}", "Path: id (Long)", "204 No Content", "Deletes user record by primary key"],
        ["PATCH", "/api/users/{id}/status", "JSON: status (ACTIVE/SUSPENDED)", "200 OK", "Mutates account status"],
        ["GET", "/api/users/verify/{email}", "Path: email (String)", "200 OK", "Verifies student KYC eligibility"]
    ]
    add_styled_table(doc, api_s2_headers, api_s2_data, col_widths=[0.9, 1.8, 1.8, 0.9, 1.6], 
                     caption="Table 2.9: Sprint 2 Spring Data JPA User Service REST API Contract")

    # 2.2.4 UI Design
    add_heading_3(doc, "2.2.4 UI Design")
    add_p(doc, "A dedicated 'User Records' management console was integrated into React 19, featuring live full-text search, "
               "role filter pills, account status badges (green for ACTIVE, amber for SUSPENDED), and modal dialogs.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    add_image_with_caption(doc, 'docs/screenshots/06_unit5_spring_boot_jpa_startup.png', 
                           "Figure 2.6: Spring Boot Data JPA Microservice Startup Banner and Port Binding", width_inches=3.8)
    add_image_with_caption(doc, 'docs/screenshots/07_unit5_crud_rest_apis_execution.png', 
                           "Figure 2.7: Execution and Terminal Verification of Spring Data JPA User CRUD REST Endpoints", width_inches=3.8)
    add_image_with_caption(doc, 'docs/screenshots/real_browser_user_records.png', 
                           "Figure 2.8: Interactive User Record Management Dashboard in React 19 Frontend (Captured in Browser)", width_inches=3.8)

    # 2.2.5 Functional Test Cases
    add_heading_3(doc, "2.2.5 Functional Test Cases")
    add_p(doc, "Testing verified user persistence, unique constraints, and JPQL search. Table 2.10 compiles the executed tests.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    tc_s2_headers = ["Test ID", "Scenario", "Input Parameters", "Expected Result", "Actual", "Status"]
    tc_s2_data = [
        ["TC-S2-01", "Create User Valid", "Daksh, daksh.g@srmist.edu.in, RA2411003012297", "HTTP 201 Created; status=ACTIVE", "As expected", "PASS"],
        ["TC-S2-02", "Duplicate Email", "Re-register existing email", "HTTP 409 Conflict; DuplicateEmailException", "As expected", "PASS"],
        ["TC-S2-03", "Invalid Reg Number", "RegNumber: '12345' (invalid regex)", "HTTP 400 Bad Request; validation failed", "As expected", "PASS"],
        ["TC-S2-04", "JPQL Search Query", "Query: 'RA2411' or 'daksh'", "HTTP 200 OK; returns matching record", "As expected", "PASS"],
        ["TC-S2-05", "Update Department", "PUT /api/users/1 with new department", "HTTP 200 OK; department updated in DB", "As expected", "PASS"],
        ["TC-S2-06", "Patch Account Status", "PATCH /api/users/1/status with SUSPENDED", "HTTP 200 OK; status=SUSPENDED in DB", "As expected", "PASS"],
        ["TC-S2-07", "Delete User by ID", "DELETE /api/users/1", "HTTP 204 No Content; record purged from DB", "As expected", "PASS"]
    ]
    add_styled_table(doc, tc_s2_headers, tc_s2_data, col_widths=[0.8, 1.4, 1.6, 1.5, 0.8, 0.5], 
                     caption="Table 2.10: Sprint 2 Functional Test Cases (TC-S2-01 to TC-S2-07)")

    # 2.2.6 Daily Call Progress
    add_heading_3(doc, "2.2.6 Daily Call Progress")
    add_p(doc, "Sprint 2 progressed through five Scrum execution phases over 10 working days, summarized in Table 2.11.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    scrum_s2_headers = ["Sprint Phase", "Days", "Core Tasks Completed", "Impediments Encountered & Resolutions"]
    scrum_s2_data = [
        ["Phase 1: JPA Entity & Validation", "Days 1–2", "Defined User entity with Jakarta validation and AccountStatus enum.", "Configured Hibernate DDL auto-update and schema initialization."],
        ["Phase 2: Repositories & JPQL", "Days 3–4", "Implemented UserRepository with derived queries and JPQL multi-field search.", "Fixed JPQL syntax error using LOWER() with CONCAT for wildcard LIKE."],
        ["Phase 3: Service CRUD & Handlers", "Days 5–6", "Developed UserServiceImpl with transactional CRUD and global exception advice.", "Configured RFC-7807 problem details in error JSON payloads."],
        ["Phase 4: Client Administration UI", "Days 7–8", "Constructed User Records React data table and Add/Edit User modal dialogs.", "Synchronized form state with parent data table via callback hook."],
        ["Phase 5: JPA Test Suite Execution", "Days 9–10", "Wrote 12 Mockito and MockMvc tests; conducted sprint review.", "Sprint 2 goals met with 100% velocity realization (26/26 pts)."]
    ]
    add_styled_table(doc, scrum_s2_headers, scrum_s2_data, col_widths=[1.5, 0.8, 2.7, 2.0], 
                     caption="Table 2.11: Sprint 2 Agile Execution Milestones and Blocker Resolution Log")

    # 2.2.7 Committed vs Completed
    add_heading_3(doc, "2.2.7 Committed vs Completed User Stories")
    add_p(doc, "Sprint 2 committed 26 story points and delivered 26 story points (100% velocity realization). "
               "Table 2.12 outlines the completed user stories, and Figure 2.9 illustrates the terminal JPQL search execution.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    cvc_s2_headers = ["User Story ID", "Summary", "Committed Pts", "Completed Pts", "Status"]
    cvc_s2_data = [
        ["US-04", "Student Profile Registration", "5", "5", "COMPLETED"],
        ["US-05", "Spring Data JPA CRUD Operations", "8", "8", "COMPLETED"],
        ["US-06", "JPQL Multi-Field Full-Text Search", "5", "5", "COMPLETED"],
        ["US-10B", "Sprint 2 Automated Unit & Integration Testing", "8", "8", "COMPLETED"],
        ["Total", "Sprint 2 Velocity Summary", "26", "26", "100% DELIVERED"]
    ]
    add_styled_table(doc, cvc_s2_headers, cvc_s2_data, col_widths=[1.2, 2.7, 1.1, 1.1, 1.1], 
                     caption="Table 2.12: Sprint 2 Committed vs Completed User Stories Breakdown")
    
    add_image_with_caption(doc, 'docs/screenshots/terminal_user_jpql_search.png', 
                           "Figure 2.9: Terminal Execution and Hibernate SQL Trace of Spring Data JPA JPQL Multi-Field Search", width_inches=3.8)

    # 2.2.8 Retrospective
    add_heading_3(doc, "2.2.8 Sprint Retrospective")
    add_p(doc, "• What Went Well: Spring Data JPA simplified data access; JPQL multi-field search executed under 15 ms.\n"
               "• What Could Be Improved: Single monolithic JVM instance binds high booking traffic with KYC validation.\n"
               "• Action Items for Sprint 3: Decouple into independent microservices on ports 8080 and 8081 with circuit breaker fallback.",
          space_before=2, space_after=6, line_spacing=1.15)

    # =========================================================================
    # 2.3 SPRINT 3
    # =========================================================================
    add_heading_2(doc, "2.3 Sprint 3: Microservices Architecture, Inter-Service REST & Console")
    
    # 2.3.1 Sprint Goal
    add_heading_3(doc, "2.3.1 Sprint Goal with User Stories of Sprint 3")
    p_s3_goal = (
        "Sprint 3 decoupled the platform into independent microservices with fault-tolerant REST communication. "
        "Goal: 'Decouple backend into user-management-service (port 8081) and ride-booking-service (port 8080), establish "
        "synchronous inter-service REST calls with circuit breaker fallback, and build an interactive system console in React 19.' "
        "Table 2.13 outlines Sprint 3 stories."
    )
    add_p(doc, p_s3_goal, space_before=2, space_after=4, line_spacing=1.15)
    
    s3_us_headers = ["Story ID", "User Story Summary", "Acceptance Criteria", "Story Pts"]
    s3_us_data = [
        ["US-07", "Decouple backend into standalone microservices running on isolated ports.", 
         "1. user-service on port 8081.\n2. ride-service on port 8080.\n3. Reverse proxy handles frontend routing.", "8"],
        ["US-08", "Verify commuter KYC via synchronous REST call to user service with fallback.", 
         "1. GET /api/users/verify/{email}.\n2. 1500 ms timeout.\n3. Graceful fallback on user service outage.", "8"],
        ["US-09", "Interactive Microservices Console in UI with step runner and wire inspector.", 
         "1. 4-step pipeline runner.\n2. Live display of wire JSON payloads.\n3. Service health status indicators.", "5"],
        ["US-10C", "End-to-end integration tests verifying inter-service communication and full suite.", 
         "1. Comprehensive test suite with 22 tests passing 100%.\n2. Verified fallback under simulated outage.", "7"]
    ]
    add_styled_table(doc, s3_us_headers, s3_us_data, col_widths=[0.8, 2.5, 2.6, 0.6], 
                     caption="Table 2.13: Sprint 3 Detailed User Stories and Acceptance Criteria")

    # 2.3.2 Functional Document
    add_heading_3(doc, "2.3.2 Functional Document")
    add_p(doc, "Scope: Physical segregation of bounded contexts: user-management-service (port 8081) and ride-booking-service (port 8080).\n"
               "Inter-Service Workflow:\n"
               "1. Commuter initiates booking: POST /api/rides/{id}/book on port 8080.\n"
               "2. RideService dispatches HTTP GET to UserVerificationClient on port 8081: /api/users/verify/{email}.\n"
               "3. If verified, booking is confirmed and dynamic fare split recalculated.\n"
               "4. Circuit Breaker Fallback: If port 8081 is unreachable or exceeds 1500 ms timeout, a provisional booking is permitted "
               "with an alert warning, ensuring high availability.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    add_styled_table(doc, 
                     ["Microservice Boundary", "Port", "Database Store", "Exposed APIs", "Inter-Service Dependency"],
                     [["user-management-service", "8081", "H2 (users table)", "/api/users/**, /api/users/verify/**", "None (Self-contained)"],
                      ["ride-booking-service", "8080", "H2 (rides, bookings)", "/api/rides/**, /api/bookings/**", "Calls port 8081 for KYC"],
                      ["autoshare-react-client", "3000", "Browser Local State", "Reverse proxy /api/rides & /api/users", "Consumes both services via proxy"]],
                     col_widths=[1.6, 0.7, 1.4, 1.8, 1.5],
                     caption="Table 2.14: Sprint 3 Microservices Inter-Service REST Contract & Architecture Boundaries")

    # 2.3.3 Architecture Document
    add_heading_3(doc, "2.3.3 Architecture Document")
    add_p(doc, "The microservices architecture employs a reverse proxy topology. Vite proxies /api/rides to 8080 and /api/users to 8081. "
               "Inter-service calls use UserVerificationClient wrapping RestTemplateBuilder with connect and read timeouts (1500 ms) "
               "and try-catch fallback returning UserVerificationResponse.builder().verified(true).provisional(true).build().",
          space_before=2, space_after=4, line_spacing=1.15)

    # 2.3.4 UI Design
    add_heading_3(doc, "2.3.4 UI Design")
    add_p(doc, "The 'Microservices Console' tab allows developers to execute a live 4-step distributed transaction: Step 1 (KYC Check), "
               "Step 2 (Fetch Rides), Step 3 (Atomic Seat Claim), and Step 4 (Fare Recalculation), with a Live Wire Inspector showing JSON payloads.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    add_image_with_caption(doc, 'docs/screenshots/08_unit5_microservices_inter_service_trace.png', 
                           "Figure 2.10: Inter-Service HTTP REST Trace between Ride Service (8080) and User Service (8081)", width_inches=3.8)
    add_image_with_caption(doc, 'docs/screenshots/real_browser_microservices_console.png', 
                           "Figure 2.11: Microservices Architecture Console with Step-by-Step Pipeline Runner & Wire Inspector (Captured in Browser)", width_inches=3.8)

    # 2.3.5 Functional Test Cases
    add_heading_3(doc, "2.3.5 Functional Test Cases")
    add_p(doc, "Sprint 3 verified inter-service communication and fallback handling. Table 2.15 itemizes the test results.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    tc_s3_headers = ["Test ID", "Scenario", "Input Parameters", "Expected Result", "Actual", "Status"]
    tc_s3_data = [
        ["TC-S3-01", "KYC Verified", "GET /api/users/verify/daksh.g@srmist.edu.in", "HTTP 200 OK; verified=true", "As expected", "PASS"],
        ["TC-S3-02", "KYC Unregistered", "GET /api/users/verify/unknown@srmist.edu.in", "HTTP 404 Not Found; verified=false", "As expected", "PASS"],
        ["TC-S3-03", "Suspended Account", "Booking attempt by SUSPENDED user", "HTTP 403 Forbidden; 'Account suspended'", "As expected", "PASS"],
        ["TC-S3-04", "Circuit Breaker Fallback", "Port 8081 stopped; book seat on port 8080", "HTTP 201 Created; provisional=true warning", "As expected", "PASS"],
        ["TC-S3-05", "Proxy Routing 8080", "GET /api/rides via port 3000", "Proxied to :8080; HTTP 200 OK", "As expected", "PASS"],
        ["TC-S3-06", "Proxy Routing 8081", "GET /api/users via port 3000", "Proxied to :8081; HTTP 200 OK", "As expected", "PASS"],
        ["TC-S3-07", "Console Pipeline", "Execute all 4 steps sequentially", "All 4 steps green; JSON payloads displayed", "As expected", "PASS"],
        ["TC-S3-08", "Full Regression Suite", "Run Maven test across all modules", "22 tests executed; 0 failures; 0 errors", "As expected", "PASS"]
    ]
    add_styled_table(doc, tc_s3_headers, tc_s3_data, col_widths=[0.8, 1.4, 1.6, 1.5, 0.8, 0.5], 
                     caption="Table 2.15: Sprint 3 Functional Test Cases (TC-S3-01 to TC-S3-08)")

    # 2.3.6 Daily Call Progress
    add_heading_3(doc, "2.3.6 Daily Call Progress")
    add_p(doc, "Sprint 3 executed across five distributed Scrum phases over 10 working days, as detailed in Table 2.16.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    scrum_s3_headers = ["Sprint Phase", "Days", "Core Tasks Completed", "Impediments Encountered & Resolutions"]
    scrum_s3_data = [
        ["Phase 1: Service Decoupling", "Days 1–2", "Separated backend into standalone modules on ports 8080 and 8081.", "Resolved port collision by configuring distinct server.port properties."],
        ["Phase 2: Inter-Service Client", "Days 3–4", "Implemented UserVerificationClient with RestTemplateBuilder.", "Handled connection timeouts by setting 1500 ms read timeout limits."],
        ["Phase 3: Circuit Breaker Fallback", "Days 5–6", "Integrated graceful degradation permitting provisional bookings on outage.", "Verified thread resilience during simulated user service shutdown."],
        ["Phase 4: Console UI & Inspector", "Days 7–8", "Built Microservices Console tab with 4-step runner and live wire inspector.", "Added JSON syntax highlighting for raw wire payloads."],
        ["Phase 5: Full Regression Testing", "Days 9–10", "Executed automated regression suite (22 tests); completed sprint demo.", "Sprint 3 goals achieved with 100% velocity realization (28/28 pts)."]
    ]
    add_styled_table(doc, scrum_s3_headers, scrum_s3_data, col_widths=[1.5, 0.8, 2.7, 2.0], 
                     caption="Table 2.16: Sprint 3 Agile Execution Milestones and Blocker Resolution Log")

    # 2.3.7 Committed vs Completed
    add_heading_3(doc, "2.3.7 Committed vs Completed User Stories")
    add_p(doc, "Sprint 3 committed 28 story points and delivered 28 story points (100% velocity realization). "
               "Table 2.17 details sprint velocity, and Figure 2.12 displays the terminal trace of the inter-service call.",
          space_before=2, space_after=4, line_spacing=1.15)
    
    cvc_s3_headers = ["User Story ID", "Summary", "Committed Pts", "Completed Pts", "Status"]
    cvc_s3_data = [
        ["US-07", "Microservices Decoupling (Ports 8080 & 8081)", "8", "8", "COMPLETED"],
        ["US-08", "Inter-Service REST KYC Client with Fallback", "8", "8", "COMPLETED"],
        ["US-09", "Microservices Console & Live Wire Inspector", "5", "5", "COMPLETED"],
        ["US-10C", "End-to-End Distributed Integration Testing", "7", "7", "COMPLETED"],
        ["Total", "Sprint 3 Velocity Summary", "28", "28", "100% DELIVERED"]
    ]
    add_styled_table(doc, cvc_s3_headers, cvc_s3_data, col_widths=[1.2, 2.7, 1.1, 1.1, 1.1], 
                     caption="Table 2.17: Sprint 3 Committed vs Completed User Stories Breakdown")
    
    add_image_with_caption(doc, 'docs/screenshots/terminal_interservice_rest_trace.png', 
                           "Figure 2.12: Microservices Synchronous Inter-Service REST Trace and Circuit Breaker Verification in Terminal", width_inches=3.8)

    # 2.3.8 Retrospective
    add_heading_3(doc, "2.3.8 Sprint Retrospective")
    add_p(doc, "• What Went Well: Microservices cleanly segregated domain concerns; circuit breaker fallback proved resilient under outages.\n"
               "• What Could Be Improved: Service endpoints rely on static port URLs rather than dynamic service discovery.\n"
               "• Production Roadmap: Integrate Spring Cloud Gateway, Docker Compose containerization, and managed PostgreSQL.",
          space_before=2, space_after=6, line_spacing=1.15)
    
    doc.add_page_break()
    print("Chapter 2 generated successfully.")
