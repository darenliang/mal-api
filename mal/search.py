from mal import config
from mal.base import _Base


class _SearchResult:
    def __init__(self, url, image_url, title, synopsis, media_type, score):
        self.url = url
        self.image_url = image_url
        self.title = title
        self.synopsis = synopsis
        self.type = media_type
        self.score = score


class _Search(_Base):
    def __init__(self, query, mal_type, timeout):
        if len(query) > 100:
            raise ValueError("Query cannot be more than 100 characters")
        super().__init__(timeout)
        self._query = query
        self._url = config.MAL_ENDPOINT + "{}.php?q={}".format(mal_type, query)
        self._page = self._parse_url(self._url)
        self._inner_page = self._page.find("div", {"class": "js-block-list"})
        if self._inner_page is None:
            raise ValueError("No results found")

    @staticmethod
    def _parse_eps_vols(text):
        text = text.strip()
        try:
            return int(text)
        except ValueError:
            return None

    @staticmethod
    def _parse_score(text):
        text = text.strip()
        try:
            return float(text)
        except ValueError:
            return None

    @staticmethod
    def _remove_suffix(text, suffix):
        if text.endswith(suffix):
            return text[:-len(suffix)]
        return text
