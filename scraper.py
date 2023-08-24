import requests
from bs4 import BeautifulSoup
import re


headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
url = "https://www.bleepingcomputer.com/news/security/winrar-zero-day-exploited-since-april-to-hack-trading-accounts/"

# Send request with headers and get response.
response = requests.get(url, headers=headers)

# Check if the request was successful.
if response.status_code == 200:
    print("Success")
    html_content = response.content
else:
    print("Failed to fetch the website.")
    exit()

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Get title and body.
title = soup.find("div", class_="article_section").find("h1").get_text()
raw_body = soup.find("div", class_="articleBody").find_all("p", recursive=False)

# Join all elements in the body together.
body = "".join(element.get_text() for element in raw_body)

print(title)
print(body)
