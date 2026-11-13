import os
import win32com.client
import json

abs_path = os.path.abspath('docs/Full stack _SAMPLE PROJECT REPORT.docx')
word = win32com.client.Dispatch('Word.Application')
word.Visible = False

results = {
    'headings': {},
    'figures': {},
    'tables': {}
}

try:
    doc = word.Documents.Open(abs_path)
    doc.Repaginate()
    total_pages = doc.ComputeStatistics(2)
    print(f"Total Physical Pages in Document: {total_pages}")
    
    wdActiveEndAdjustedPageNumber = 3
    
    for p in doc.Paragraphs:
        txt = p.Range.Text.strip().replace('\r', '').replace('\x07', '')
        if not txt:
            continue
        page_num = p.Range.Information(wdActiveEndAdjustedPageNumber)
        
        # Check Figures
        if txt.startswith("Figure ") and ":" in txt:
            fig_id = txt.split(":")[0].strip()
            if fig_id not in results['figures']:
                results['figures'][fig_id] = (page_num, txt)
                print(f"Figure {fig_id:10s} -> Page {page_num:2d} | {txt[:60]}")
                
        # Check Tables
        elif txt.startswith("Table ") and ":" in txt:
            tbl_id = txt.split(":")[0].strip()
            if tbl_id not in results['tables']:
                results['tables'][tbl_id] = (page_num, txt)
                print(f"Table  {tbl_id:10s} -> Page {page_num:2d} | {txt[:60]}")
                
        # Check Key Headings
        for kw in [
            'ABSTRACT', 'TABLE OF CONTENTS', 'LIST OF FIGURES', 'LIST OF TABLES', 'LIST OF ABBREVIATIONS',
            '1.1 General', '1.2 Motivation', '1.3 Problem Statement', '1.4 Sustainable Development Goals',
            '1.5 Product Vision Statement', '1.5.1 Target Audience', '1.5.2 User Needs', '1.5.3 Product Features', '1.5.4 Core Value',
            '1.6 Product Goal', '1.7 Product Backlog', '1.8 Product Release Plan',
            '2.1 Sprint 1', '2.1.1 Sprint Goal', '2.1.2 Functional Document', '2.1.3 Architecture Document',
            '2.1.4 UI Design', '2.1.5 Functional Test Cases', '2.1.6 Daily Call Progress', '2.1.7 Committed vs Completed', '2.1.8 Sprint Retrospective',
            '2.2 Sprint 2', '2.2.1 Sprint Goal', '2.2.2 Functional Document', '2.2.3 Architecture Document',
            '2.2.4 UI Design', '2.2.5 Functional Test Cases', '2.2.6 Daily Call Progress', '2.2.7 Committed vs Completed', '2.2.8 Sprint Retrospective',
            '2.3 Sprint 3', '2.3.1 Sprint Goal', '2.3.2 Functional Document', '2.3.3 Architecture Document',
            '2.3.4 UI Design', '2.3.5 Functional Test Cases', '2.3.6 Daily Call Progress', '2.3.7 Committed vs Completed', '2.3.8 Sprint Retrospective',
            '3.1 Project Outcomes', '3.2 Automated Test Suite', '3.3 Committed vs Completed User Stories Across All Sprints',
            '3.4 Empirical Performance', '4.1 Conclusion', '4.2 Future Enhancements',
            'APPENDIX A'
        ]:
            if kw.lower() in txt.lower() and len(txt) < 100:
                if kw not in results['headings']:
                    results['headings'][kw] = page_num
                    print(f"Heading {kw:35s} -> Page {page_num:2d}")
                    
        if txt.startswith("CHAPTER 1"):
            results['headings']['CHAPTER 1'] = page_num
        elif txt.startswith("CHAPTER 2"):
            results['headings']['CHAPTER 2'] = page_num
        elif txt.startswith("CHAPTER 3"):
            results['headings']['CHAPTER 3'] = page_num
        elif txt.startswith("CHAPTER 4"):
            results['headings']['CHAPTER 4'] = page_num
            
    doc.Close(False)
finally:
    word.Quit()

with open('extracted_page_numbers.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Saved extracted_page_numbers.json successfully.")

