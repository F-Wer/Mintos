from typing import Any

import requests
from lxml import html


USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"

LOGIN_URL = "https://www.mintos.com/de/login"
URL = "https://www.mintos.com/de/ubersicht/"
#TEST
def main():
    session_requests: Any = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='_csrf_token']/@value")))[0]
   #data_folder = Path('C:\\users\\fabia\\PycharmProjects\\MintosCr\\Authentication/')
   # file_to_open = data_folder / "Account.txt"
    f = open("Account.txt","r")
    lines = f.readlines()
    # Create payload
    payload = {
        "_username": lines[0],
        "_password": lines[1],
        "_csrf_token": authenticity_token

    }
    f.close()
    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    url= 'https://www.mintos.com/de/ubersicht/'
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    mintos_names = tree.xpath("//div[@class='value']/a/text()")

    print(mintos_names)

if __name__ == '__main__':
    main()