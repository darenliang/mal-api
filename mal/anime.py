from mal.mal import _MAL

from mal import config


class Anime(_MAL):
    def __init__(self, mal_id, timeout=config.TIMEOUT):
        super().__init__(mal_id, "anime", timeout)

    def reload(self):
        self.__init__(self._mal_id)

    def _get_op_ed(self, option):
        themes = []
        if option == "op":
            data = self._page.find("div", {"class": "opnening"}).parent
        else:
            data = self._page.find("div", {"class": "ending"}).parent
        data = data.findChildren("span", {"class": "theme-song"})
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
    def episodes(self):
        try:
            self._episodes
        except AttributeError:
            self._episodes = self._get_span_text(self._border_spans, "Episodes:", int)
        return self._episodes

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
    def related_anime(self):
        try:
            self._related_anime
        except AttributeError:
            self._related_anime = self._get_related()
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
