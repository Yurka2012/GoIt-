import requests
# from bs4 import BeautifulSoup4
from bs4 import BeautifulSoup

response = requests.get('https://pypi.org/project/beautifulsoup4/')
# print(response.status_code)
with open('index.html', 'w') as file:
    file.write(response.text)
