from typing import List, Optional

from mal import config, base
from mal.search import _Search, _SearchResult


class AnimeSearchResult(_SearchResult):
    def __init__(self, tds):
        """
        Anime search result
        :param tds: Table columns
        """
        super().__init__(tds)

    @property
    @base.property
    def episodes(self) -> Optional[int]:
        """
        Get episodes
        :return: Episodes count
        """
        try:
            self._episodes
        except AttributeError:
            self._episodes = self._parse_eps_vols()
        return self._episodes


class AnimeSearch(_Search):
    def __init__(self, query: str, timeout: int = config.TIMEOUT):
        """
        Anime search by query
        :param query: Query text
        :param timeout: Timeout in seconds
        """
        super().__init__(query, "anime", timeout)

    def reload(self) -> None:
        """
        Reload anime search
        :return: None
        """
        self.__init__(self._query)

    @property
    @base.property_list
    def results(self) -> List[AnimeSearchResult]:
        """
        Get results
        :return: List of anime search results
        """
        try:
            self._results
        except AttributeError:
            trs = self._inner_page.find_all("tr")
            results = []
            for tr in trs[1:]:
                tds = tr.find_all("td")
                results.append(AnimeSearchResult(tds))
            self._results = results
        return self._results
