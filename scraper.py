import requests
from bs4 import BeautifulSoup
import re

headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
url = "--"  

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Success")
    html_content = response.content
else:
    print("Failed to fetch the website.")
    exit()

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the text elements (e.g., paragraphs, headings, etc.) you want to scrape
article_section = soup.find('div', class_='article_section')
text_elements = article_section.find_all(['p', 'h1', 'h2', 'h3', 'h4'])

# Extract the text from each element and concatenate them into a single string - Remove noise with regex.
scraped_text = ' '.join(element.get_text() for element in text_elements)
scraped_text = re.sub(' Related Articles.*','',scraped_text)
print(scraped_text)
