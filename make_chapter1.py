import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
import os
from docx_helpers import (
    add_p, add_heading_1, add_heading_2, add_heading_3, add_heading_4,
    add_image_with_caption, add_styled_table
)

def build_chapter_1(doc):
    # ==========================================
    # CHAPTER 1: INTRODUCTION
    # ==========================================
    add_heading_1(doc, "CHAPTER 1\nINTRODUCTION")
    
    # 1.1 General (Introduction to Project)
    add_heading_2(doc, "1.1 General (Introduction to Project)")
    p1 = (
        "Suburban university campuses across India face substantial localized mobility challenges. "
        "At the Kattankulathur campus of SRM Institute of Science and Technology, over forty thousand "
        "students, faculty, and administrative staff navigate daily transit between instructional buildings, "
        "research laboratories, university entrance gates, and adjacent residential clusters. While inter-city "
        "and regional transit is partially serviced by suburban rail (Potheri Railway Station) and state bus "
        "routes along National Highway 45 (GST Road), the final one to four kilometers connecting primary campus "
        "gates—specifically Main Gate 1, Gate 2, Tech Park Gate, and the Central Library Block—to high-density "
        "student residential communities such as Estancia, Abode Valley, Green Pearl PG, and Potheri village "
        "relies almost exclusively on three-wheeled auto-rickshaws (TukTuks)."
    )
    add_p(doc, p1)
    
    p2 = (
        "Under the prevailing unorganized system, auto-rickshaw drivers negotiate fares on an ad-hoc basis, "
        "typically charging flat rates of ₹120 to ₹180 per trip regardless of passenger count. Because students "
        "exit academic blocks at varying intervals without a coordinated digital platform, they frequently hire "
        "vehicles individually. This results in heavy financial outlays for students, long queues of idling "
        "vehicles causing bottleneck congestion along institutional service roads, and heightened carbon "
        "emissions from underutilized vehicles. Autoshare is engineered as a responsive web platform to resolve "
        "this systemic inefficiency. By establishing an automated digital pooling marketplace, Autoshare enables "
        "students heading toward identical destinations to discover, coordinate, and share auto-rickshaw journeys, "
        "dynamically splitting transit fares and verifying university credentials to guarantee commuter safety."
    )
    add_p(doc, p2)

    # 1.2 Motivation
    add_heading_2(doc, "1.2 Motivation")
    p3 = (
        "The motivation behind engineering Autoshare stems from direct observation of daily campus transit "
        "friction across three primary dimensions: economic burden, physical congestion, and student security."
    )
    add_p(doc, p3)
    
    mots = [
        ("Economic Relief for Students: ", 
         "A student commuting twice daily between campus and residential quarters incurs monthly auto fares "
         "exceeding ₹4,500 when traveling alone. By pairing three students in a single vehicle, the individual fare "
         "drops to ₹40–₹60 per trip, generating direct savings of ₹2,500 to ₹3,200 per month per student. For an "
         "undergraduate population, these recurring savings represent meaningful economic relief."),
        ("Traffic Mitigation & Campus Ecology: ", 
         "During morning rush hours (07:30 to 08:45 AM) and evening dismissal (04:15 to 05:30 PM), hundreds of "
         "half-empty auto-rickshaws clog Gate 1 and the Potheri railway underpass. Consolidating commuters into "
         "shared three-passenger journeys directly reduces peak vehicle trips by up to 66%, easing traffic flow and "
         "lowering localized carbon emissions."),
        ("Institutional Trust & Safety: ", 
         "Ad-hoc ride sharing arranged verbally at roadside stands or unstructured messaging groups (e.g. WhatsApp "
         "or Telegram) lacks identity accountability. Students have no guarantee that co-passengers are legitimate "
         "campus members. Autoshare enforces institutional email verification (@srmist.edu.in) and registration number "
         "checks, establishing an authentic peer trust circle.")
    ]
    for lbl, desc in mots:
        p_m = doc.add_paragraph()
        p_m.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_m.paragraph_format.space_before = Pt(3)
        p_m.paragraph_format.space_after = Pt(4)
        p_m.paragraph_format.line_spacing = 1.3
        r_lbl = p_m.add_run(lbl)
        r_lbl.font.name = "Times New Roman"
        r_lbl.font.size = Pt(12)
        r_lbl.font.bold = True
        r_desc = p_m.add_run(desc)
        r_desc.font.name = "Times New Roman"
        r_desc.font.size = Pt(12)

    # 1.3 Problem Statement and Description
    add_heading_2(doc, "1.3 Problem Statement and Description")
    p4 = (
        "At institutional university campuses, students commuting between academic buildings and surrounding residential "
        "enclaves suffer from significant financial and logistical friction due to uncoordinated transport scheduling. "
        "The lack of a unified digital mobility board forces students to either pay full, inflated auto-rickshaw fares individually "
        "or spend ten to twenty minutes standing at campus exits attempting to verbally locate peers bound for the same destination. "
        "Existing commercial ride-hailing services (e.g., Uber, Ola) do not service localized short-distance TukTuk pooling "
        "within campus perimeters, nor do they support institutional student credential validation or split-fare calculations "
        "for cash/UPI spot settlement."
    )
    add_p(doc, p4)
    
    p5 = (
        "To systematically address this problem, the platform must satisfy three engineering requirements: first, provide "
        "a sub-second route discovery interface where commuters can post and search active journeys filtered by campus gate, "
        "destination hotspot, and departure window; second, implement an atomic transactional backend capable of recalculating "
        "proportional fare shares in real time as seats are booked, preventing over-allocation beyond legal three-passenger vehicle "
        "capacity; third, maintain a persistent, decoupled user management system that enforces institutional identity verification "
        "through Spring Data JPA and microservices architecture."
    )
    add_p(doc, p5)

    # 1.4 Sustainable Development Goals of the Project
    add_heading_2(doc, "1.4 Sustainable Development Goals of the Project")
    p6 = (
        "The technical design and real-world deployment of Autoshare directly align with three United Nations Sustainable "
        "Development Goals (UN SDGs):"
    )
    add_p(doc, p6)
    
    sdgs = [
        ("SDG 11: Sustainable Cities and Communities (Target 11.2): ",
         "Target 11.2 focuses on providing access to safe, affordable, accessible, and sustainable transport systems for all. "
         "Autoshare directly advances this objective in a university micro-city environment by optimizing vehicle occupancy, "
         "reducing gate-side gridlock, and making safe local transport economically accessible to all student demographics."),
        ("SDG 12: Responsible Consumption and Production (Target 12.2): ",
         "Target 12.2 emphasizes achieving the sustainable management and efficient use of natural resources. By multiplying "
         "the passenger-kilometer efficiency of auto-rickshaws, Autoshare minimizes fuel wastage caused by single-passenger trips, "
         "promoting shared asset utilization."),
        ("SDG 9: Industry, Innovation, and Infrastructure (Target 9.4): ",
         "Target 9.4 calls for upgraded infrastructure and retrofitted industries to make them sustainable, with increased "
         "resource-use efficiency and greater adoption of clean, environmentally sound technologies. Autoshare demonstrates "
         "this through a modern, cloud-native microservices architecture that can be scaled across other institutional campuses.")
    ]
    for s_title, s_desc in sdgs:
        p_s = doc.add_paragraph()
        p_s.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_s.paragraph_format.space_before = Pt(3)
        p_s.paragraph_format.space_after = Pt(4)
        p_s.paragraph_format.line_spacing = 1.3
        r_t = p_s.add_run(s_title)
        r_t.font.name = "Times New Roman"
        r_t.font.size = Pt(12)
        r_t.font.bold = True
        r_d = p_s.add_run(s_desc)
        r_d.font.name = "Times New Roman"
        r_d.font.size = Pt(12)

    # 1.5 Product Vision Statement
    add_heading_2(doc, "1.5 Product Vision Statement")
    
    add_heading_3(doc, "1.5.1 Target Audience")
    p_aud = (
        "The primary audience comprises undergraduate and postgraduate students enrolled at SRMIST Kattankulathur, "
        "including hostel residents (Pari, Kaveri, Paari, Oori blocks) traveling to rail stations and day scholars residing "
        "in private hostels and residential apartment complexes (Estancia, Abode Valley, Green Pearl, Valliammai enclave). "
        "The secondary audience includes faculty members, campus facilities management monitoring entrance gate traffic, and "
        "local auto-rickshaw driver unions benefiting from organized, predictable passenger queues."
    )
    add_p(doc, p_aud)
    
    add_heading_3(doc, "1.5.2 User Needs & Pain Points")
    p_needs = (
        "Commuters require rapid journey discovery without scrolling through hundreds of unorganized chat messages. Key needs include: "
        "(1) instantaneous route search by origin gate and destination hotspot; (2) transparent, automated fare split mathematics "
        "eliminating awkward monetary calculations at destination; (3) real-time seat availability meters showing remaining auto capacity; "
        "(4) identity guarantees ensuring co-passengers are enrolled university students; and (5) zero-friction mobile web accessibility "
        "without requiring heavy native app installations."
    )
    add_p(doc, p_needs)
    
    add_heading_3(doc, "1.5.3 Product Features & Ecosystem")
    p_feat = (
        "Autoshare delivers a unified web-based mobility platform consisting of four core modules: "
        "(1) Campus Rides Feed with instant hotspot filter chips; (2) Ride Offering Modal with dynamic per-seat fare previews; "
        "(3) Spring Data JPA User Management Console with role-based access control and status lifecycle toggles; and "
        "(4) Microservices Verification Console providing real-time wire tracing between independent microservice boundaries."
    )
    add_p(doc, p_feat)
    
    add_heading_3(doc, "1.5.4 Core Value Propositions")
    p_val = (
        "The system delivers value through three core engineering pillars: "
        "(1) Financial Economy: Guarantees fair, equal cost sharing where each added co-passenger strictly reduces individual expense; "
        "(2) Transactional Integrity: Employs ACID-compliant relational transactions preventing race conditions during concurrent seat claims; and "
        "(3) Architectural Resilience: Implements decoupled Spring Boot microservices with circuit breaker fallbacks, ensuring ride discovery "
        "remains operational even during intermittent user service maintenance."
    )
    add_p(doc, p_val)

    # 1.6 Product Goal
    add_heading_2(doc, "1.6 Product Goal")
    p_goal = (
        "The engineering goal of Autoshare is to deliver a production-grade, enterprise-ready campus mobility system with "
        "the following concrete technical and operational targets: "
        "(1) Sub-25 millisecond median latency for active ride queries and search filtering; "
        "(2) 100% mathematical consistency in dynamic fare division across all passenger states (1 to 3 co-passengers); "
        "(3) Strict identity enforcement restricting ride bookings to valid institutional email addresses (@srmist.edu.in); "
        "(4) Decoupled microservice architecture isolating user verification from the high-throughput ride-booking pipeline; and "
        "(5) High software reliability validated by an automated test suite achieving 100% pass rate across unit, repository, and controller layers."
    )
    add_p(doc, p_goal)

    # 1.7 Product Backlog
    add_heading_2(doc, "1.7 Product Backlog")
    p_bl = (
        "The product backlog was prioritized using the industry-standard MoSCoW framework (Must Have, Should Have, "
        "Could Have, Won't Have) and estimated in Agile story points using a modified Fibonacci scale. Development was "
        "organized into three two-week sprints. Table 1.1 delineates the master product backlog, while Figure 1.1 illustrates "
        "the backlog board and sprint allocation."
    )
    add_p(doc, p_bl)
    
    # Backlog Table
    bl_headers = ["ID", "User Story Summary", "Category", "MoSCoW", "Pts", "Sprint"]
    bl_data = [
        ["US-01", "As a host, I want to publish a ride offer with gate, destination, and fare.", "Ride Lifecycle", "Must Have", "5", "Sprint 1"],
        ["US-02", "As a commuter, I want to search and filter rides by route and hotspot.", "Discovery", "Must Have", "5", "Sprint 1"],
        ["US-03", "As a commuter, I want to book a seat and see the dynamic fare recalculated.", "Booking Engine", "Must Have", "8", "Sprint 1"],
        ["US-04", "As a student, I want to register a profile with registration number and email.", "Identity", "Must Have", "5", "Sprint 2"],
        ["US-05", "As an admin, I want to perform full CRUD on student records via Data JPA.", "Persistence", "Must Have", "8", "Sprint 2"],
        ["US-06", "As an admin, I want to search users via JPQL full-text multi-field queries.", "Search Engine", "Should Have", "5", "Sprint 2"],
        ["US-07", "As an architect, I want to decouple user mgmt into a standalone microservice.", "Architecture", "Must Have", "8", "Sprint 3"],
        ["US-08", "As an engine, I want to verify commuter KYC via inter-service REST with fallback.", "Resilience", "Must Have", "8", "Sprint 3"],
        ["US-09", "As a developer, I want an interactive system console with JSON wire inspection.", "Observability", "Should Have", "5", "Sprint 3"],
        ["US-10", "As a QA engineer, I want 20+ automated unit & integration tests passing 100%.", "Quality / Testing", "Must Have", "8", "Sprint 1-3"],
        ["US-11", "As a commuter, I want an in-app slide-over coordination chat drawer.", "Coordination", "Could Have", "5", "Sprint 1"],
        ["US-12", "As an admin, I want live campus savings KPIs and co-passenger counters.", "Analytics", "Could Have", "5", "Sprint 2"]
    ]
    add_styled_table(doc, bl_headers, bl_data, col_widths=[0.8, 2.7, 1.2, 0.9, 0.5, 0.7], 
                     caption="Table 1.1: Autoshare Product Backlog with MoSCoW Prioritization and Story Point Estimates")
    
    add_image_with_caption(doc, 'docs/screenshots/figure_1_1_ms_planner_board.png', 
                           "Figure 1.1: Autoshare Product Backlog and Sprint Board Allocation", width_inches=5.8)

    # 1.8 Product Release Plan
    add_heading_2(doc, "1.8 Product Release Plan")
    p_rp = (
        "The project release roadmap followed an iterative, incremental deployment plan spanning three discrete development "
        "phases. Release 1.0 established the foundational monolithic ride-pooling prototype, pairing the React 19 client with "
        "the Spring Boot ride-booking engine and in-memory persistence. Release 2.0 integrated the Spring Data JPA user management "
        "system, implementing complete CRUD capabilities, JPQL multi-field search queries, and relational schema validation. "
        "Release 3.0 completed the distributed transition by decoupling the architecture into independent microservices on ports "
        "8080 and 8081, connecting them via synchronous REST clients with circuit breaker fallbacks, and delivering the interactive "
        "microservices console. Figure 1.2 details the release cadence and timeline milestones."
    )
    add_p(doc, p_rp)
    
    add_image_with_caption(doc, 'docs/screenshots/figure_1_2_release_plan.png', 
                           "Figure 1.2: Autoshare Product Release Roadmap & Sprint Cadence", width_inches=5.8)
    
    doc.add_page_break()
    print("Chapter 1 generated successfully.")

