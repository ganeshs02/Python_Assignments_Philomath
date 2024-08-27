#1 -wrtie a program  to manipulate pdf files using pypdf .
''' your programs should be able to merge multiple pdf 
files into a single pdf.you are welcome to add more 
functionalities.'''

#2 - pypdf is a free and open-source pure-python PDF library 
'''capable of splitting ,merging,cropping,and transforming 
the pages of the pdf files.it can also add custom DeprecationWarning
viewing opetions, and passwords to pdf files .pypdf can
retrieve text and metadata from pdfs as well'''

from PyPDF2 import PdfWriter
import os

print(dir(PdfWriter))

#directory which contains files
dir = r"C:\Users\Ganseh\Desktop\Python Assignments\Python_Revision_challenge\PDFS" #r'' is used for the raw string which does not count '\n'

#create a pdf writer object
merger = PdfWriter()

#list all pdf file in the dir
files = [file for file in os.listdir(dir) if file.endswith(".pdf")]

#append each pdf to the mereger

for pdf in files:
    path = os.path.join(dir, pdf)
    merger.append(path)

#output file path
output_path = r"C:\Users\Ganseh\Desktop\Python Assignments\Python_Revision_challenge\PDFS\merged-pdf.pdf"

#write out the merged pdf

merger.write(output_path)
merger.close()