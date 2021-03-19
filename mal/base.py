from typing import Any, Callable

import requests
from bs4 import BeautifulSoup
import os

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

    def _parse_url(self, url, debug) -> Any:
        """
        Parse URL
        :param url: URL
        :return: Beautiful Soup object
        """
        if debug and os.path.exists("__cache.bin"):
            fp = open("__cache.bin","rb")
            _page = fp.read()
            fp.close()
            print("Warning: debug mode; loading from cache..")
            return BeautifulSoup(_page, "html.parser")
        else:
            page_response = requests.get(url, timeout=self.timeout)
            if debug:
                fp = open("__cache.bin","wb")
                fp.write(page_response.content)
                fp.close()
            return BeautifulSoup(page_response.content, "html.parser")
