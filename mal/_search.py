import re
from typing import Optional

from mal import config, _base
from mal._base import _Base


class _SearchResult:
    _image_url_path_regex = r"images\/([a-z]+\/\d+\/\d+)\."
    _mal_id_regex = r"^https:\/\/myanimelist\.net\/.+\/(\d+)\/.+$"

    def __init__(self, tds):
        self._tds = tds

    @staticmethod
    def _remove_suffix(text, suffix) -> str:
        if text.endswith(suffix):
            return text[: -len(suffix)]
        return text

    def _parse_eps_vols(self) -> Optional[int]:
        try:
            raw_text = self._tds[3].text
            raw_text = raw_text.strip()
            return int(raw_text)
        except ValueError:
            return None

    @property
    @_base.property
    def url(self) -> str:
        try:
            self._url
        except AttributeError:
            self._url = self._tds[0].find("a")["href"]
        return self._url

    @property
    @_base.property
    def mal_id(self) -> int:
        try:
            self._mal_id
        except AttributeError:
            match = re.match(_SearchResult._mal_id_regex, self.url)
            self._mal_id = int(match.group(1))
        return self._mal_id

    @property
    @_base.property
    def image_url(self) -> str:
        try:
            self._image_url
        except AttributeError:
            url = self._tds[0].find("img")["data-src"]
            image_path = re.search(
                _SearchResult._image_url_path_regex,
                url
            ).group(1)
            self._image_url = f"https://cdn.myanimelist.net/images/{image_path}.jpg"
        return self._image_url

    @property
    @_base.property
    def title(self) -> str:
        try:
            self._title
        except AttributeError:
            self._title = self._tds[1].find("strong").text.strip()
        return self._title

    @property
    @_base.property
    def synopsis(self) -> str:
        try:
            self._synopsis
        except AttributeError:
            self._synopsis = self._remove_suffix(
                self._tds[1].find("div", {"class": "pt4"}).text.strip(),
                "read more.",
            )
        return self._synopsis

    @property
    @_base.property
    def type(self) -> str:
        try:
            self._type
        except AttributeError:
            self._type = self._tds[2].text.strip()
        return self._type

    @property
    @_base.property
    def score(self) -> Optional[float]:
        try:
            self._score
        except AttributeError:
            raw_score = self._tds[4].text
            raw_score = raw_score.strip()
            try:
                self._score = float(raw_score)
            except ValueError:
                self._score = None
        return self._score


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
