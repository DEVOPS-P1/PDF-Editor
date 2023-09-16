import os
import PyPDF2

# Prompt the user to enter the file names for "A.pdf" and "B.pdf"
pdf_a_filename = 'C:/Users/keepe/Downloads/SCAN-20230507T043854Z/Consulting_skill_1+2+3_odd.pdf'
pdf_b_filename = 'C:/Users/keepe/Downloads/SCAN-20230507T043854Z/Consulting_skill_1+2+3_even.pdf'
pdf_output_location ='C:/Users/keepe/Downloads/SCAN-20230507T043854Z/'

while not pdf_a_filename or not pdf_b_filename:
    pdf_a_filename = input('Enter the file name for Odd number file: ')
    pdf_b_filename = input('Enter the file name for Even number file: ')
    pdf_output_location = input('Enter the location for Output: ')

    if not os.path.isfile(pdf_a_filename) or not os.path.isfile(pdf_b_filename):
        print('Error: One or both of the files does not exist.')
        pdf_a_filename = ''
        pdf_b_filename = ''
        pdf_output_location =''

# Open the first PDF file "A.pdf" and create a PDF reader object
pdf_a_file = open(pdf_a_filename, 'rb')
pdf_a_reader = PyPDF2.PdfFileReader(pdf_a_file)

# Open the second PDF file "B.pdf" and create a PDF reader object
pdf_b_file = open(pdf_b_filename, 'rb')
pdf_b_reader = PyPDF2.PdfFileReader(pdf_b_file)

# Create a PDF writer object
pdf_writer = PyPDF2.PdfFileWriter()

# Loop through the odd-numbered pages in "A.pdf" and add them to the output PDF file
for page_num in range(0, pdf_a_reader.getNumPages(), 1):
    page_obj_odd = pdf_a_reader.getPage(page_num)
    page_obj_even = pdf_b_reader.getPage(page_num)
    pdf_writer.addPage(page_obj_odd)
    pdf_writer.addPage(page_obj_even)
    # Loop through the even-numbered pages in "B.pdf" and add them to the output PDF file
#for page_num in range(1, pdf_b_reader.getNumPages(), 2):
    #page_obj_even = pdf_b_reader.getPage(page_num)
    #pdf_writer.addPage(page_obj_even)


# Create a new PDF file name for the output PDF file
output_filename = pdf_output_location+'merged.pdf'

# Open the output PDF file in write-binary mode
pdf_output_file = open(output_filename, 'wb')

# Write the merged PDF file to disk
pdf_writer.write(pdf_output_file)

# Close the output PDF file
pdf_output_file.close()

# Close the PDF files
pdf_a_file.close()
pdf_b_file.close()