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


def scrape_by_issue(journal_class: type, path: str, journal: str, journal_long: str):
    issue = journal_class.get_issue(journal)
    for i in issue:
        article = journal_class.get_article(i)
        journal_class.save_data(i, article, path, journal, journal_long)
