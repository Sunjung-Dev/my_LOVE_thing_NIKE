#crawling NIKE site

import requests
from bs4 import BeautifulSoup

def crawl_info():
    url = 'https://www.nike.com/kr/launch/?type=feed'
    response = requests.get(url)
    
    result = BeautifulSoup(response.text , 'html.parser')
    shoes_info = result.find('div', class_='ncss-col-sm-12 full')
    #왜 None으로 나오는거야 ?! 
    print(shoes_info)

print(crawl_info())