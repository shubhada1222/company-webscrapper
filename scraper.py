import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Tesla,_Inc."

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text()

with open("data/company.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Website scraped successfully")