from PyPDF2 import PdfFileWriter, PdfFileReader
import time
from colorama import init, Fore, Style
init(convert=True)

file = input('Enter File Name: ')

og_file = open('{}.pdf'.format(file), 'rb')
input_file = PdfFileReader(og_file)
cropped_pdf = PdfFileWriter()

num_of_pages = input_file.getNumPages()

page = input_file.getPage(1)

page.cropBox.lowerLeft=(50, 175)
page.cropBox.upperRight=(600, 455)


output = PdfFileWriter()
output.addPage(page)

with open('{}-Shipping-Label.pdf'.format(file), 'wb') as new:
    output.write(new)

print (Fore.CYAN + 'Shipping Label Successfully Generated!')
time.sleep(5)
