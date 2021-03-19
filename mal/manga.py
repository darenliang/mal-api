from typing import Optional, List, Dict

from mal import config, base
from mal.mal import _MAL


class MangaCharacter:
    def __init__(self, name, role):
        """
        Manga character
        :param name: Character name
        :param role: Role
        """
        self.name: str = name
        self.role: str = role


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

    def _get_characters(self) -> List[MangaCharacter]:
        """
        Get list of characters
        :return: List of characters
        """
        # Quickly narrow down character header
        td = self._page.find("td", {"class": "pb24"})
        headers = td.find_all("h2")

        character_header = None
        for header in headers:
            # MyAnimeList, can you please stop making your pages different?
            if header.contents[1] == "Characters":
                character_header = header
                break

        # Move through DOM to check for the existence of a characters table
        data = character_header.next_sibling
        if "No characters for this manga have been added to this title" in data:
            return []

        characters = []
        chars = data.findChildren("tr")
        for i, char in enumerate(chars):
            name = char.select('a')[1].text
            role = char.select('small')[0].text
            characters.append(
                MangaCharacter(
                    name,  # noqa: name will always be defined
                    role,  # noqa: role will always be defined
                )
            )

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
    def characters(self) -> List[MangaCharacter]:
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
