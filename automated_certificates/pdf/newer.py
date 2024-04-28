import PyPDF2

# Create a new PDF document with blank pages
pdf_writer = PyPDF2.PdfWriter()
for i in range(0, 1000, 4):
    page = PyPDF2.pdf.PageObject.createBlankPage(None, 612, 792)  # Create a blank page with US Letter size (8.5 x 11 inches)

    # Add the numbers to the page
    for j in range(4):
        if i+j < 1000:
            page.addText(str(i+j+1), 50, 700-j*50)

    # Add the page to the PDF document
    pdf_writer.addPage(page)

# Save the PDF to a file
with open('output.pdf', 'wb') as output_file:
    pdf_writer.write(output_file)
