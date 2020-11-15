from typing import Optional, List, Dict

from mal import config
from mal.mal import _MAL


class Manga(_MAL):
    def __init__(self, mal_id: int, timeout: int = config.TIMEOUT):
        """
        Manga query by ID
        :param mal_id: MyAnimeList ID
        :param timeout: Timeout in seconds
        """
        super().__init__(mal_id, "manga", timeout)

    def reload(self) -> None:
        """
        Reload manga query
        :return: None
        """
        self.__init__(self._mal_id)

    @property
    def volumes(self) -> Optional[int]:
        """
        Get volumes
        :return: Volumes count
        """
        try:
            self._volumes
        except AttributeError:
            self._volumes = self._get_span_text(self._border_spans, "Volumes:", int)
        return self._volumes

    @property
    def chapters(self) -> Optional[int]:
        """
        Get chapters
        :return: Chapters count
        """
        try:
            self._chapters
        except AttributeError:
            self._chapters = self._get_span_text(self._border_spans, "Chapters:", int)
        return self._chapters

    @property
    def published(self) -> Optional[str]:
        """
        Get published time
        :return: Published time
        """
        try:
            self._published
        except AttributeError:
            self._published = self._get_span_text(self._border_spans, "Published:", str)
        return self._published

    @property
    def authors(self) -> List[str]:
        """
        Get authors
        :return: List of authors
        """
        try:
            self._authors
        except AttributeError:
            self._authors = self._get_span_text(self._border_spans, "Authors:", list)
        return self._authors

    @property
    def related_manga(self) -> Dict[str, List[str]]:
        """
        Get related manga
        :return: Dict of related manga
        """
        try:
            self._related_manga
        except AttributeError:
            self._related_manga = self._get_related()
        return self._related_manga

    @property
    def synopsis(self) -> Optional[str]:
        """
        Get synopsis
        :return: Synopsis text
        """
        try:
            self._synopsis
        except AttributeError:
            self._synopsis = self._get_itemprop_value(
                self._page, "description", "span", str
            )
        return self._synopsis

    @property
    def background(self) -> Optional[str]:
        """
        Get background info
        :return: Background info
        """
        try:
            self._background
        except AttributeError:
            self._background = self._parse_background("h2")
        return self._background
