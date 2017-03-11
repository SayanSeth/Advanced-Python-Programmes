import requests
from bs4 import BeautifulSoup


def crawler(max_pages):
    page = 1
    for page in range(1, max_pages+1):
        url = 'http://www.allitebooks.com/page/' + str(page) + '/'
        source_code = requests.get(url)
        plain_text = source_code.text
        # print(plain_text) To Get Source Code
        soup = BeautifulSoup(plain_text, "lxml")
        i = 0
        print('Page Number =', page)
        for link in soup.find_all("a", {'rel': 'bookmark'}):
            i += 1
            href = link.get('href')
            text = link.text
            if i%2 == 0:
                print(href, "=", text)
            page += 1

print("\n Hello User \n It is programmed to search from allitebooks.com")
number = input("\n How Many Pages you want to Print? \n Input Number = ")
number = int(number)
crawler(number)
