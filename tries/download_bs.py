import re
import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.Request('http://www.ntma.ie/business-areas/funding-and-debt-management/government-bonds/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req).read()

soup = BeautifulSoup(webpage, "lxml")


#for link in soup.find_all('a'):
#    print(link.get('href'))




pattern = re.compile(r"http:\/\/www\.ntma\.ie\/download\/dail_bonds_outstanding_reports\/OutstandingBondsreport\d+-\d+-\d+\.pdf")
link = soup.find('a', {'href' = pattern})





yassss = link.get('href')

print(yassss)


# uwaga - na pewno bs4 posiada opcje pobierania pliku z linku
req = urllib.request.Request(yassss, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req)

# opens a file in binary mode so you can save data with it instead of just text
with open('C:/Users/Bartosz.Ciesielczyk/Desktop/python/daily/data/1.pdf', 'wb') as output:
    output.write(webpage.read())


#with open('1.pdf', 'wb') as output:
#    output.write(yassss.read())
