from typing import Optional, List, Dict

from mal import config, _base
from mal._mal import _MAL


class AnimeCharacterResult:
    def __init__(self, name, role, voice_actor):
        """
        Anime character result
        """
        self._name = name
        self._role = role
        self._voice_actor = voice_actor

    @property
    def name(self) -> str:
        return self._name

    @property
    def role(self) -> str:
        return self._role

    @property
    def voice_actor(self) -> str:
        return self._voice_actor


class AnimeStaffResult:
    def __init__(self, name, role):
        """
        Anime staff result
        """
        self._name = name
        self._role = role

    @property
    def name(self) -> str:
        return self._name

    @property
    def role(self) -> str:
        return self._role


class Anime(_MAL):
    def __init__(self, mal_id: int, timeout: int = config.TIMEOUT):
        """
        Anime query by ID
        """
        super().__init__(mal_id, "anime", timeout)

    def reload(self) -> None:
        """
        Reload anime query
        """
        self.__init__(self._mal_id)

    def _get_op_ed(self, option) -> List[str]:
        themes = []
        if option == "op":
            data = self._page.find("div", {"class": "opnening"}).parent
        else:
            data = self._page.find("div", {"class": "ending"}).parent
        data = data.findChildren("td", {"width": "84%"})
        if data:
            if len(data) > 1:
                for theme in data:
                    themes.append(self._clean_text(theme.text[3:]))
            else:
                themes = [self._clean_text(data[0].text)]
        return themes

    def _get_related_anime(self) -> Dict[str, List[str]]:
        # Quickly narrow down header
        headers = self._page.find_all("h2")

        related_header = None  # noqa
        for header in headers:
            if header.text == "Related Anime":
                related_header = header
                break
        else:
            return {}

        data = {}
        rows = related_header.parent.next_sibling.findChildren("tr")

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

    def _get_characters(self) -> List[AnimeCharacterResult]:
        # Quickly narrow down character header
        headers = self._page.find_all("h2")

        character_header = None
        for header in headers:
            if header.text == "Characters & Voice Actors":
                character_header = header
                break

        # Move through DOM to check for the existence of a characters table
        data = character_header.parent.next_sibling
        if "No characters or voice actors have been added to this title" in data:
            return []

        characters = []
        chars = data.findChildren("tr")
        for i, char in enumerate(chars):
            if i % 2 == 0:
                name = char.select('a')[1].text
                role = char.select('small')[0].text
            else:
                actor = char.select('a')[0].text
                characters.append(
                    AnimeCharacterResult(
                        name,  # noqa: name will always be defined
                        role,  # noqa: role will always be defined
                        actor
                    )
                )

        return characters

    def _get_staff(self) -> List[AnimeStaffResult]:
        # Quickly narrow down staff header
        headers = self._page.find_all("h2")

        staff_header = None
        for header in headers:
            if header.text == "Staff":
                staff_header = header
                break

        # Move through DOM to check for the existence of a staff table
        if "No staff for this anime have been added to this title" in staff_header.next_sibling:
            return []

        # Set staff div using relative DOM operations
        # MyAnimeList, please add ids to your site elements.
        # It'll make our lives much easier. Thank you in advanced.
        data = staff_header.parent.next_sibling.next_sibling

        # Since the pics are class 'ac borderClass' they are also selected, skipping
        # them.
        data = data.findAll('td', {"class": "borderClass"})[1::2]

        staff = []
        for i, el in enumerate(data):
            name = el.select('a')[0].text
            role = el.select('div')[0].select('small')[0].text
            staff.append(AnimeStaffResult(name, role))

        return staff

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
    def episodes(self) -> Optional[int]:
        try:
            self._episodes
        except AttributeError:
            self._episodes = self._get_span_text(self._border_spans, "Episodes:", int)
        return self._episodes

    @property
    @_base.property
    def aired(self) -> Optional[str]:
        try:
            self._aired
        except AttributeError:
            self._aired = self._get_span_text(self._border_spans, "Aired:", str)
        return self._aired

    @property
    @_base.property
    def premiered(self) -> Optional[str]:
        try:
            self._premiered
        except AttributeError:
            self._premiered = self._get_span_text(self._border_spans, "Premiered:", str)
        return self._premiered

    @property
    @_base.property
    def broadcast(self) -> Optional[str]:
        try:
            self._broadcast
        except AttributeError:
            self._broadcast = self._get_span_text(self._border_spans, "Broadcast:", str)
        return self._broadcast

    @property
    @_base.property_list
    def producers(self) -> List[str]:
        try:
            self._producers
        except AttributeError:
            self._producers = self._get_span_text(
                self._border_spans, "Producers:", list
            )
        return self._producers

    @property
    @_base.property_list
    def licensors(self) -> List[str]:
        try:
            self._licensors
        except AttributeError:
            self._licensors = self._get_span_text(
                self._border_spans, "Licensors:", list
            )
        return self._licensors

    @property
    @_base.property_list
    def studios(self) -> List[str]:
        try:
            self._studios
        except AttributeError:
            self._studios = self._get_span_text(self._border_spans, "Studios:", list)
        return self._studios

    @property
    @_base.property
    def source(self) -> Optional[str]:
        try:
            self._source
        except AttributeError:
            self._source = self._get_span_text(self._border_spans, "Source:", str)
        return self._source

    @property
    @_base.property
    def duration(self) -> Optional[str]:
        try:
            self._duration
        except AttributeError:
            self._duration = self._get_span_text(self._border_spans, "Duration:", str)
        return self._duration

    @property
    @_base.property
    def rating(self) -> Optional[str]:
        try:
            self._rating
        except AttributeError:
            self._rating = self._get_span_text(self._border_spans, "Rating:", str)
        return self._rating

    @property
    @_base.property_dict
    def related_anime(self) -> Dict[str, List[str]]:
        try:
            self._related_anime
        except AttributeError:
            self._related_anime = self._get_related_anime()
        return self._related_anime

    @property
    @_base.property_list
    def opening_themes(self) -> List[str]:
        try:
            self._opening_themes
        except AttributeError:
            self._opening_themes = self._get_op_ed("op")
        return self._opening_themes

    @property
    @_base.property_list
    def ending_themes(self) -> List[str]:
        try:
            self._ending_themes
        except AttributeError:
            self._ending_themes = self._get_op_ed("ed")
        return self._ending_themes

    @property
    @_base.property_list
    def characters(self) -> List[AnimeCharacterResult]:
        try:
            self._characters
        except AttributeError:
            self._characters = self._get_characters()
        return self._characters

    @property
    @_base.property_list
    def staff(self) -> List[AnimeStaffResult]:
        try:
            self._staff
        except AttributeError:
            self._staff = self._get_staff()
        return self._staff

    @property
    @_base.property
    def synopsis(self) -> Optional[str]:
        try:
            self._synopsis
        except AttributeError:
            self._synopsis = self._get_itemprop_value(
                self._page, "description", "p", str
            )
        return self._synopsis

    @property
    @_base.property
    def background(self) -> Optional[str]:
        try:
            self._background
        except AttributeError:
            self._background = self._parse_background("div")
        return self._background
