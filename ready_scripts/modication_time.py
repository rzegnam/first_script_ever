import os
from requests import get

url = 'http://www.ntma.ie/download/dail_bonds_outstanding_reports/OutstandingBondsreport-2017-11-02.pdf'

f1 = os.stat('1.pdf').st_mtime
f2 = os.stat('2.pdf').st_mtime

if f1 > f2:
    print(f1)
    print(f2)
    with open('2.pdf', 'wb') as f:
        f.write(get(url).content)
if f1 < f2:
    print("f2")
    with open('1.pdf', 'wb') as f:
        f.write(get(url).content)
