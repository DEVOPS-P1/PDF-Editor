import PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter

# Open the PDF file in binary mode
pdf_file = open ('C:/Users/keepe/Downloads/Consulting_method_4+5.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Print the number of pages in the PDF file
print('Number of pages: ', pdf_reader.getNumPages())

# Loop through each page and print its properties
for page_num in range(pdf_reader.getNumPages()):
    print('Page', page_num+1, 'properties:')
    page_obj = pdf_reader.getPage(page_num)
    print('\tMedia Box:', page_obj.mediaBox)
    print('\tCrop Box:', page_obj.cropBox)
    print('\tTrim Box:', page_obj.trimBox)
    print('\tArt Box:', page_obj.artBox)
    print('\tRotation:', page_obj.get('/Rotate', 0))
    print('\tContents:', len(page_obj['/Contents']), 'content streams')

# Close the PDF file
pdf_file.close()