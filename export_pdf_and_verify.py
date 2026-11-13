import os
import win32com.client

abs_docx = os.path.abspath('docs/Full stack _SAMPLE PROJECT REPORT.docx')
abs_pdf = os.path.abspath('docs/Full stack _SAMPLE PROJECT REPORT.pdf')

word = win32com.client.Dispatch('Word.Application')
word.Visible = False

try:
    print(f"Opening {abs_docx}...")
    doc = word.Documents.Open(abs_docx)
    doc.Repaginate()
    total_pages = doc.ComputeStatistics(2)
    print(f"Total physical pages in Word: {total_pages}")
    
    print(f"Exporting to PDF: {abs_pdf}...")
    # 17 = wdFormatPDF
    doc.SaveAs2(abs_pdf, FileFormat=17)
    print(f"PDF successfully exported! Size: {os.path.getsize(abs_pdf)} bytes")
    doc.Close(False)
finally:
    word.Quit()

print("All done!")

