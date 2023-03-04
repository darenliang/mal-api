from typing import Any, Callable

import requests
from bs4 import BeautifulSoup


def property(func: Callable) -> Callable:
    def wrapper(self):
        try:
            return func(self)
        except:
            return None

    return wrapper


def property_list(func: Callable) -> Callable:
    def wrapper(self):
        try:
            return func(self)
        except:
            return []

    return wrapper


def property_dict(func: Callable) -> Callable:
    def wrapper(self):
        try:
            return func(self)
        except:
            return {}

    return wrapper


class _Base:
    def __init__(self, timeout):
        self.timeout = timeout

    def _parse_url(self, url) -> Any:
        page_response = requests.get(url, timeout=self.timeout)
        return BeautifulSoup(page_response.content, "html.parser", from_encoding='utf-8')
