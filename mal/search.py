import re
from typing import Optional

from mal import config
from mal.base import _Base


class _SearchResult:
    _image_url_path_regex = r"images\/([a-z]+\/\d+\/\d+)\."
    _mal_id_regex = r"^https:\/\/myanimelist\.net\/.+\/(\d+)\/.+$"

    def __init__(self, tds):
        """
        Search result
        :param tds: Table columns
        """
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
    def url(self) -> str:
        """
        Get URL
        :return: URL
        """
        try:
            self._url
        except AttributeError:
            self._url = self._tds[0].find("a")["href"]
        return self._url

    @property
    def mal_id(self) -> int:
        """
        Get MyAnimeList ID
        :return: MyAnimeList ID
        """
        try:
            self._mal_id
        except AttributeError:
            match = re.match(_SearchResult._mal_id_regex, self.url)
            self._mal_id = int(match.group(1))
        return self._mal_id

    @property
    def image_url(self) -> str:
        """
        Get image URL
        :return: Image URL
        """
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
    def title(self) -> str:
        """
        Get title
        :return: Title
        """
        try:
            self._title
        except AttributeError:
            self._title = self._tds[1].find("strong").text.strip()
        return self._title

    @property
    def synopsis(self) -> str:
        """
        Get synopsis
        :return: Synopsis text
        """
        try:
            self._synopsis
        except AttributeError:
            self._synopsis = self._remove_suffix(
                self._tds[1].find("div", {"class": "pt4"}).text.strip(),
                "read more.",
            )
        return self._synopsis

    @property
    def type(self) -> str:
        """
        Get media type
        :return: Media type
        """
        try:
            self._type
        except AttributeError:
            self._type = self._tds[2].text.strip()
        return self._type

    @property
    def score(self) -> Optional[float]:
        """
        Get score
        :return: Score
        """
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
