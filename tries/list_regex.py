# w PyPDF2 nie da się odpowiednio wykadrować pdf'a, na razie zrobię to w inny sposoób, a potem poszukam jeszcze funkji - może któraś spełnia wymagania co do kadrowania
from PyPDF2 import PdfFileWriter, PdfFileReader
import re

# r - the file will be only read, b - appended to the mode opens the file in binary mode
path = r"C:\Users\Bartosz.Ciesielczyk\Desktop\python\daily\1.pdf"
path2 = r"C:\Users\Bartosz.Ciesielczyk\Desktop\python\daily\2.pdf"
input_pdf = PdfFileReader(open(path, "rb"))
input_pdf2 = PdfFileReader(open(path2, "rb"))
output = PdfFileWriter()

# getting number of pages
num_pages = input_pdf.getNumPages()
num_pages2 = input_pdf2.getNumPages()

print("1.pdf has %d pages." % num_pages)
print("2.pdf has %d pages." % num_pages2)

# getting exact page and adding it to output variable

text = input_pdf.getPage(0).extractText()
page2 = input_pdf2.getPage(0)
text2 = page2.extractText()


print(text)
print(text2)
print(text.split())
print(text2.split())

lista1 = text.split()
lista3 = text2.split()

lista2 = lista1[124:]
lista4 = lista3[124:]
print(lista2)
print(lista2)

tekst = str(lista2)
tekst3 = str(lista4)

regex = r"\d+,?\d+\.\d+"


matches = re.findall(regex, tekst)
matches2 = re.findall(regex, tekst3)

print(matches)
print(matches2)

tekst2 = str(matches)
tekst4 = str(matches2)

if matches == matches2:
    print("Nic się nie zmieniło")
else:
    print("Zaszły zmiany")

txtFile = open('dane.txt', 'w')
txtFile.write(tekst2)
txtFile.close()

