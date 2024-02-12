# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:21:16 2023

@author: rajendra
"""



from bs4 import BeautifulSoup

# Load the HTML document using BeautifulSoup
with open("C:/2-dataset/sample_doc.html", "r", encoding="utf-8") as file:html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Extracting text content
text_content = soup.get_text(strip=True)
print(text_content)

# Finding specific HTML elements
address_tag = soup.find("address")
print(address_tag)

all_addresses = soup.find_all("address")
print(all_addresses)

bold_text = soup.find_all("b")
print(bold_text)

quotes = soup.find_all("q")
print(quotes)

# Finding tables and their contents
table = soup.find("table")
print(table)


for row in table.find_all("tr"):
    columns=row.find_all("td")
    print(columns)
    
    table.find_all("tr")[3].find_all("td")[2]

















