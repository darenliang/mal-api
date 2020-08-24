from mal import config
from mal.search import _Search, _SearchResult


class MangaSearchResult(_SearchResult):
    def __init__(self, url, image_url, title, synopsis, media_type, volumes, score):
        super().__init__(url, image_url, title, synopsis, media_type, score)
        self.volumes = volumes


class MangaSearch(_Search):
    def __init__(self, query, timeout=config.TIMEOUT):
        super().__init__(query, "manga", timeout)

    def reload(self):
        self.__init__(self._query)

    @property
    def results(self):
        try:
            self._results
        except AttributeError:
            trs = self._inner_page.find_all("tr")
            results = []
            for tr in trs[1:]:
                tds = tr.find_all("td")
                results.append(MangaSearchResult(
                    url=tds[0].find("a")["href"],
                    image_url=tds[0].find("img")["data-src"],
                    title=tds[1].find("strong").text.strip(),
                    synopsis=self._remove_suffix(tds[1].find("div", {"class": "pt4"}).text.strip(), "read more."),
                    media_type=tds[2].text.strip(),
                    volumes=self._parse_eps_vols(tds[3].text),
                    score=self._parse_score(tds[4].text)
                ))
            self._results = results
        return self._results
