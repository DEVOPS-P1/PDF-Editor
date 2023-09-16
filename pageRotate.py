import os
import PyPDF2

# Set the directory containing the PDF files
#pdf_directory = 'C:\\Users\\keepe\\Downloads\\SCAN-20230505T124812Z-001\\SCAN'

# Prompt the user to enter the file names for "A.pdf"
pdf_directory = input('Enter the directory to be rotated: ')

# Loop through all the PDF files in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        # Open the PDF file in read-binary mode
        pdf_file = open(os.path.join(pdf_directory, filename), 'rb')

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfFileWriter()

        # Loop through all the pages in the PDF file
        for page_num in range(pdf_reader.getNumPages()):
            # Get the page object
            page_obj = pdf_reader.getPage(page_num)

            # Rotate the page by 90 degrees clockwise
            page_obj.rotateCounterClockwise(90)

            # Add the rotated page to the output PDF file
            pdf_writer.addPage(page_obj)

        # Create a new file name for the output PDF file
        output_filename = os.path.join(pdf_directory, f'rotated_{filename}')

        # Open the output PDF file in write-binary mode
        pdf_output_file = open(output_filename, 'wb')

        # Write the rotated PDF file to disk
        pdf_writer.write(pdf_output_file)

        # Close the output PDF file
        pdf_output_file.close()
