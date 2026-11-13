import docx
from docx.shared import Inches, Pt, RGBColor
import os
import sys

from make_front_matter import build_front_matter
from make_chapter1 import build_chapter_1
from make_chapter2 import build_chapter_2
from make_chapter3_4 import build_chapter_3_4
from make_appendices import build_appendices

def main():
    print("Initializing document...")
    doc = docx.Document()
    
    # Configure margins for all sections
    for sec in doc.sections:
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.left_margin = Inches(1.25)
        sec.right_margin = Inches(1.0)
        
    # Configure Normal style default font
    style_normal = doc.styles['Normal']
    font_normal = style_normal.font
    font_normal.name = 'Times New Roman'
    font_normal.size = Pt(12)
    font_normal.color.rgb = RGBColor(15, 23, 42)
    
    print("Building Front Matter (Cover, Declaration, Certificate, Abstract, TOC, Lists)...")
    build_front_matter(doc)
    
    # Add section break for Chapter 1 and restart page numbering at 1
    from docx.oxml import parse_xml
    from docx.oxml.ns import nsdecls
    
    ch1_section = doc.add_section()
    ch1_section.top_margin = Inches(1.0)
    ch1_section.bottom_margin = Inches(1.0)
    ch1_section.left_margin = Inches(1.25)
    ch1_section.right_margin = Inches(1.0)
    
    sectPr = ch1_section._sectPr
    pgNumType = parse_xml(r'<w:pgNumType %s w:start="1"/>' % nsdecls('w'))
    sectPr.append(pgNumType)
    
    print("Building Chapter 1 (Introduction, Goals, Backlog, Release Plan)...")
    build_chapter_1(doc)
    
    print("Building Chapter 2 (Sprint 1, Sprint 2, Sprint 3 with all subsections)...")
    build_chapter_2(doc)
    
    print("Building Chapters 3 & 4 (Results, Test Breakdown, Performance, Conclusion)...")
    build_chapter_3_4(doc)
    
    print("Building Appendix A (Sample Coding)...")
    build_appendices(doc)
    
    output_path = 'docs/Full stack _SAMPLE PROJECT REPORT.docx'
    print(f"Saving completed document to {output_path}...")
    doc.save(output_path)
    print("Done! File size:", os.path.getsize(output_path), "bytes.")

if __name__ == '__main__':
    main()

