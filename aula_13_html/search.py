import requests
from bs4 import BeautifulSoup  #pip install bs4 para organizar codigo html

response = requests.get("http://www.google.com/search", params={'q': 'cavalo'})
print(response.status_code)
if response.status_code >= 200:
    soup = BeautifulSoup(response.text, "html.parser")
    output = []
    for searchWrapper in soup.find_all('a'): 
        print(searchWrapper)


