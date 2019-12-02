from PyPDF2 import PdfFileWriter, PdfFileReader

og_file = open('Gucci-Blade-Ship.pdf', 'rb')
input_file = PdfFileReader(og_file)
cropped_pdf = PdfFileWriter()

num_of_pages = input_file.getNumPages()
print (num_of_pages)

