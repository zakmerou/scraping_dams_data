import tabula
import matplotlib.pyplot as plt
import pandas as pd

from urllib.parse import urljoin
from datetime import date, timedelta


base_url = "http://81.192.10.228/wp-content/uploads/"


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2021, 12, 1)
end_date = date(2021, 12, 2)

for single_date in daterange(start_date, end_date):
  url = single_date.strftime("%Y/%m/%d_%m_%Y") + '.pdf'
  pdf_path = urljoin(base_url,url)
  
  dfs = tabula.read_pdf(pdf_path, pages = 'all', columns=[1,2], stream =True)[0]
  dams_stats = dfs.iloc[:, 0:3].iloc[3:]

  # Rename Columns
  dams_stats.columns.values[0] = "Barrages"
  dams_stats.columns.values[1] = "Capacité Normale"
  dams_stats.columns.values[2] = "Reserve"

  # Split Mixed Column into two columns
  dams_stats[['Reserve','Taux de Remplissage %']] = dams_stats['Reserve'].str.split(' ',expand=True)
  
  # Convert to Float
  dams_stats['Capacité Normale'] = dams_stats['Capacité Normale'].str.replace(",",".").astype(float)
  dams_stats['Reserve'] = dams_stats['Reserve'].str.replace(",",".").astype(float)
  dams_stats['Taux de Remplissage %'] = dams_stats['Taux de Remplissage %'].str.replace(",",".").astype(float)

  # TO DO: Add date dimension / 

  dams_stats
  #dams_stats.plot(x="Barrages", y="Capacité Normale", figsize=(20, 10))