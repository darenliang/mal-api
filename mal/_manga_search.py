from typing import List, Optional

from mal import config, _base
from mal._search import _Search, _SearchResult


class MangaSearchResult(_SearchResult):
    def __init__(self, tds):
        """
        Manga search result
        """
        super().__init__(tds)

    """
    Duplicate properties for AutoAPI
    """

    @property
    def mal_id(self) -> int:
        return super().mal_id

    @property
    def title(self) -> str:
        return super().title

    @property
    def url(self) -> str:
        return super().url

    @property
    def image_url(self) -> str:
        return super().image_url

    @property
    def type(self) -> Optional[str]:
        return super().type

    @property
    def score(self) -> Optional[float]:
        return super().score

    @property
    def synopsis(self) -> Optional[str]:
        return super().synopsis

    """
    Duplicate properties for AutoAPI ends here
    """

    @property
    @_base.property
    def volumes(self) -> Optional[int]:
        try:
            self._volumes
        except AttributeError:
            self._volumes = self._parse_eps_vols()
        return self._volumes


class MangaSearch(_Search):
    def __init__(self, query: str, timeout: int = config.TIMEOUT):
        """
        Manga search by query
        """
        super().__init__(query, "manga", timeout)

    def reload(self) -> None:
        """
        Reload manga search
        """
        self.__init__(self._query)

    @property
    @_base.property_list
    def results(self) -> List[MangaSearchResult]:

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
