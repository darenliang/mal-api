import requests
from bs4 import BeautifulSoup


class _Base:
    def __init__(self, timeout):
        self.timeout = timeout

    def _parse_url(self, url):
        page_response = requests.get(url, timeout=self.timeout)
        return BeautifulSoup(page_response.content, "html.parser")
