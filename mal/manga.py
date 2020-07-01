from mal.mal import _MAL

from mal import config


class Manga(_MAL):
    def __init__(self, mal_id, timeout=config.TIMEOUT):
        super().__init__(mal_id, "manga", timeout)

    def reload(self):
        self.__init__(self._mal_id)

    @property
    def volumes(self):
        try:
            self._volumes
        except AttributeError:
            self._volumes = self._get_span_text(self._border_spans, "Volumes:", int)
        return self._volumes

    @property
    def chapters(self):
        try:
            self._chapters
        except AttributeError:
            self._chapters = self._get_span_text(self._border_spans, "Chapters:", int)
        return self._chapters

    @property
    def published(self):
        try:
            self._published
        except AttributeError:
            self._published = self._get_span_text(self._border_spans, "Published:", str)
        return self._published

    @property
    def authors(self):
        try:
            self._authors
        except AttributeError:
            self._authors = self._get_span_text(self._border_spans, "Authors:", list)
        return self._authors

    @property
    def related_manga(self):
        try:
            self._related_manga
        except AttributeError:
            self._related_manga = self._get_related()
        return self._related_manga
