# Ejemplo extraído de https://scipython.com/blog/scraping-a-wikipedia-table-with-beautiful-soup/
import urllib.request
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2'
req = urllib.request.urlopen(url)
article = req.read().decode()

with open('ISO_3166-1_alpha-2.html', 'w', encoding='UTF-8') as fo:
    fo.write(article)

# Load article, turn into soup and get the <table>s.
article = open('ISO_3166-1_alpha-2.html', encoding='UTF-8').read()
soup = BeautifulSoup(article, 'html.parser')
tables = soup.find_all('table', class_='sortable')

# Search through the tables for the one with the headings we want.
for table in tables:
    ths = table.find_all('th')
    headings = [th.text.strip() for th in ths]
    if headings[:5] == ['Code', 'Country name', 'Year', 'ccTLD', 'ISO 3166-2']:
        break

# Extract the columns we want and write to a semicolon-delimited text file.
with open('iso_3166-1_alpha-2_codes.txt', 'w') as fo:
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if not tds:
            continue
        code, country, year, ccTLD = [td.text.strip() for td in tds[:4]]
        # Wikipedia does something funny with country names containing
        # accented characters: extract the correct string form.
        if '!' in country:
            country = country[country.index('!')+1:]
        print('; '.join([code, country, year, ccTLD]), file=fo)
