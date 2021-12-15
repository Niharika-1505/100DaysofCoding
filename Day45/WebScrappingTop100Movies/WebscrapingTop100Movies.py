import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
html_contents = response.text
soup = BeautifulSoup(html_contents, "html.parser")
all_cinema_titles = soup.find_all(name="h3", class_="title")

cinema_titles = [each_cinema_title.getText() for each_cinema_title in all_cinema_titles]
cinemas = cinema_titles[::-1]

with open("Top100MoviesToWatch.txt", mode="w") as file:
    for each_cinema in cinemas:
        file.write(f"{each_cinema}\n")
