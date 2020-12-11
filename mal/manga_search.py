from typing import List, Optional

from mal import config
from mal.search import _Search, _SearchResult


class MangaSearchResult(_SearchResult):
    def __init__(self, tds):
        """
        Manga search result
        :param tds: Table columns
        """
        super().__init__(tds)

    @property
    def volumes(self) -> Optional[int]:
        """
        Get volumes
        :return: Volumes count
        """
        try:
            self._volumes
        except AttributeError:
            self._volumes = self._parse_eps_vols()
        return self._volumes


class MangaSearch(_Search):
    def __init__(self, query: str, timeout: int = config.TIMEOUT):
        """
        Manga search by query
        :param query: Query text
        :param timeout: Timeout in seconds
        """
        super().__init__(query, "manga", timeout)

    def reload(self) -> None:
        """
        Reload manga search
        :return: None
        """
        self.__init__(self._query)

    @property
    def results(self) -> List[MangaSearchResult]:
        """
        Get results
        :return: List of manga search results
        """
        try:
            self._results
        except AttributeError:
            trs = self._inner_page.find_all("tr")
            results = []
            for tr in trs[1:]:
                tds = tr.find_all("td")
                results.append(MangaSearchResult(tds))
            self._results = results
        return self._results
