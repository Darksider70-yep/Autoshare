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
    
    # 1.1 General
    add_heading_2(doc, "1.1 General (Introduction to Project)")
    p1 = (
        "Suburban university campuses across India face substantial localized mobility challenges. "
        "At the Kattankulathur campus of SRM Institute of Science and Technology, over forty thousand "
        "students, faculty, and administrative staff navigate daily transit between instructional buildings, "
        "campus entrance gates (Main Gate 1, Gate 2, Tech Park Gate, Library Block), and adjacent residential clusters "
        "(Estancia, Abode Valley, Green Pearl PG, and Potheri Railway Station). While regional transit is serviced by "
        "suburban rail along GST Road (NH-45), the final one to four kilometers relies on three-wheeled auto-rickshaws (TukTuks). "
        "Prevailing unorganized auto-rickshaws charge flat rates of ₹120–₹180 per trip regardless of passenger count. "
        "Autoshare establishes an automated digital pooling marketplace, enabling students bound for identical destinations "
        "to discover, coordinate, and share rides, dynamically splitting transit fares down to ₹40–₹60 per seat while enforcing "
        "university credential verification to ensure commuter safety."
    )
    add_p(doc, p1, space_before=1, space_after=3, line_spacing=1.1)

    # 1.2 Motivation
    add_heading_2(doc, "1.2 Motivation")
    mots = [
        ("• Economic Relief: ", "Solo commuters incur monthly auto fares exceeding ₹4,500. Three-passenger pooling drops individual trip costs to ₹40–₹60, delivering direct student savings of ₹2,500 to ₹3,200 monthly."),
        ("• Traffic & Ecological Mitigation: ", "Consolidating solo rides into 3-passenger pools reduces campus gate vehicular volume by up to 66% during peak hours (07:30–08:45 AM, 04:15–05:30 PM), curbing congestion and emissions."),
        ("• Institutional Trust & Safety: ", "Informal roadside pooling lacks accountability. Autoshare enforces university email validation (@srmist.edu.in) and registration number verification, creating an authenticated peer trust circle.")
    ]
    for lbl, desc in mots:
        p_m = doc.add_paragraph()
        p_m.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_m.paragraph_format.space_before = Pt(0)
        p_m.paragraph_format.space_after = Pt(1)
        p_m.paragraph_format.line_spacing = 1.1
        r_lbl = p_m.add_run(lbl)
        r_lbl.font.name = "Times New Roman"
        r_lbl.font.size = Pt(10)
        r_lbl.font.bold = True
        r_desc = p_m.add_run(desc)
        r_desc.font.name = "Times New Roman"
        r_desc.font.size = Pt(10)

    # 1.3 Problem Statement
    add_heading_2(doc, "1.3 Problem Statement and Description")
    p4 = (
        "Lack of centralized transit scheduling forces students to either pay inflated solo fares or spend 15–20 minutes "
        "at campus gates verbally seeking co-passengers. Commercial aggregators do not service localized short-distance "
        "TukTuk pooling, nor do they support campus credential validation or spot split-fare settlements. "
        "Autoshare resolves this through: (1) a sub-second route discovery interface filtered by gate and destination; "
        "(2) an atomic transactional backend calculating dynamic proportional fare splits while enforcing the legal 3-passenger "
        "limit; and (3) a decoupled, persistent user identity architecture using Spring Data JPA and microservices."
    )
    add_p(doc, p4, space_before=1, space_after=3, line_spacing=1.1)

    # 1.4 SDGs
    add_heading_2(doc, "1.4 Sustainable Development Goals of the Project")
    p6 = (
        "Autoshare aligns with three United Nations Sustainable Development Goals (UN SDGs):\n"
        "• SDG 11 (Sustainable Cities - Target 11.2): Expands safe, affordable, accessible campus transit.\n"
        "• SDG 12 (Responsible Consumption - Target 12.2): Triples passenger-km efficiency, curbing fuel waste.\n"
        "• SDG 9 (Industry & Innovation - Target 9.4): Delivers a scalable cloud-native microservice architecture."
    )
    add_p(doc, p6, space_before=1, space_after=3, line_spacing=1.1)

    # 1.5 Product Vision
    add_heading_2(doc, "1.5 Product Vision Statement & Ecosystem")
    p_vis = (
        "Autoshare serves students, faculty, and administrators across three engineering pillars: (1) Financial Economy "
        "via dynamic proportional fare sharing; (2) Transactional Integrity via ACID relational transactions preventing "
        "overbooking; and (3) Architectural Resilience via independent Spring Boot microservices with circuit breaker fallback."
    )
    add_p(doc, p_vis, space_before=1, space_after=3, line_spacing=1.1)

    # 1.6 Product Goal
    add_heading_2(doc, "1.6 Product Goal")
    p_goal = (
        "Deliver a production-ready campus mobility platform achieving: sub-25 ms median REST latency, 100% mathematical precision "
        "in dynamic fare split calculations (1–3 co-passengers), strict @srmist.edu.in KYC verification, decoupled microservice "
        "boundaries (ports 8080 and 8081), and an automated test suite achieving 100% pass rate across all tiers."
    )
    add_p(doc, p_goal, space_before=1, space_after=4, line_spacing=1.1)

    # 1.7 Product Backlog
    add_heading_2(doc, "1.7 Product Backlog")
    p_bl = (
        "The master backlog was prioritized using MoSCoW and estimated in story points across three sprints. "
        "Table 1.1 delineates the backlog, and Figure 1.1 illustrates the client runtime in terminal."
    )
    add_p(doc, p_bl, space_before=1, space_after=3, line_spacing=1.1)
    
    bl_headers = ["ID", "User Story Summary", "Category", "MoSCoW", "Pts", "Sprint"]
    bl_data = [
        ["US-01", "Publish ride offer with gate, destination, capacity (1-3), and fare.", "Ride Lifecycle", "Must Have", "5", "Sprint 1"],
        ["US-02", "Search and filter active campus rides by route and destination hotspot.", "Discovery", "Must Have", "5", "Sprint 1"],
        ["US-03", "Atomic seat booking with dynamic proportional fare recalculation.", "Booking Engine", "Must Have", "8", "Sprint 1"],
        ["US-04", "Register student profile with SRM email, registration number, department.", "Identity", "Must Have", "5", "Sprint 2"],
        ["US-05", "Spring Data JPA CRUD management of student records with constraints.", "Persistence", "Must Have", "8", "Sprint 2"],
        ["US-06", "Multi-attribute full-text student search using custom JPQL queries.", "Search Engine", "Should Have", "5", "Sprint 2"],
        ["US-07", "Decouple backend into standalone microservices on isolated ports (8080/8081).", "Architecture", "Must Have", "8", "Sprint 3"],
        ["US-08", "Synchronous inter-service KYC verification client with circuit breaker fallback.", "Resilience", "Must Have", "8", "Sprint 3"],
        ["US-09", "Interactive Microservices Console with pipeline runner & JSON wire inspector.", "Observability", "Should Have", "5", "Sprint 3"],
        ["US-10", "Automated unit and integration test suite with 22 tests passing 100%.", "Quality / QA", "Must Have", "8", "Sprint 1-3"]
    ]
    add_styled_table(doc, bl_headers, bl_data, col_widths=[0.7, 3.0, 1.2, 0.9, 0.4, 0.7], 
                     caption="Table 1.1: Autoshare Product Backlog with MoSCoW Prioritization and Story Point Estimates")
    
    add_image_with_caption(doc, 'docs/screenshots/terminal_vite_frontend.png', 
                           "Figure 1.1: Vite Development Server and Local Reverse Proxy Initialized in Terminal", width_inches=4.0)

    # 1.8 Product Release Plan
    add_heading_2(doc, "1.8 Product Release Plan")
    p_rp = (
        "The project followed an incremental release plan across three development milestones: "
        "Release 1.0 established the monolithic ride-pooling engine with dynamic fare division in Spring Boot and React 19. "
        "Release 2.0 integrated Spring Data JPA user persistence, full CRUD operations, and JPQL search. "
        "Release 3.0 completed distributed decoupling into independent microservices on ports 8080 and 8081 with circuit breaker "
        "fallback and an interactive system console. Figure 1.2 shows the backend microservice startup and port binding in terminal."
    )
    add_p(doc, p_rp, space_before=1, space_after=3, line_spacing=1.1)
    
    add_image_with_caption(doc, 'docs/screenshots/terminal_spring_boot_startup.png', 
                           "Figure 1.2: Spring Boot 3.3.4 Microservice Bootstrap Execution and Port Binding in Terminal", width_inches=4.0)
    
    doc.add_page_break()
    print("Chapter 1 generated successfully.")
