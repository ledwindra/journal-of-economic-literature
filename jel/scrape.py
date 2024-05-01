import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0'}
    try:
        response = requests.get(url, headers=headers, timeout=None)
        html = BeautifulSoup(response.content, "html.parser")

        return html
    
    except requests.exceptions.ConnectionError:
        pass
