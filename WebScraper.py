import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        self.data = list()
        URL = 'https://www.esrl.noaa.gov/gmd/aggi/aggi.html'  # The url to get info
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.findAll('table')[1]
        table_rows = table.find_all("tr")
        for tr in table_rows[4:]:
            td = tr.find_all('td')
            row = [i.text for i in td]
            data_tuple = (int(row[0]), row[1],
                          row[2], row[3], row[4], row[5], row[6])
            self.data.append(data_tuple)