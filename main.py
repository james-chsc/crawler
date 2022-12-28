import requests
from bs4 import BeautifulSoup

url = "https://24h.pchome.com.tw/"
rsp = requests.get(url)

soup = BeautifulSoup(rsp.text, 'html.parser')
print(soup.prettify())  # prettify()用來把 html 程式變漂亮

