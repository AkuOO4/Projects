import PyPDF2

# Create a new PDF document with four pages
pdf_writer = PyPDF2.PdfFileWriter()
for i in range(4):
    pdf_writer.addBlankPage()

# Add the numbers to separate pages
for i in range(4):
    page = pdf_writer.getPage(i)
    page.mergePage(PyPDF2.PdfFileReader(f"{i+1}.pdf").getPage(0)) # assuming you have 4 pdfs with names 1.pdf, 2.pdf, 3.pdf and 4.pdf
    pdf_writer.addPage(page)

# Save the updated PDF to a file
with open('output.pdf', 'wb') as output_file:
    pdf_writer.write(output_file)