from typing import Optional, List, Dict

from mal import config, base
from mal.mal import _MAL


class Manga(_MAL):
    def __init__(self, mal_id: int, timeout: int = config.TIMEOUT, debug: int = False):
        """
        Manga query by ID
        :param mal_id: MyAnimeList ID
        :param timeout: Timeout in seconds
        """
        super().__init__(mal_id, "manga", timeout, debug)

    def reload(self) -> None:
        """
        Reload manga query
        :return: None
        """
        self.__init__(self._mal_id)

    def _get_characters(self) -> List[str]:
        """
        Get list of characters
        :param option: 
        :return: List of characters
        """
        data = self._page.find("div", {"class": "detail-characters-list clearfix"}) #staff has the same class as the voice actors, so selecting second tag 
        data = data.findAll('td', {"class": "borderClass"} )[1::2] #since the pics are class 'ac borderClass' they are also selected, skipping them
        characters = [ x.select('a')[0].text for x in data ]
        return characters

    @property
    @base.property
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
    @base.property
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
    @base.property
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
    @base.property_list
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
    @base.property_list
    def characters(self) -> List[str]:
        """
        Get characters
        :return: List of characters
        """
        try:
            self._characters
        except AttributeError:
            self._characters = self._get_characters()
        return self._characters


    @property
    @base.property_dict
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
    @base.property
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
    @base.property
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
