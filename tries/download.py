import urllib.request


req = urllib.request.Request('http://www.ntma.ie/download/dail_bonds_outstanding_reports/OutstandingBondsreport2017-05-23.pdf', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req)



# opens a file in binary mode so you can save data with it instead of just text
with open('gong.pdf', 'wb') as output:
    output.write(webpage.read())

