from bs4 import BeautifulSoup

# import lxml

with open("website.html") as html_file:
    contents = html_file.read()
soup = BeautifulSoup(contents, "html.parser")
print(f"1. Title: {soup.title}\nJust the string within Title: {soup.title.string}")
# print(soup.prettify())  # Indents the html code beautifully

all_p_tags = soup.find_all(name="p")  # Retrieves all Paragraph tags
print(f"2. {all_p_tags}")
for tag in all_p_tags:  # Prints just the text from those Paragraph tags
    print(f"3. {tag.getText()}")
    # print(tag.get("em"))

labels = soup.find(name="label", class_="label")
print(f"4. {labels}")
print(f"5. {labels.getText()}")
print(f"6. {labels.name}")
print(f"7. {labels.get('class')}")

india_flag_url = soup.select_one(selector="li a")  # This uses a CSS selector to find all the <a> tags in a <li> tag
print(f"8. india_flag_url {india_flag_url}")

name = soup.select_one(selector="#name")  # looks for an id named name
print(f"9. Name: {name}")

class_name = soup.select(selector=".label")  # looks for all classes named label
print(f"10. Class: {class_name}")

form_tag = soup.find("input")
name_value = form_tag.get("name")
print(f"11. Getting Attribute values: {name_value}")
