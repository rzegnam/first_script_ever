from PyPDF2 import PdfFileWriter, PdfFileReader

path = r"C:\Users\Bartosz.Ciesielczyk\Desktop\python\daily\final.pdf"

pdfFileObj = open(path, 'rb')
pdfReader = PdfFileReader(pdfFileObj)

page = pdfReader.getPage(0)
text = page.extractText()

print(text)
print(text.split())
print(len(text))

# zapis do pliku wyciagnietego tekstu
#txtFile = open('dane.txt', 'w')
#txtFile.write(text)
#txtFile.close()


