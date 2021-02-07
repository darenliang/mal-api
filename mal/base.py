from typing import Any, Callable

import requests
from bs4 import BeautifulSoup


def property(func: Callable) -> Callable:
    """
    Handle crashes when accessing properties
    :param func: Callable
    :return: Property value
    """

    def wrapper(self):
        try:
            return func(self)
        except:
            return None

    return wrapper


def property_list(func: Callable) -> Callable:
    """
    Handle crashes when accessing properties
    :param func: Callable
    :return: Property value
    """

    def wrapper(self):
        try:
            return func(self)
        except:
            return []

    return wrapper


def property_dict(func: Callable) -> Callable:
    """
    Handle crashes when accessing properties
    :param func: Callable
    :return: Property value
    """

    def wrapper(self):
        try:
            return func(self)
        except:
            return {}

    return wrapper


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
