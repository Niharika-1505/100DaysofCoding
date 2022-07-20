import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

'''https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python'''

response = requests.get(url="https://www.isdscotland.org/Products-and-Services/Data-Definitions-and-References"
                            "/National-Reference-Files/")
html_contents = response.text
soup = BeautifulSoup(html_contents, "html.parser")

# Getting href link
all_articles = soup.find(href=True, string="purchpro")
Url_to_Extract_purchpro = all_articles['href']

# To read data from href into a List
purchpro_raw_webdata = urlopen(Url_to_Extract_purchpro)
purchpro_webdata_List = purchpro_raw_webdata.readlines()

# Removing leading and trailing characters from each element in the list
list_after_removing_starting_2_chars = list(map(lambda x: str(x)[2:], purchpro_webdata_List))
list_after_removing_ending_10_chars = list(map(lambda x: str(x)[:-10], list_after_removing_starting_2_chars))

# Removing extra whitespaces from each element in the list and creating a final list
final_purchproList = []
for each_element in list_after_removing_ending_10_chars:
    data = " ".join(each_element.split())
    final_purchproList.append(data)

# Writing the List to DataFrame
df = pd.DataFrame(final_purchproList)

# Writing the DataFrame to CSV
df.to_csv("purchpro.csv", index=False)
