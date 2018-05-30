import wget
import re
from requests import get
from bs4 import BeautifulSoup
import os.path

def make_soup(url):
    r = get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup

def obtain_link(content):
    pattern = re.compile('government_bonds')
    result = content.find(href=pattern)
    return result.get('href')

def download_pdf(link):
    f1 = os.stat('1.pdf').st_mtime
    f2 = os.stat('2.pdf').st_mtime

    if f1 > f2:
        print("Nadpisuję 2. pdf")
        with open('2.pdf', 'wb') as f:
            f.write(get(link).content)
    else:
        print("Nadpisuję 1.pdf")
        with open('1.pdf', 'wb') as f:
            f.write(get(link).content)

url = 'http://www.ntma.ie/business-areas/funding-and-debt-management/government-bonds/'

a1 = make_soup(url)
a = obtain_link(a1)
download_pdf(a)
print(a)




#filename = wget.download(a)
#print(filename)
