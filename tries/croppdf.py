from PyPDF2 import PdfFileWriter, PdfFileReader

# r - the file will be only read, b - appended to the mode opens the file in binary mode
path = r"C:\Users\Bartosz.Ciesielczyk\Desktop\python\daily\test.pdf"
input_pdf = PdfFileReader(open(path, "rb"))
output = PdfFileWriter()

# getting number of pages
num_pages = input_pdf.getNumPages()

print("test.pdf has %d pages." % num_pages)

# getting exact page and adding it to output variable
page = input_pdf.getPage(0)

# cropping pdf file -- ??get??

print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y() )
page.trimBox.lowerLeft = (450, 75)
page.trimBox.upperRight = (590, 670)
page.cropBox.lowerLeft = (500, 100)
page.cropBox.upperRight = (612, 692)

#page.cropBox.lowerLeft = (50, 50)
#page.cropBox.upperRight = (200, 200)

output.addPage(page)



# output_pdf is object of pdf to save
output_pdf = open('final.pdf', 'wb')
output.write(output_pdf)
output_pdf.close()


