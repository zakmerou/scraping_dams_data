import os
import requests
import sys
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from datetime import date, timedelta
import tabula


base_url = "http://81.192.10.228/wp-content/uploads/"


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2015, 12, 15)
#end_date = date(2021, 12, 7)
end_date = date(2021, 12, 9)

for single_date in daterange(start_date, end_date):
    url = single_date.strftime("%Y/%m/%d_%m_%Y") + '.pdf'
    print(url)

    folder_location = r'C:\Users\z.chmirou\scraping_dams'
    if not os.path.exists(folder_location):os.mkdir(folder_location)

    filename = os.path.join(folder_location,url.split('/')[-1])
    
    pdf_file = requests.get(urljoin(base_url,url)).content
    if sys.getsizeof(pdf_file) > 50000:
        with open(filename, 'wb') as f:
            f.write(pdf_file)

for single_date in daterange(start_date, end_date):
    url = single_date.strftime("%Y/%m/%d_%m_%Y").lstrip("0").replace("/0", "/") + '.pdf'

    folder_location = r'C:\Users\z.chmirou\scraping_dams'
    if not os.path.exists(folder_location):os.mkdir(folder_location)

    filename = os.path.join(folder_location,url.split('/')[-1])
    
    pdf_file = requests.get(urljoin(base_url,url)).content
    if sys.getsizeof(pdf_file) > 50000:
        with open(filename, 'wb') as f:
            f.write(pdf_file)