import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
import os

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set padding for a table cell (in twips, 20 twips = 1 pt)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(r'<w:tcMar {}><w:top w:w="{}" w:type="dxa"/><w:bottom w:w="{}" w:type="dxa"/><w:left w:w="{}" w:type="dxa"/><w:right w:w="{}" w:type="dxa"/></w:tcMar>'.format(nsdecls('w'), top, bottom, left, right))
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    """Set background color of a cell (e.g. 'F1F5F9')."""
    shading = parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), color_hex))
    cell._tc.get_or_add_tcPr().append(shading)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    """Set clean thin borders on a table."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(r'''
        <w:tblBorders {} >
            <w:top w:val="{}" w:sz="{}" w:space="0" w:color="{}"/>
            <w:bottom w:val="{}" w:sz="{}" w:space="0" w:color="{}"/>
            <w:left w:val="{}" w:sz="{}" w:space="0" w:color="{}"/>
            <w:right w:val="{}" w:sz="{}" w:space="0" w:color="{}"/>
            <w:insideH w:val="{}" w:sz="{}" w:space="0" w:color="{}"/>
            <w:insideV w:val="{}" w:sz="{}" w:space="0" w:color="{}"/>
        </w:tblBorders>
    '''.format(nsdecls('w'), val, sz, color, val, sz, color, val, sz, color, val, sz, color, val, sz, color, val, sz, color))
    tblPr.append(borders)

def add_p(doc, text="", font_name="Times New Roman", size_pt=12, bold=False, italic=False, color_rgb=(0,0,0), align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=6, line_spacing=1.3):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if text:
        run = p.add_run(text)
        run.font.name = font_name
        run.font.size = Pt(size_pt)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = RGBColor(*color_rgb)
    return p

def add_heading_1(doc, text):
    return add_p(doc, text, size_pt=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=14, space_after=12)

def add_heading_2(doc, text):
    return add_p(doc, text, size_pt=14, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=12, space_after=6)

def add_heading_3(doc, text):
    return add_p(doc, text, size_pt=13, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=10, space_after=4)

def add_heading_4(doc, text):
    return add_p(doc, text, size_pt=12, bold=True, italic=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=8, space_after=4)

def add_image_with_caption(doc, img_path, caption_text, width_inches=4.3):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(3)
        p_img.paragraph_format.space_after = Pt(1)
        run = p_img.add_run()
        run.add_picture(img_path, width=Inches(width_inches))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(1)
        p_cap.paragraph_format.space_after = Pt(4)
        run_cap = p_cap.add_run(caption_text)
        run_cap.font.name = "Times New Roman"
        run_cap.font.size = Pt(9)
        run_cap.font.bold = True
        run_cap.font.italic = True
    else:
        print(f"Warning: Image {img_path} not found.")

def add_code_block(doc, code_text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
    set_cell_shading(cell, "F8FAFC")
    
    # Border
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(r'''
        <w:tcBorders {} >
            <w:top w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>
            <w:left w:val="single" w:sz="18" w:space="0" w:color="3B82F6"/>
            <w:right w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>
        </w:tcBorders>
    '''.format(nsdecls('w')))
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text)
    run.font.name = "Consolas"
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor(30, 41, 59)

def add_styled_table(doc, headers, data, col_widths=None, caption=""):
    if caption:
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(4)
        p_cap.paragraph_format.space_after = Pt(2)
        run_cap = p_cap.add_run(caption)
        run_cap.font.name = "Times New Roman"
        run_cap.font.size = Pt(9.5)
        run_cap.font.bold = True
        
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table, color="CBD5E1", sz="4")
    
    # Headers
    for c_idx, h_text in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_margins(cell, top=50, bottom=50, left=80, right=80)
        set_cell_shading(cell, "E2E8F0")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05
        run = p.add_run(h_text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(15, 23, 42)
        
    # Data rows
    for r_idx, row_values in enumerate(data):
        bg = "FFFFFF" if r_idx % 2 == 0 else "F8FAFC"
        for c_idx, val in enumerate(row_values):
            cell = table.cell(r_idx + 1, c_idx)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=35, bottom=35, left=80, right=80)
            set_cell_shading(cell, bg)
            p = cell.paragraphs[0]
            if c_idx == 0 or len(str(val)) < 15:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            run = p.add_run(str(val))
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            run.font.color.rgb = RGBColor(30, 41, 59)
            
    # Apply column widths
    if col_widths and len(col_widths) == len(headers):
        for row in table.rows:
            for c_idx, w in enumerate(col_widths):
                row.cells[c_idx].width = Inches(w)
                
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(6)
    return table

