import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO

'''https://blog.finxter.com/a-step-by-step-guide-to-fetching-the-url-from-the-href-attribute-using-beautifulsoup/
https://stackoverflow.com/questions/5710867/downloading-and-unzipping-a-zip-file-without-writing-to-disk'''

response = requests.get(url="https://digital.nhs.uk/services/organisation-data-service/file-downloads/gp-and-gp"
                            "-practice-related-data")
html_contents = response.text
soup = BeautifulSoup(html_contents, "html.parser")

# Getting href link to download zip file
all_articles = soup.find(href=True, string="enurse")
Url_to_download_zip = all_articles['href']

# Write to CSV after reading the csv file from the zip folder
response = urlopen(Url_to_download_zip)
zipfile = ZipFile(BytesIO(response.read()))
print(zipfile.namelist())
zipfile.extract("enurse.csv")

