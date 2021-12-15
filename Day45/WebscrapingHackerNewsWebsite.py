import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
html_contents = response.text
soup = BeautifulSoup(html_contents, "html.parser")
all_articles = soup.find_all(name="a", class_="titlelink")
article_text = []
article_links = []
for each_article in all_articles:
    text = each_article.getText()
    article_text.append(text)
    link = each_article.get("href")
    article_links.append(link)

votes_for_articles = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_vote = max(votes_for_articles)
index_of_highest_vote = votes_for_articles.index(highest_vote)
print(f"{article_text[index_of_highest_vote]}: {article_links[index_of_highest_vote]}")
