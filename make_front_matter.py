import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
import os
from docx_helpers import (
    add_p, add_heading_1, add_heading_2, add_heading_3, 
    set_cell_margins, set_cell_shading, set_table_borders
)

def build_front_matter(doc):
    # ==========================================
    # 1. COVER PAGE / TITLE PAGE
    # ==========================================
    add_p(doc, "AUTOSHARE: CAMPUS RIDE-POOLING AND MOBILITY PLATFORM WITH MICROSERVICES ARCHITECTURE", 
          size_pt=18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=12, line_spacing=1.3)
    
    add_p(doc, "Course Code: 21CSP401L — Major Project / Full Stack Web Development", 
          size_pt=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=24)
    
    add_p(doc, "Submitted by", 
          size_pt=13, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=6)
    
    add_p(doc, "DAKSH GEHLOT [RA2411003012297]", 
          size_pt=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=24)
    
    add_p(doc, "Under the Guidance of", 
          size_pt=13, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=6)
    
    add_p(doc, "Dr. M. S. ABIRAMI, M.Tech., Ph.D.", 
          size_pt=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=2)
    add_p(doc, "Associate Professor, Department of Computing Technologies", 
          size_pt=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=20)
    
    # SRM Logo
    logo_path = 'docs/screenshots/srm_logo_image1.jpeg'
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(8)
        p_logo.paragraph_format.space_after = Pt(12)
        run_logo = p_logo.add_run()
        run_logo.add_picture(logo_path, width=Inches(1.8))
        
    add_p(doc, "in partial fulfillment of the requirements for the degree of", 
          size_pt=12, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=6)
    add_p(doc, "BACHELOR OF TECHNOLOGY", 
          size_pt=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=2)
    add_p(doc, "in", 
          size_pt=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=2)
    add_p(doc, "COMPUTER SCIENCE AND ENGINEERING", 
          size_pt=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=18)
    
    add_p(doc, "DEPARTMENT OF COMPUTING TECHNOLOGIES\nCOLLEGE OF ENGINEERING AND TECHNOLOGY\nSRM INSTITUTE OF SCIENCE AND TECHNOLOGY\nKATTANKULATHUR – 603 203, TAMIL NADU, INDIA", 
          size_pt=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=12, line_spacing=1.2)
    add_p(doc, "MAY 2026", 
          size_pt=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=0)
    
    doc.add_page_break()

    # ==========================================
    # 2. OWN WORK DECLARATION FORM
    # ==========================================
    logo_path2 = 'docs/screenshots/srm_logo_image2.jpeg'
    if os.path.exists(logo_path2):
        p_logo2 = doc.add_paragraph()
        p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo2.paragraph_format.space_before = Pt(0)
        p_logo2.paragraph_format.space_after = Pt(4)
        run_logo2 = p_logo2.add_run()
        run_logo2.add_picture(logo_path2, width=Inches(1.3))

    add_p(doc, "DEPARTMENT OF COMPUTING TECHNOLOGIES", 
          size_pt=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=2)
    add_p(doc, "SRM INSTITUTE OF SCIENCE & TECHNOLOGY", 
          size_pt=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=4)
    add_p(doc, "OWN WORK DECLARATION FORM", 
          size_pt=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=10)
    
    add_p(doc, "This sheet must be filled in (each box ticked to show that the condition has been met). It must be signed and dated along with your student registration number and included with all assignments you submit – work will not be marked unless this is done.", 
          size_pt=9.5, italic=True, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=8)
    
    add_p(doc, "To be completed by the student for all assessments:", 
          size_pt=10.5, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=4, space_after=4)
    
    # Metadata table
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(meta_table, color="94A3B8", sz="4")
    meta_fields = [
        ("Degree / Course", "B.Tech Computer Science and Engineering / 21CSP401L"),
        ("Student Name", "Daksh Gehlot"),
        ("Registration Number", "RA2411003012297"),
        ("Title of Work", "Autoshare: Campus Ride-Pooling and Mobility Platform with Microservices Architecture")
    ]
    for idx, (lbl, val) in enumerate(meta_fields):
        c0 = meta_table.cell(idx, 0)
        c1 = meta_table.cell(idx, 1)
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        set_cell_margins(c0, 80, 80, 100, 100)
        set_cell_margins(c1, 80, 80, 100, 100)
        set_cell_shading(c0, "F1F5F9")
        set_cell_shading(c1, "FFFFFF")
        
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r0 = p0.add_run(lbl)
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(10)
        r0.font.bold = True
        
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r1 = p1.add_run(val)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(10)

    add_p(doc, "I / We hereby certify that this assessment complies with the University’s Rules and Regulations relating to Academic misconduct and plagiarism, as listed in the University Website, Regulations, and the Education Committee guidelines.", 
          size_pt=10, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=10, space_after=6)
    
    add_p(doc, "I / We confirm that all the work contained in this assessment is my / our own except where indicated, and that I / We have met the following conditions:", 
          size_pt=10, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=4, space_after=4)
    
    conditions = [
        "[X]  Clearly referenced / listed all sources as appropriate",
        "[X]  Referenced and put in inverted commas all quoted text (from books, web, etc)",
        "[X]  Given the sources of all pictures, data etc. that are not my own",
        "[X]  Not made any use of the report(s) or essay(s) of any other student(s) either past or present",
        "[X]  Acknowledged in appropriate places any help that I have received from others (fellow students, technicians, external sources)",
        "[X]  Complied with any other plagiarism criteria specified in the Course handbook / University website"
    ]
    for cond in conditions:
        add_p(doc, cond, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=1, space_after=2)
        
    add_p(doc, "I / We understand that any false claim for this work will be penalized in accordance with University policies and regulations.", 
          size_pt=10, italic=True, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=6, space_after=10)
    
    # Signature Box
    sig_table = doc.add_table(rows=2, cols=3)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(sig_table, color="94A3B8", sz="4")
    sig_headers = ["Student Name", "Registration Number", "Signature & Date"]
    for c_i, h_txt in enumerate(sig_headers):
        cell = sig_table.cell(0, c_i)
        set_cell_margins(cell, 80, 80, 100, 100)
        set_cell_shading(cell, "F1F5F9")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_txt)
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)
        r.font.bold = True
        
    sig_vals = ["Daksh Gehlot", "RA2411003012297", "Daksh Gehlot (12-05-2026)"]
    for c_i, v_txt in enumerate(sig_vals):
        cell = sig_table.cell(1, c_i)
        set_cell_margins(cell, 120, 120, 100, 100)
        set_cell_shading(cell, "FFFFFF")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(v_txt)
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)
        if c_i == 2:
            r.font.italic = True
            
    doc.add_page_break()

    # ==========================================
    # 3. BONAFIDE CERTIFICATE
    # ==========================================
    if os.path.exists(logo_path2):
        p_logo3 = doc.add_paragraph()
        p_logo3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo3.paragraph_format.space_before = Pt(0)
        p_logo3.paragraph_format.space_after = Pt(4)
        run_logo3 = p_logo3.add_run()
        run_logo3.add_picture(logo_path2, width=Inches(1.5))

    add_p(doc, "SRM INSTITUTE OF SCIENCE AND TECHNOLOGY", 
          size_pt=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=2)
    add_p(doc, "KATTANKULATHUR – 603 203, CHENNAI, INDIA", 
          size_pt=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=14)
    add_p(doc, "BONAFIDE CERTIFICATE", 
          size_pt=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=8, space_after=16)
    
    cert_text = (
        "Certified that 21CSP401L- Major Project report titled “AUTOSHARE: CAMPUS RIDE-POOLING "
        "AND MOBILITY PLATFORM WITH MICROSERVICES ARCHITECTURE” is the bonafide work of "
        "“DAKSH GEHLOT [RA2411003012297]”, who carried out the project work under my supervision. "
        "Certified further, that to the best of my knowledge the work reported herein does not form "
        "part of any other project report or dissertation on the basis of which a degree or award "
        "was conferred on an earlier occasion on this or any other candidate."
    )
    add_p(doc, cert_text, size_pt=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=12, space_after=48, line_spacing=1.4)
    
    # Signature layout table
    sig_cert_table = doc.add_table(rows=1, cols=2)
    sig_cert_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # no visible borders
    set_table_borders(sig_cert_table, color="FFFFFF", sz="0", val="none")
    
    cell_guide = sig_cert_table.cell(0, 0)
    cell_guide.width = Inches(3.2)
    set_cell_margins(cell_guide, 40, 40, 60, 60)
    p_g = cell_guide.paragraphs[0]
    p_g.alignment = WD_ALIGN_PARAGRAPH.LEFT
    rg1 = p_g.add_run("SIGNATURE\n\n\n\n")
    rg1.font.bold = True
    rg1.font.size = Pt(11)
    rg2 = p_g.add_run("Dr. M. S. ABIRAMI, M.Tech., Ph.D.\nSUPERVISOR\nAssociate Professor\nDepartment of Computing Technologies\nCollege of Engineering and Technology\nSRM Institute of Science and Technology")
    rg2.font.size = Pt(10)
    
    cell_hod = sig_cert_table.cell(0, 1)
    cell_hod.width = Inches(3.3)
    set_cell_margins(cell_hod, 40, 40, 60, 60)
    p_h = cell_hod.paragraphs[0]
    p_h.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    rh1 = p_h.add_run("SIGNATURE\n\n\n\n")
    rh1.font.bold = True
    rh1.font.size = Pt(11)
    rh2 = p_h.add_run("Dr. PUSHPALATHA M., Ph.D.\nHEAD OF THE DEPARTMENT\nProfessor & Head\nDepartment of Computing Technologies\nCollege of Engineering and Technology\nSRM Institute of Science and Technology")
    rh2.font.size = Pt(10)

    doc.add_page_break()

    # ==========================================
    # 4. ABSTRACT
    # ==========================================
    add_heading_1(doc, "ABSTRACT")
    
    abstract_text = (
        "At suburban engineering campuses such as SRM Institute of Science and Technology, "
        "Kattankulathur, thousands of student commuters travel daily between university entrance "
        "gates (Gate 1, Gate 2, Tech Park Gate, Library Block) and surrounding residential clusters "
        "(Estancia, Abode Valley, Green Pearl PG, and Potheri Railway Station). Due to unstructured "
        "commute coordination, students frequently hire single-occupant auto-rickshaws (TukTuks), "
        "incurring steep individual fares ranging from ₹120 to ₹180 per trip, exacerbating gate-side "
        "traffic congestion, and missing opportunities for safe peer travel. This project presents "
        "Autoshare, a full-stack campus ride-pooling and mobility platform designed to pair commuters "
        "traveling along identical routes, calculate proportional dynamic fare splits (reducing individual "
        "commute expenses to ₹40–₹60 per seat), and enforce strict campus identity verification. "
        "The backend is developed with Java 17 and Spring Boot 3.3.4, implementing a decoupled "
        "microservices architecture comprising a ride-booking service (port 8080) for ride lifecycle "
        "and fare division logic, and a user-management service (port 8081) backed by Spring Data JPA "
        "and Hibernate for relational user persistence and verification. Inter-service identity checks "
        "are executed via synchronous HTTP REST requests protected by a circuit breaker pattern with "
        "graceful fallback. The client tier is built as a single-page application using React 19 and "
        "Vite 6, featuring live route filtering, modal ride posting, interactive JPA user administration, "
        "and a real-time microservices console. The platform is comprehensively verified through an "
        "automated test suite of 22 JUnit 5 and Mockito tests across repository, service, and controller "
        "tiers with 100% pass rate. Empirical performance benchmarks demonstrate sub-25 ms REST response "
        "latencies and atomic transaction management under concurrent seat bookings, establishing a secure, "
        "economical, and scalable mobility solution for institutional campuses."
    )
    add_p(doc, abstract_text, size_pt=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=14, space_after=14, line_spacing=1.35)
    
    add_p(doc, "Keywords: Campus Mobility, Ride-Pooling, Spring Boot 3, Microservices Architecture, Spring Data JPA, Dynamic Fare Split, React 19, RESTful Web Services.", 
          size_pt=11, bold=True, italic=True, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=10, space_after=10)

    doc.add_page_break()

    # ==========================================
    # 5. TABLE OF CONTENTS
    # ==========================================
    add_heading_1(doc, "TABLE OF CONTENTS")
    
    toc_data = [
        ("ABSTRACT", "iv"),
        ("TABLE OF CONTENTS", "v"),
        ("LIST OF FIGURES", "vii"),
        ("LIST OF TABLES", "viii"),
        ("LIST OF ABBREVIATIONS", "ix"),
        ("", ""),
        ("1   INTRODUCTION", "1"),
        ("     1.1  General (Introduction to Project)", "1"),
        ("     1.2  Motivation", "2"),
        ("     1.3  Problem Statement and Description", "3"),
        ("     1.4  Sustainable Development Goals of the Project", "4"),
        ("     1.5  Product Vision Statement", "5"),
        ("          1.5.1  Target Audience", "5"),
        ("          1.5.2  User Needs & Pain Points", "5"),
        ("          1.5.3  Product Features & Ecosystem", "6"),
        ("          1.5.4  Core Value Propositions", "6"),
        ("     1.6  Product Goal", "7"),
        ("     1.7  Product Backlog (MoSCoW Prioritized User Stories)", "7"),
        ("     1.8  Product Release Plan", "9"),
        ("", ""),
        ("2   SPRINT PLANNING AND EXECUTION", "10"),
        ("     2.1  Sprint 1: Core Ride-Pooling Engine & Dynamic Fare Split System", "10"),
        ("          2.1.1  Sprint Goal with User Stories of Sprint 1", "10"),
        ("          2.1.2  Functional Document", "11"),
        ("          2.1.3  Architecture Document", "13"),
        ("          2.1.4  UI Design", "15"),
        ("          2.1.5  Functional Test Cases", "17"),
        ("          2.1.6  Daily Scrum Call Progress", "19"),
        ("          2.1.7  Committed vs Completed User Stories", "21"),
        ("          2.1.8  Sprint Retrospective", "22"),
        ("     2.2  Sprint 2: Spring Data JPA User Record Management & Persistence", "23"),
        ("          2.2.1  Sprint Goal with User Stories of Sprint 2", "23"),
        ("          2.2.2  Functional Document", "24"),
        ("          2.2.3  Architecture Document", "26"),
        ("          2.2.4  UI Design", "28"),
        ("          2.2.5  Functional Test Cases", "30"),
        ("          2.2.6  Daily Scrum Call Progress", "32"),
        ("          2.2.7  Committed vs Completed User Stories", "34"),
        ("          2.2.8  Sprint Retrospective", "35"),
        ("     2.3  Sprint 3: Microservices Architecture, Inter-Service REST & Console", "36"),
        ("          2.3.1  Sprint Goal with User Stories of Sprint 3", "36"),
        ("          2.3.2  Functional Document", "37"),
        ("          2.3.3  Architecture Document", "39"),
        ("          2.3.4  UI Design", "42"),
        ("          2.3.5  Functional Test Cases", "44"),
        ("          2.3.6  Daily Scrum Call Progress", "46"),
        ("          2.3.7  Committed vs Completed User Stories", "48"),
        ("          2.3.8  Sprint Retrospective", "49"),
        ("", ""),
        ("3   RESULTS AND DISCUSSION", "50"),
        ("     3.1  Project Outcomes & Deliverables Alignment", "50"),
        ("     3.2  Automated Test Suite Verification (22 Automated Tests)", "52"),
        ("     3.3  Committed vs Completed User Stories Across All Sprints", "55"),
        ("     3.4  Empirical Performance & Latency Benchmarks", "56"),
        ("", ""),
        ("4   CONCLUSIONS & FUTURE ENHANCEMENTS", "58"),
        ("     4.1  Conclusion", "58"),
        ("     4.2  Future Enhancements & Production Roadmap", "59"),
        ("", ""),
        ("APPENDIX", "61"),
        ("     A.  PATENT DISCLOSURE FORM (INVENTION DISCLOSURE)", "61"),
        ("     B.  SAMPLE CODING (CORE SERVICE & REPOSITORY IMPLEMENTATIONS)", "66"),
        ("     C.  PLAGIARISM EVALUATION REPORT", "74")
    ]
    
    toc_table = doc.add_table(rows=len(toc_data) + 1, cols=2)
    toc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(toc_table, color="FFFFFF", sz="0", val="none")
    
    # Header
    c0 = toc_table.cell(0, 0)
    c1 = toc_table.cell(0, 1)
    c0.width = Inches(5.5)
    c1.width = Inches(1.0)
    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r0 = p0.add_run("CHAPTER NO. / TITLE")
    r0.font.bold = True
    r0.font.size = Pt(10.5)
    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r1 = p1.add_run("PAGE NO.")
    r1.font.bold = True
    r1.font.size = Pt(10.5)
    
    for idx, (title, pg) in enumerate(toc_data):
        c0 = toc_table.cell(idx + 1, 0)
        c1 = toc_table.cell(idx + 1, 1)
        c0.width = Inches(5.5)
        c1.width = Inches(1.0)
        set_cell_margins(c0, 20, 20, 40, 40)
        set_cell_margins(c1, 20, 20, 40, 40)
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p0.paragraph_format.line_spacing = 1.15
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        
        is_bold = (title.startswith("1 ") or title.startswith("2 ") or title.startswith("3 ") or 
                   title.startswith("4 ") or title.startswith("APPENDIX") or title in ["ABSTRACT", "TABLE OF CONTENTS", "LIST OF FIGURES", "LIST OF TABLES", "LIST OF ABBREVIATIONS"])
        r0 = p0.add_run(title)
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(10)
        r0.font.bold = is_bold
        
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.paragraph_format.line_spacing = 1.15
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(pg)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(10)
        r1.font.bold = is_bold

    doc.add_page_break()

    # ==========================================
    # 6. LIST OF FIGURES
    # ==========================================
    add_heading_1(doc, "LIST OF FIGURES")
    
    figures_data = [
        ("Figure 1.1", "Autoshare Product Backlog and Sprint Board Allocation", "8"),
        ("Figure 1.2", "Autoshare Product Release Roadmap & Sprint Cadence", "9"),
        ("Figure 2.1", "Autoshare React 19 Client Landing Page & Active Rides Feed", "15"),
        ("Figure 2.2", "REST API Response Payload for Active Campus Rides (GET /api/rides)", "16"),
        ("Figure 2.3", "Dynamic Fare Split Calculation JSON Endpoint (GET /api/rides/1/fare-split)", "16"),
        ("Figure 2.4", "In-Memory H2 Relational Database Web Console and Schema Tables", "17"),
        ("Figure 2.5", "Sprint 1 Burndown Chart & Story Point Realization", "22"),
        ("Figure 2.6", "Spring Boot Data JPA Microservice Startup Banner and Port Binding", "28"),
        ("Figure 2.7", "Execution of Spring Data JPA User CRUD REST Endpoints", "29"),
        ("Figure 2.8", "Interactive User Record Management Dashboard in React 19 Frontend", "30"),
        ("Figure 2.9", "Sprint 2 Burndown Chart & Story Point Realization", "35"),
        ("Figure 2.10", "Inter-Service HTTP REST Trace between Ride Service (8080) and User Service (8081)", "43"),
        ("Figure 2.11", "Microservices Architecture Console with Step-by-Step Pipeline Runner & Wire Inspector", "44"),
        ("Figure 2.12", "Sprint 3 Burndown Chart & Story Point Realization", "49"),
        ("Figure 3.1", "Automated Test Suite Execution Logs Showing 22 Passing Unit and Integration Tests", "54"),
        ("Figure 3.2", "Committed vs Completed Story Points per Sprint and Overall Project", "56"),
        ("Figure 3.3", "REST API Endpoint Latency Benchmarks under Concurrent Requests", "57")
    ]
    
    fig_table = doc.add_table(rows=len(figures_data) + 1, cols=3)
    fig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(fig_table, color="FFFFFF", sz="0", val="none")
    
    fig_headers = ["FIGURE NO.", "TITLE", "PAGE NO."]
    fig_widths = [1.2, 4.6, 0.9]
    for c_i, h_txt in enumerate(fig_headers):
        cell = fig_table.cell(0, c_i)
        cell.width = Inches(fig_widths[c_i])
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_i < 2 else WD_ALIGN_PARAGRAPH.RIGHT
        r = p.add_run(h_txt)
        r.font.bold = True
        r.font.size = Pt(10.5)
        
    for r_i, (f_no, f_title, f_pg) in enumerate(figures_data):
        row = fig_table.rows[r_i + 1]
        for c_i, val in enumerate([f_no, f_title, f_pg]):
            cell = row.cells[c_i]
            cell.width = Inches(fig_widths[c_i])
            set_cell_margins(cell, 25, 25, 30, 30)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_i < 2 else WD_ALIGN_PARAGRAPH.RIGHT
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5)
            if c_i == 0:
                r.font.bold = True

    doc.add_page_break()

    # ==========================================
    # 7. LIST OF TABLES
    # ==========================================
    add_heading_1(doc, "LIST OF TABLES")
    
    tables_data = [
        ("Table 1.1", "Product Backlog with MoSCoW Prioritization and Story Point Estimates", "8"),
        ("Table 2.1", "Sprint 1 Detailed User Stories and Acceptance Criteria", "11"),
        ("Table 2.2", "Sprint 1 Role-Based Access Control Authorization Matrix", "13"),
        ("Table 2.3", "Sprint 1 Core REST API Contract Specification", "14"),
        ("Table 2.4", "Sprint 1 Functional Test Cases (TC-S1-01 to TC-S1-06)", "18"),
        ("Table 2.5", "Sprint 1 Daily Scrum Progress & Blocker Resolution Log (10 Days)", "20"),
        ("Table 2.6", "Sprint 1 Committed vs Completed User Stories Breakdown", "21"),
        ("Table 2.7", "Sprint 2 Detailed User Stories and Acceptance Criteria", "24"),
        ("Table 2.8", "Sprint 2 User Identity Authorization Matrix", "26"),
        ("Table 2.9", "Sprint 2 Spring Data JPA User Service REST API Contract", "27"),
        ("Table 2.10", "Sprint 2 Functional Test Cases (TC-S2-01 to TC-S2-07)", "31"),
        ("Table 2.11", "Sprint 2 Daily Scrum Progress & Blocker Resolution Log (10 Days)", "33"),
        ("Table 2.12", "Sprint 2 Committed vs Completed User Stories Breakdown", "34"),
        ("Table 2.13", "Sprint 3 Detailed User Stories and Acceptance Criteria", "37"),
        ("Table 2.14", "Sprint 3 Microservices Inter-Service REST Contract & Fallback Behavior", "41"),
        ("Table 2.15", "Sprint 3 Functional Test Cases (TC-S3-01 to TC-S3-08)", "45"),
        ("Table 2.16", "Sprint 3 Daily Scrum Progress & Blocker Resolution Log (10 Days)", "47"),
        ("Table 2.17", "Sprint 3 Committed vs Completed User Stories Breakdown", "48"),
        ("Table 3.1", "Project Deliverables Alignment and Outcome Verification Matrix", "51"),
        ("Table 3.2", "Comprehensive Automated Test Suite Execution Breakdown (22 Tests)", "53"),
        ("Table 3.3", "Multi-Sprint Story Point Velocity and Completion Summary", "55"),
        ("Table 3.4", "Empirical Performance and Latency Benchmarks across Key Endpoints", "57")
    ]
    
    tbl_list = doc.add_table(rows=len(tables_data) + 1, cols=3)
    tbl_list.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_list, color="FFFFFF", sz="0", val="none")
    
    tbl_headers = ["TABLE NO.", "TITLE", "PAGE NO."]
    tbl_widths = [1.2, 4.6, 0.9]
    for c_i, h_txt in enumerate(tbl_headers):
        cell = tbl_list.cell(0, c_i)
        cell.width = Inches(tbl_widths[c_i])
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_i < 2 else WD_ALIGN_PARAGRAPH.RIGHT
        r = p.add_run(h_txt)
        r.font.bold = True
        r.font.size = Pt(10.5)
        
    for r_i, (t_no, t_title, t_pg) in enumerate(tables_data):
        row = tbl_list.rows[r_i + 1]
        for c_i, val in enumerate([t_no, t_title, t_pg]):
            cell = row.cells[c_i]
            cell.width = Inches(tbl_widths[c_i])
            set_cell_margins(cell, 25, 25, 30, 30)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_i < 2 else WD_ALIGN_PARAGRAPH.RIGHT
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5)
            if c_i == 0:
                r.font.bold = True

    doc.add_page_break()

    # ==========================================
    # 8. LIST OF ABBREVIATIONS
    # ==========================================
    add_heading_1(doc, "LIST OF ABBREVIATIONS")
    
    abbreviations = [
        ("API", "Application Programming Interface"),
        ("ACID", "Atomicity, Consistency, Isolation, Durability"),
        ("CI/CD", "Continuous Integration / Continuous Deployment"),
        ("CORS", "Cross-Origin Resource Sharing"),
        ("CRUD", "Create, Read, Update, Delete"),
        ("DAO", "Data Access Object"),
        ("DDL", "Data Definition Language"),
        ("DOM", "Document Object Model"),
        ("DTO", "Data Transfer Object"),
        ("ERD", "Entity Relationship Diagram"),
        ("HMR", "Hot Module Replacement"),
        ("HTTP", "Hypertext Transfer Protocol"),
        ("IDF", "Invention Disclosure Form"),
        ("JPA", "Jakarta Persistence API / Spring Data JPA"),
        ("JPQL", "Java Persistence Query Language"),
        ("JSON", "JavaScript Object Notation"),
        ("JVM", "Java Virtual Machine"),
        ("KYC", "Know Your Customer (Campus Affiliation Verification)"),
        ("MoSCoW", "Must have, Should have, Could have, Won't have"),
        ("MVC", "Model View Controller"),
        ("ORM", "Object Relational Mapping"),
        ("REST", "Representational State Transfer"),
        ("SDG", "Sustainable Development Goal (United Nations)"),
        ("SPA", "Single Page Application"),
        ("SQL", "Structured Query Language"),
        ("SSO", "Single Sign-On"),
        ("SVG", "Scalable Vector Graphics"),
        ("UI / UX", "User Interface / User Experience"),
        ("URI / URL", "Uniform Resource Identifier / Uniform Resource Locator"),
        ("VCF", "Variant Call Format / Virtual Context Framework")
    ]
    
    abbr_table = doc.add_table(rows=len(abbreviations) + 1, cols=2)
    abbr_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(abbr_table, color="CBD5E1", sz="4")
    
    # Headers
    h0 = abbr_table.cell(0, 0)
    h1 = abbr_table.cell(0, 1)
    h0.width = Inches(1.8)
    h1.width = Inches(4.9)
    set_cell_margins(h0, 80, 80, 120, 120)
    set_cell_margins(h1, 80, 80, 120, 120)
    set_cell_shading(h0, "E2E8F0")
    set_cell_shading(h1, "E2E8F0")
    
    p0 = h0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0 = p0.add_run("ACRONYM")
    r0.font.bold = True
    r0.font.size = Pt(10)
    
    p1 = h1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r1 = p1.add_run("EXPANSION / MEANING")
    r1.font.bold = True
    r1.font.size = Pt(10)
    
    for idx, (acr, exp) in enumerate(abbreviations):
        c0 = abbr_table.cell(idx + 1, 0)
        c1 = abbr_table.cell(idx + 1, 1)
        c0.width = Inches(1.8)
        c1.width = Inches(4.9)
        set_cell_margins(c0, 60, 60, 120, 120)
        set_cell_margins(c1, 60, 60, 120, 120)
        bg = "FFFFFF" if idx % 2 == 0 else "F8FAFC"
        set_cell_shading(c0, bg)
        set_cell_shading(c1, bg)
        
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(acr)
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r1 = p1.add_run(exp)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(9.5)

    doc.add_page_break()
    print("Front matter generated successfully.")

