from bs4 import BeautifulSoup
import urllib
url = 'http://www.immi.gov.au/skilled/general-skilled-migration/estimated-allocation-times.htm'
page = urllib.urlopen(url)
soup = BeautifulSoup(page)
for row in soup.html.body.findAll('tr'):
 data = row.findAll('td')
 if data and 'subclass 885online' in data[0].text:
  print (data[4].text)
 
