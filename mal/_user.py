import math
import re
from datetime import datetime, timezone, timedelta
from typing import Optional, List, Dict

import requests
from dateutil.parser import parse

from mal import config
from mal._base import _Base


class User(_Base):
    def __init__(
        self, username: str, friends: bool = True, anime_list: bool = True,
        manga_list: bool = True, timeout: int = config.TIMEOUT
    ):
        super().__init__(timeout)
        if not (2 <= len(username) <= 16):
            raise ValueError(
                "Username has to be between 2 and 16 characters long"
            )
        self._url = config.MAL_ENDPOINT + "profile/{}".format(username)
        self._page = self._parse_url(self._url)
        if self._page.select_one(".display-submit"):
            raise Exception("Temporarily blocked by MyAnimeList")
        self._username = self._page.select_one(
            "meta[property='og:url']"
        )["content"].split("/")[-1]
        title = self._page.select_one("meta[property='og:title']")["content"]
        if title == "404 Not Found - MyAnimeList.net ":
            raise ValueError("No such user on MyAnimeList")

        user_image = self._page.select_one(".user-image > img")
        self._image_url = user_image["data-src"] if user_image else None
        self._user_id = int(self._image_url.split('/')[-1].split('.')[0])

        self._last_online = None
        self._gender = None
        self._birthday = None
        self._location = None
        self._joined = None
        for row in self._page.select_one(".user-status").select("li"):
            title = row.select_one(".user-status-title").text
            if title == "Supporter":
                continue
            data = row.select_one(".user-status-data").text
            if title == "Last Online":
                self._last_online = self._parse_date(data)
            elif title == "Gender":
                self._gender = data
            elif title == "Birthday":
                self._birthday = self._parse_date(data)
            elif title == "Location":
                self._location = data
            elif title == "Joined":
                self._joined = self._parse_date(data)

        anime_stats = self._page.select_one(".stats.anime")
        anime_watching_stats = \
            anime_stats.select_one(".stats-status").select("li")
        anime_other_stats = \
            anime_stats.select_one(".stats-data").select("li")

        def get_stats(stats):
            return int(stats.select_one("span").text.replace(",", ""))

        def get_other_stats(stats):
            return int(
                stats.select_one("span:nth-child(2)").text.replace(",", "")
            )

        self._anime_stats = {
            "days_watched": float(
                anime_stats.select_one(".stat-score > div")
                    .text.split()[1].replace(",", "")
            ),
            "mean_score": float(anime_stats.select_one(".score-label").text),
            "watching": get_stats(anime_watching_stats[0]),
            "completed": get_stats(anime_watching_stats[1]),
            "on_hold": get_stats(anime_watching_stats[2]),
            "dropped": get_stats(anime_watching_stats[3]),
            "plan_to_watch": get_stats(anime_watching_stats[4]),
            "total_entries": get_other_stats(anime_other_stats[0]),
            "rewatched": get_other_stats(anime_other_stats[1]),
            "episodes_watched": get_other_stats(anime_other_stats[2]),
        }

        manga_stats = self._page.select_one(".stats.manga")
        manga_reading_stats = \
            manga_stats.select_one(".stats-status").select("li")
        manga_other_stats = \
            manga_stats.select_one(".stats-data").select("li")

        self._manga_stats = {
            "days_read": float(
                manga_stats.select_one(".stat-score > div")
                    .text.split()[1].replace(",", "")
            ),
            "mean_score": float(manga_stats.select_one(".score-label").text),
            "reading": get_stats(manga_reading_stats[0]),
            "completed": get_stats(manga_reading_stats[1]),
            "on_hold": get_stats(manga_reading_stats[2]),
            "dropped": get_stats(manga_reading_stats[3]),
            "plan_to_read": get_stats(manga_reading_stats[4]),
            "total_entries": get_other_stats(manga_other_stats[0]),
            "reread": get_other_stats(manga_other_stats[1]),
            "chapters_read": get_other_stats(manga_other_stats[2]),
            "volumes_read": get_other_stats(manga_other_stats[3]),
        }

        self._favorites = {
            "anime": None if
            self._page.select_one("#anime_favorites") is None
            else [int(re.search("anime/(.*)/", fa["href"]).group(1)) for fa
                  in self._page.select("#anime_favorites a")],
            "manga": None if
            self._page.select_one("#manga_favorites") is None
            else [int(re.search("manga/(.*)/", fm["href"]).group(1)) for fm
                  in self._page.select("#manga_favorites a")],
            "characters": None if
            self._page.select_one("#character_favorites") is None
            else [int(re.search("character/(.*)/", fc["href"]).group(1)) for fc
                  in self._page.select("#character_favorites a")],
            "people": None if
            self._page.select_one("#person_favorites") is None
            else [int(re.search("people/(.*)/", fp["href"]).group(1)) for fp
                  in self._page.select("#person_favorites a")]
        }

        self._about = self._page.select_one(".word-break")
        if self._about:
            self._about = self._about.text

        self._friend_count = int(
            self._page.select_one(
                f"a[href=\"https://myanimelist.net/profile/{self._username}"
                f"/friends\"]").text.replace("All (", "")[:-1])

    @staticmethod
    def _parse_date(date) -> datetime:
        if "Now" in date:
            return datetime.now(timezone.utc)
        elif "minutes" in date:
            return datetime.now(timezone.utc) - timedelta(
                minutes=int(date.split()[0]))
        elif "hours" in date:
            return datetime.now(timezone.utc) - timedelta(
                hours=int(date.split()[0]))
        elif "hour" in date:
            return datetime.now(timezone.utc) - timedelta(hours=1)
        elif "Today" in date:
            return parse(date.split()[1])
        elif "Yesterday" in date:
            return parse(date.split()[1]) - timedelta(days=1)
        else:
            return parse(date)

    def _get_friends(self) -> List[Dict[str, str]]:
        friends = []
        if self._friend_count != 0:
            for i in range(1, (math.ceil(self._friend_count / 100)) + 1):
                friend_page = self._parse_url(
                    f"{config.MAL_ENDPOINT}profile/{self._username}/friends?p={i}")
                if friend_page.select_one(".display-submit") is not None:
                    raise Exception("Temporarily blocked by MyAnimeList")

                friends.extend([{"username": friend.select_one("a").text,
                                 "friends_since": self._parse_date(
                                     friend.findChildren("div")[2]
                                         .text.replace(
                                         "\n      Friends since ", ""
                                     )[:-4]) if len(
                                     friend.select("div")) >= 3 else None}
                                for friend in
                                friend_page.select(".data")])
        return friends

    def _get_anime_list(self) -> List[Dict[str, int]]:
        anime_list = []
        for i in range(math.ceil(self._anime_stats["total_entries"] / 300)):
            r_alist = requests.get(
                f"{config.MAL_ENDPOINT}animelist/{self._username}/load.json?status=7&offset={i * 300}")
            anime_list.extend([{"title": a["anime_title"],
                                "mal_id": a["anime_id"],
                                "status": a["status"],
                                "score": a["score"],
                                "tags": a["tags"],
                                "is_rewatching": a["is_rewatching"],
                                "watched_episodes": a["num_watched_episodes"],
                                "total_episodes": a["anime_num_episodes"],
                                "start_date": a["start_date_string"],
                                "finish_date": a["finish_date_string"],
                                "priority": a["priority_string"]}
                               for a in r_alist.json()])
        return anime_list

    def _get_manga_list(self) -> List[Dict[str, int]]:
        manga_list = []
        for i in range(math.ceil(self._manga_stats["total_entries"] / 300)):
            r_mlist = requests.get(
                f"{config.MAL_ENDPOINT}mangalist/{self._username}/load.json?status=7&offset={i * 300}")
            manga_list.extend([{"title": m["manga_title"],
                                "mal_id": m["manga_id"],
                                "status": m["status"],
                                "type": m["manga_media_type_string"],
                                "score": m["score"],
                                "tags": m["tags"],
                                "is_rereading": m["is_rereading"],
                                "read_chapters": m["num_read_chapters"],
                                "read_volumes": m["num_read_volumes"],
                                "total_chapters": m["manga_num_chapters"],
                                "total_volumes": m["manga_num_volumes"],
                                "start_date": m["start_date_string"],
                                "finish_date": m["finish_date_string"],
                                "priority": m["priority_string"]}
                               for m in r_mlist.json()])
        return manga_list

    @property
    def username(self) -> str:
        return self._username

    @property
    def url(self) -> str:
        return self._url

    @property
    def image(self) -> Optional[str]:
        return self._image_url

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def last_online(self) -> Optional[datetime]:
        return self._last_online

    @property
    def gender(self) -> Optional[str]:
        return self._gender

    @property
    def birthday(self) -> Optional[datetime]:
        return self._birthday

    @property
    def location(self) -> Optional[str]:
        return self._location

    @property
    def joined(self) -> Optional[datetime]:
        return self._joined

    @property
    def anime_stats(self) -> Dict[str, float]:
        return self._anime_stats

    @property
    def manga_stats(self) -> Dict[str, float]:
        return self._manga_stats

    @property
    def favorites(self) -> Dict[str, Optional[int]]:
        return self._favorites

    @property
    def about(self) -> Optional[str]:
        return self._about

    @property
    def friend_count(self) -> int:
        return self._friend_count

    @property
    def friends(self) -> Optional[List[Dict[str, str]]]:
        try:
            self._friends
        except AttributeError:
            self._friends = self._get_friends() if self.friends else None
        return self._friends

    @property
    def anime_list(self) -> Optional[List[Dict[str, int]]]:
        try:
            self._anime_list
        except AttributeError:
            self._anime_list = self._get_anime_list() \
                if self.anime_list and \
                   self._page.select_one(".anime.updates p") is None \
                else None
        return self._anime_list

    @property
    def manga_list(self) -> Optional[List[Dict[str, int]]]:
        try:
            self._manga_list
        except AttributeError:
            self._manga_list = self._get_manga_list() \
                if self.manga_list and \
                   self._page.select_one(".manga.updates p") is None \
                else None
        return self._manga_list
