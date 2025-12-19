import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []
tags_list = []

for quote in soup.find_all("div", class_="quote"):
    quotes.append(quote.find("span", class_="text").text)
    authors.append(quote.find("small", class_="author").text)
    tags = quote.find_all("a", class_="tag")
    tags_list.append(", ".join([tag.text for tag in tags]))

df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors,
    "Tags": tags_list
})

df.to_csv("quotes_dataset.csv", index=False)
print("Done")
