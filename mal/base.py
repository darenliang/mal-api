from typing import Any

import requests
from bs4 import BeautifulSoup


class _Base:
    def __init__(self, timeout):
        """
        Base class
        :param timeout: Timeout in seconds
        """
        self.timeout = timeout

    def _parse_url(self, url) -> Any:
        """
        Parse URL
        :param url: URL
        :return: Beautiful Soup object
        """
        page_response = requests.get(url, timeout=self.timeout)
        return BeautifulSoup(page_response.content, "html.parser")
