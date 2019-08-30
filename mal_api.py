import re

import requests
from bs4 import BeautifulSoup

import config


class Anime:
    def __init__(self, id):
        self._mal_id = id
        self._url = config.ANIME_ENDPOINT + str(self._mal_id)
        self._page = self._parse_url(self._url)
        title = self._page.find("meta", property="og:title")["content"]
        if title == config.NOT_FOUND_TITLE:
            raise ValueError("No such anime id on MyAnimeList")
        else:
            self._title = title
            url = self._page.find("meta", property="og:url")["content"]
            self._url = url
            self._page_stats = self._parse_url(url + "/stats")
            self._border_spans = self._page.find("td", {'class': 'borderClass'}).findChildren("span",
                                                                                              {'class': 'dark_text'})

    def _parse_url(self, url):
        page_response = requests.get(url, timeout=5)
        return BeautifulSoup(page_response.content, "lxml")

    def _get_span_text(self, page, key, typing, bypass_link=False):
        for span in page:
            if span.get_text() == key:
                first_link = span.parent.a
                if first_link and not bypass_link:
                    if typing == str:
                        return first_link.text
                    if typing == list:
                        return [link.get_text() for link in span.parent.findChildren("a")]
                else:
                    results = span.parent.findChildren(text=True, recursive=True)
                    result = results[results.index(key) + 1].strip()
                    if result == "Unknown":
                        return None
                    else:
                        if typing == int:
                            return int(re.sub('[^0-9]', '', result))
                        if typing == str:
                            return result
                        if typing == list:
                            return [element.strip() for element in result.split(",")]
        if typing == list:
            return []
        return None

    def _get_itemprop_span_value(self, page, itemprop, typing):
        result = page.find("span", itemprop=itemprop).text
        if result:
            if typing == int or typing == float:
                return typing(re.sub('[^0-9.]', '', page.find("span", itemprop=itemprop).text))
            elif typing == str:
                return page.find("span", itemprop=itemprop).text.replace('\n', ' ').replace('\r', '').strip()
        else:
            return None

    def _get_related_anime(self):
        data = {}
        rows = self._page.find("td", {'class': 'pb24'}).table.findChildren("tr")
        for row in rows:
            data[row.td.text[:-1]] = [link.get_text() for link in row.findChildren("a")]
        return data

    def _get_op_ed(self, option):
        themes = []
        if option == "op":
            data = self._page.find("div", {'class': 'opnening'}).parent
        else:
            data = self._page.find("div", {'class': 'ending'}).parent
        data = data.findChildren("span", {'class': 'theme-song'})
        if data:
            if len(data) > 1:
                for theme in data:
                    themes.append(theme.text[4:])
            else:
                themes = [data[0].text]
            return themes
        else:
            return None

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
    def episodes(self):
        try:
            self._episodes
        except AttributeError:
            self._episodes = self._get_span_text(self._border_spans, "Episodes:", int)
        return self._episodes

    @property
    def status(self):
        try:
            self._status
        except AttributeError:
            self._status = self._get_span_text(self._border_spans, "Status:", str)
        return self._status

    @property
    def aired(self):
        try:
            self._aired
        except AttributeError:
            self._aired = self._get_span_text(self._border_spans, "Aired:", str)
        return self._aired

    @property
    def premiered(self):
        try:
            self._premiered
        except AttributeError:
            self._premiered = self._get_span_text(self._border_spans, "Premiered:", str)
        return self._premiered

    @property
    def broadcast(self):
        try:
            self._broadcast
        except AttributeError:
            self._broadcast = self._get_span_text(self._border_spans, "Broadcast:", str)
        return self._broadcast

    @property
    def producers(self):
        try:
            self._producers
        except AttributeError:
            self._producers = self._get_span_text(self._border_spans, "Producers:", list)
        return self._producers

    @property
    def licensors(self):
        try:
            self._licensors
        except AttributeError:
            self._licensors = self._get_span_text(self._border_spans, "Licensors:", list)
        return self._licensors

    @property
    def studios(self):
        try:
            self._studios
        except AttributeError:
            self._studios = self._get_span_text(self._border_spans, "Studios:", list)
        return self._studios

    @property
    def source(self):
        try:
            self._source
        except AttributeError:
            self._source = self._get_span_text(self._border_spans, "Source:", str)
        return self._source

    @property
    def genres(self):
        try:
            self._genres
        except AttributeError:
            self._genres = self._get_span_text(self._border_spans, "Genres:", list)
        return self._genres

    @property
    def duration(self):
        try:
            self._duration
        except AttributeError:
            self._duration = self._get_span_text(self._border_spans, "Duration:", str)
        return self._duration

    @property
    def rating(self):
        try:
            self._rating
        except AttributeError:
            self._rating = self._get_span_text(self._border_spans, "Rating:", str)
        return self._rating

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
            raw_string = self._page.find("h2", {'style': "margin-top: 15px;"}).parent.text
            result = raw_string[raw_string.index("EditBackground") + 14:].replace("\n", " ").replace("\r", "").strip()
            if result == config.NO_BACKGROUND_INFO:
                self._background = None
            else:
                self._background = result
        return self._background

    @property
    def related_anime(self):
        try:
            self._related_anime
        except AttributeError:
            self._related_anime = self._get_related_anime()
        return self._related_anime

    @property
    def opening_themes(self):
        try:
            self._opening_themes
        except AttributeError:
            self._opening_themes = self._get_op_ed("op")
        return self._opening_themes

    @property
    def ending_themes(self):
        try:
            self._ending_themes
        except AttributeError:
            self._ending_themes = self._get_op_ed("ed")
        return self._ending_themes
