# w PyPDF2 nie da się odpowiednio wykadrować pdf'a, na razie zrobię to w inny sposoób, a potem poszukam jeszcze funkji - może któraś spełnia wymagania co do kadrowania
# http://stackoverflow.com/questions/2357230/what-is-the-proper-way-to-comment-functions-in-python
from PyPDF2 import PdfFileWriter, PdfFileReader
import re
from ah import convert_pdf_to_txt

def text_extracting(path):
    """Funkcja otwiera plik o podanej sciezce 
    i eksportuje tekst do zmiennej"""
    input_pdf = PdfFileReader(open(path, "rb"))
    text = input_pdf.getPage(0).extractText()
    return text

def text_crop(text):
    """String na liste, usuniecie nieistotnych
    elementow, konwersja do stringa"""
    list_to_crop = text.split()
    crop = list_to_crop[124:]
    data = str(crop)
    return data

def regex_function(to_match):
    """Zwraca listę wartosci, 
    które spełniają warunek regex"""
    regex = r"\d+,?\d+\.\d+"
    # matches = [x for x in to_match if re.search(regex, to_match) ]
    matches = re.findall(regex, to_match)
    return matches

def regex_dates(to_match):
    regex = r"\d+/\d+/\d+"
    matches = re.findall(regex, to_match)
    return matches

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
#print(daty)

zipped = list(zip(daty, data_1))
#print(zipped)

#print(alalal)
dictio = dict(list(zipped))
#print(dictio)

