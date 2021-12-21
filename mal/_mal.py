import re
from typing import Any, Optional, List, Dict

from mal import config, _base
from mal._base import _Base


class _MAL(_Base):
    def __init__(self, mal_id, mal_type, timeout):
        super().__init__(timeout)
        self._mal_id = mal_id
        self._url = config.MAL_ENDPOINT + "{}/{}".format(mal_type, mal_id)
        self._page = self._parse_url(self._url)
        title = self._page.find("meta", property="og:title")["content"]
        if title == "404 Not Found - MyAnimeList.net ":
            raise ValueError("No such id on MyAnimeList")
        self._title = title
        url = self._page.find("meta", property="og:url")["content"]
        self._url = url

        # Not used right now
        self._page_stats = self._parse_url(url + "/stats")

        self._border_spans = self._page.find(
            "td", {"class": "borderClass"}
        ).findChildren("span", {"class": "dark_text"})

    @staticmethod
    def _get_span_text(page, key, typing, bypass_link=False) -> Any:
        for span in page:
            if span.get_text() == key:
                first_link = span.parent.a
                if first_link and not bypass_link:
                    if typing == str:
                        return first_link.text
                    if typing == list:
                        res = [
                            link.get_text().strip() for link in span.parent.findChildren("a")
                        ]
                        if "add some" in res:
                            res.remove("add some")
                        return res
                else:
                    results = span.parent.findChildren(text=True, recursive=True)
                    result = results[results.index(key) + 1].strip()
                    if result == "Unknown":
                        return None
                    else:
                        if typing == int:
                            num = re.sub("[^0-9]", "", result)
                            if num:
                                return int(num)
                            else:
                                return None
                        if typing == str:
                            return result
                        if typing == list:
                            return [element.strip() for element in result.split(",")]
        if typing == list:
            return []
        return None

    @staticmethod
    def _get_itemprop_value(page, itemprop, element, typing) -> Any:
        result = page.find(element, itemprop=itemprop)
        if result is not None:
            if typing == int or typing == float:
                return typing(re.sub("[^0-9.]", "", result.text))
            elif typing == str:
                return result.text.replace("\n", " ").replace("\r", "").strip()
        else:
            return None

    @staticmethod
    def _clean_text(text) -> str:
        return text.strip().replace(u"\xa0", " ")

    def _parse_background(self, element) -> Optional[str]:
        raw_string = self._page.find(
            element, {"style": "margin-top: 15px;"}
        ).parent.text
        result = (
            raw_string[raw_string.index("EditBackground") + 14:]
                .replace("\n", " ")
                .replace("\r", "")
                .strip()
        )
        if result == "No background information has been added to this title. " \
                     "Help improve our database by adding background information here.":
            return None
        return result

    @property
    @_base.property
    def mal_id(self) -> int:
        return self._mal_id

    @property
    @_base.property
    def title(self) -> str:
        return self._title

    @property
    @_base.property
    def title_english(self) -> str:
        try:
            self._title_english
        except AttributeError:
            self._title_english = self._get_span_text(
                self._border_spans, "English:", str
            )
        return self._title_english

    @property
    @_base.property
    def title_japanese(self) -> str:
        try:
            self._title_japanese
        except AttributeError:
            self._title_japanese = self._get_span_text(
                self._border_spans, "Japanese:", str
            )
        return self._title_japanese

    @property
    @_base.property_list
    def title_synonyms(self) -> List[str]:
        try:
            self._title_synonyms
        except AttributeError:
            self._title_synonyms = self._get_span_text(
                self._border_spans, "Synonyms:", list
            )
        return self._title_synonyms

    @property
    @_base.property
    def url(self) -> str:
        return self._url

    @property
    @_base.property
    def image_url(self) -> Optional[str]:
        try:
            self._image_url
        except AttributeError:
            self._image_url = self._page.find("meta", property="og:image")["content"]
        return self._image_url

    @property
    @_base.property
    def type(self) -> Optional[str]:
        try:
            self._type
        except AttributeError:
            self._type = self._get_span_text(self._border_spans, "Type:", str)
        return self._type

    @property
    @_base.property
    def status(self) -> Optional[str]:
        try:
            self._status
        except AttributeError:
            self._status = self._get_span_text(self._border_spans, "Status:", str)
        return self._status

    @property
    @_base.property_list
    def genres(self) -> List[str]:
        try:
            self._genres
        except AttributeError:
            genres = self._get_span_text(self._border_spans, "Genres:", list)
            if not genres:
                self._genres = self._get_span_text(self._border_spans, "Genre:", list)
            else:
                self._genres = genres
        return self._genres

    @property
    @_base.property_list
    def themes(self) -> List[str]:
        try:
            self._themes
        except AttributeError:
            themes = self._get_span_text(self._border_spans, "Themes:", list)
            if not themes:
                self._themes = self._get_span_text(self._border_spans, "Theme:", list)
            else:
                self._themes = themes
        return self._themes

    @property
    @_base.property
    def score(self) -> Optional[float]:
        try:
            self._score
        except AttributeError:
            self._score = self._get_itemprop_value(
                self._page, "ratingValue", "span", float
            )
        return self._score

    @property
    @_base.property
    def scored_by(self) -> Optional[int]:
        try:
            self._scored_by
        except AttributeError:
            self._scored_by = self._get_itemprop_value(
                self._page, "ratingCount", "span", int
            )
        return self._scored_by

    @property
    @_base.property
    def rank(self) -> Optional[int]:
        try:
            self._rank
        except AttributeError:
            self._rank = self._get_span_text(self._border_spans, "Ranked:", int, True)
        return self._rank

    @property
    @_base.property
    def popularity(self) -> Optional[int]:
        try:
            self._popularity
        except AttributeError:
            self._popularity = self._get_span_text(
                self._border_spans, "Popularity:", int
            )
        return self._popularity

    @property
    @_base.property
    def members(self) -> Optional[int]:
        try:
            self._members
        except AttributeError:
            self._members = self._get_span_text(self._border_spans, "Members:", int)
        return self._members

    @property
    @_base.property
    def favorites(self) -> Optional[int]:
        try:
            self._favorites
        except AttributeError:
            self._favorites = self._get_span_text(self._border_spans, "Favorites:", int)
        return self._favorites
