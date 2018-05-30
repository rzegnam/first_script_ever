from PyPDF2 import PdfFileWriter, PdfFileReader
import re
from ah import convert_pdf_to_txt
from ulepszanie import *

a = convert_pdf_to_txt('1.pdf')
b = convert_pdf_to_txt('2.pdf')


data_1 = regex_function(a)
data_2 = regex_function(b)


if data_1 == data_2:
    print("Nic sie nie zmienilo")
else:
    print("Zaszly zmiany")
    for i in range(len(data_1)):
        cont = i+1
        if data_1[i] != data_2[i]:
            print("Wystapiła zmiana w wierszu nr: %d." % cont)


daty = regex_dates(a)
print(daty)

zipped = list(zip(daty, data_1))
print(zipped)

#print(alalal)
dictio = dict(list(zipped))
print(dictio)

data_1 = [i.replace(',','') for i in data_1]

print(data_1)
