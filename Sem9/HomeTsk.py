import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs

url = 'https://sazonovmebel.ru/'
response = requests.get(url).text
soup = bs(response, 'html.parser')
find_text = soup.find('body').find('div', class_="container-list"). \
    find(class_="element-content button-1 element-content--free"). \
    find(class_="btn-content text-color hover-text-color btn-content-text icon-on-left")
tqdm(print(find_text.text))
