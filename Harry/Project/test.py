from bs4 import BeautifulSoup
import requests       
url= "https://www.dictionary.com/browse/vacant"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
first_div = soup.find('div', class_="NZKOFkdkcvYgD3lqOIJw")
print(first_div.get_text())


