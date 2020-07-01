import re

from mal import config
from mal.base import _Base


class _MAL(_Base):
    def __init__(self, mal_id, mal_type, timeout):
        super().__init__(timeout)
        self._mal_id = mal_id
        self._url = config.MAL_ENDPOINT + "{}/{}".format(mal_type, mal_id)
        self._page = self._parse_url(self._url)
        title = self._page.find("meta", property="og:title")["content"]
        if title == config.NOT_FOUND_TITLE:
            raise ValueError("No such id on MyAnimeList")
        else:
            self._title = title
            url = self._page.find("meta", property="og:url")["content"]
            self._url = url
            self._page_stats = self._parse_url(url + "/stats")
            self._border_spans = self._page.find("td", {"class": "borderClass"}).findChildren("span",
                                                                                              {"class": "dark_text"})

    @staticmethod
    def _get_span_text(page, key, typing, bypass_link=False):
        for span in page:
            if span.get_text() == key:
                first_link = span.parent.a
                if first_link and not bypass_link:
                    if typing == str:
                        return first_link.text
                    if typing == list:
                        res = [link.get_text() for link in span.parent.findChildren("a")]
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
    def _get_itemprop_span_value(page, itemprop, typing):
        result = page.find("span", itemprop=itemprop)
        if result is not None:
            if typing == int or typing == float:
                return typing(re.sub("[^0-9.]", "", result.text))
            elif typing == str:
                return result.text.replace("\n", " ").replace("\r", "").strip()
        else:
            return None

    def _get_related(self):
        data = {}
        rows = self._page.find("td", {"class": "pb24"}).table.findChildren("tr")
        for row in rows:
            data[row.td.text[:-1]] = [link.get_text() for link in row.findChildren("a")]
        return data

    @property
    def mal_id(self):
        return self._mal_id

    @property
    def title(self):
        return self._title

    @property
    def title_english(self):
        try:
            self._title_english
        except AttributeError:
            self._title_english = self._get_span_text(self._border_spans, "English:", str)
        return self._title_english

    @property
    def title_japanese(self):
        try:
            self._title_japanese
        except AttributeError:
            self._title_japanese = self._get_span_text(self._border_spans, "Japanese:", str)
        return self._title_japanese

    @property
    def title_synonyms(self):
        try:
            self._title_synonyms
        except AttributeError:
            self._title_synonyms = self._get_span_text(self._border_spans, "Synonyms:", list)
        return self._title_synonyms

    @property
    def url(self):
        return self._url

    @property
    def image_url(self):
        try:
            self._image_url
        except AttributeError:
            self._image_url = self._page.find("meta", property="og:image")["content"]
        return self._image_url

    @property
    def type(self):
        try:
            self._type
        except AttributeError:
            self._type = self._get_span_text(self._border_spans, "Type:", str)
        return self._type

    @property
    def status(self):
        try:
            self._status
        except AttributeError:
            self._status = self._get_span_text(self._border_spans, "Status:", str)
        return self._status

    @property
    def genres(self):
        try:
            self._genres
        except AttributeError:
            self._genres = self._get_span_text(self._border_spans, "Genres:", list)
        return self._genres

    @property
    def score(self):
        try:
            self._score
        except AttributeError:
            self._score = self._get_itemprop_span_value(self._page, "ratingValue", float)
        return self._score

    @property
    def scored_by(self):
        try:
            self._scored_by
        except AttributeError:
            self._scored_by = self._get_itemprop_span_value(self._page, "ratingCount", int)
        return self._scored_by

    @property
    def rank(self):
        try:
            self._rank
        except AttributeError:
            self._rank = self._get_span_text(self._border_spans, "Ranked:", int, True)
        return self._rank

    @property
    def popularity(self):
        try:
            self._popularity
        except AttributeError:
            self._popularity = self._get_span_text(self._border_spans, "Popularity:", int)
        return self._popularity

    @property
    def members(self):
        try:
            self._members
        except AttributeError:
            self._members = self._get_span_text(self._border_spans, "Members:", int)
        return self._members

    @property
    def favorites(self):
        try:
            self._favorites
        except AttributeError:
            self._favorites = self._get_span_text(self._border_spans, "Favorites:", int)
        return self._favorites

    @property
    def synopsis(self):
        try:
            self._synopsis
        except AttributeError:
            self._synopsis = self._get_itemprop_span_value(self._page, "description", str)
        return self._synopsis

    @property
    def background(self):
        try:
            self._background
        except AttributeError:
            raw_string = self._page.find("h2", {"style": "margin-top: 15px;"}).parent.text
            result = raw_string[raw_string.index("EditBackground") + 14:].replace("\n", " ").replace("\r", "").strip()
            if result == config.NO_BACKGROUND_INFO:
                self._background = None
            else:
                self._background = result
        return self._background
