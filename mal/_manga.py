from typing import Optional, List, Dict

from mal import config, _base
from mal._mal import _MAL


class MangaCharacterResult:
    def __init__(self, name, role):
        """
        Manga character result
        """
        self._name = name
        self._role = role

    @property
    def name(self) -> str:
        return self._name

    @property
    def role(self) -> str:
        return self._role


class Manga(_MAL):
    def __init__(self, mal_id: int, timeout: int = config.TIMEOUT):
        """
        Manga query by ID
        """
        super().__init__(mal_id, "manga", timeout)

    def reload(self) -> None:
        """
        Reload manga query
        """
        self.__init__(self._mal_id)

    def _get_related_manga(self) -> Dict[str, List[str]]:
        # Quickly narrow down header
        headers = self._page.find_all("h2")

        related_header = None  # noqa
        for header in headers:
            if len(header) > 1 and header.contents[1] == "Related Manga":
                related_header = header
                break
        else:
            return {}

        data = {}
        rows = related_header.next_sibling.findChildren("tr")

        key_order = []
        for row in rows:
            key = row.td.text[:-1]
            key_order.append(key)
            data[key] = [link.get_text() for link in row.findChildren("a")]

        # Blame MyAnimeList for having such a broken site
        # Remove duplicates values
        history = set()
        for key in reversed(key_order):
            for el in data[key][:]:
                if el not in history:
                    history.add(el)
                else:
                    data[key].remove(el)
        return data

    def _get_characters(self) -> List[MangaCharacterResult]:
        # Quickly narrow down character header
        headers = self._page.find_all("h2")

        character_header = None
        for header in headers:
            # MyAnimeList, can you please stop making your pages different?
            if len(header) > 1 and header.contents[1] == "Characters":
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
                MangaCharacterResult(
                    name,  # noqa: name will always be defined
                    role,  # noqa: role will always be defined
                )
            )

        return characters

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
    def title_english(self) -> str:
        return super().title_english

    @property
    def title_japanese(self) -> str:
        return super().title_japanese

    @property
    def title_synonyms(self) -> List[str]:
        return super().title_synonyms

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
    def status(self) -> Optional[str]:
        return super().status

    @property
    def genres(self) -> List[str]:
        return super().genres

    @property
    def score(self) -> Optional[float]:
        return super().score

    @property
    def scored_by(self) -> Optional[int]:
        return super().scored_by

    @property
    def rank(self) -> Optional[int]:
        return super().rank

    @property
    def popularity(self) -> Optional[int]:
        return super().popularity

    @property
    def members(self) -> Optional[int]:
        return super().members

    @property
    def favorites(self) -> Optional[int]:
        return super().favorites

    """
    Duplicate properties for AutoAPI ends here
    """

    @property
    @_base.property
    def volumes(self) -> Optional[int]:
        try:
            self._volumes
        except AttributeError:
            self._volumes = self._get_span_text(self._border_spans, "Volumes:", int)
        return self._volumes

    @property
    @_base.property
    def chapters(self) -> Optional[int]:
        try:
            self._chapters
        except AttributeError:
            self._chapters = self._get_span_text(self._border_spans, "Chapters:", int)
        return self._chapters

    @property
    @_base.property
    def published(self) -> Optional[str]:
        try:
            self._published
        except AttributeError:
            self._published = self._get_span_text(self._border_spans, "Published:", str)
        return self._published

    @property
    @_base.property_list
    def authors(self) -> List[str]:
        try:
            self._authors
        except AttributeError:
            self._authors = self._get_span_text(self._border_spans, "Authors:", list)
        return self._authors

    @property
    @_base.property_list
    def characters(self) -> List[MangaCharacterResult]:
        try:
            self._characters
        except AttributeError:
            self._characters = self._get_characters()
        return self._characters

    @property
    @_base.property_dict
    def related_manga(self) -> Dict[str, List[str]]:
        try:
            self._related_manga
        except AttributeError:
            self._related_manga = self._get_related_manga()
        return self._related_manga

    @property
    @_base.property
    def synopsis(self) -> Optional[str]:
        try:
            self._synopsis
        except AttributeError:
            self._synopsis = self._get_itemprop_value(
                self._page, "description", "span", str
            )
        return self._synopsis

    @property
    @_base.property
    def background(self) -> Optional[str]:
        try:
            self._background
        except AttributeError:
            self._background = self._parse_background("h2")
        return self._background
