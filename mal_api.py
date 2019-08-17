import locale
import os
import re

import requests
from bs4 import BeautifulSoup

import stats


def parse_url(s):
    page_response = requests.get(s, timeout=5)
    return BeautifulSoup(page_response.content, "html.parser")


class Anime:
    def __init__(self, id):
        self._id = id
        self._url = "https://myanimelist.net/anime/" + str(id)
        self._page = self.parse_url(self._url)
        if self._page.find('title').text.strip() == "404 Not Found - MyAnimeList.net":
            raise ValueError("No such anime id on MyAnimeList")
        else:
            self._page_stats = self.parse_url(self._page.find('a', href=re.compile('/stats$'))['href'])

    def parse_url(self, url):
        page_response = requests.get(url, timeout=5)
        return BeautifulSoup(page_response.content, "html.parser")

    @property
    def name(self):
        try:
            self._name
        except AttributeError:
            self._name = self._page.find("span", itemprop="name").text
        return self._name

    @property
    def image(self):
        try:
            self._image
        except AttributeError:
            self._image = self._page.find('img', class_="ac")['src']
        return self._image

    @property
    def type(self):
        try:
            self._type
        except AttributeError:
            key = "Type:"
            if key not in self._page.text:
                return None
            self._type = self._page.find(text=key).findNext('a').text
        return self._type

    @property
    def episodes(self):
        try:
            self._episodes
        except AttributeError:
            key = "Episodes:"
            if key not in self._page.text:
                return None
            self._episodes = re.sub(r'\W+', '', str(self._page.find(text=key).next))
        return self._episodes

    @property
    def status(self):
        try:
            self._status
        except AttributeError:
            key = "Status:"
            if key not in self._page.text:
                return None
            temp = str(self._page.find('span', text=key).parent)
            no_whitespace = ''
            for i in temp:
                if i != '\n':
                    no_whitespace += i
            status = re.search('</span> {2}(.*) {2}</div>', no_whitespace)
            self._status = status.group(1)
        return self._status

    @property
    def aired(self):
        try:
            self._aired
        except AttributeError:
            key = "Aired:"
            if key not in self._page.text:
                return None
            self._aired = self._page.find(text=key).next.strip(" \n")
        return self._aired

    @property
    def premiered(self):
        try:
            self._premiered
        except AttributeError:
            key = "Premiered:"
            if key not in self._page.text:
                return None
            self._premiered = self._page.find(text=key).findNext('a').text
        return self._premiered

    @property
    def broadcast(self):
        try:
            self._broadcast
        except AttributeError:
            key = "Broadcast:"
            if key not in self._page.text:
                return None
            self._broadcast = self._page.find(text=key).next.strip(" \n")
        return self._broadcast

    @property
    def producers(self):
        try:
            self._producers
        except AttributeError:
            key = "Producers:"
            if key not in self._page.text:
                return None
            self._producers = self._page.find(text=key).parent.parent.findAll('a')
            for i in range(len(self._producers)):
                self._producers[i] = self._producers[i].text
        return self._producers

    @property
    def licensors(self):
        try:
            self._licensors
        except AttributeError:
            key = "Licensors:"
            if key not in self._page.text:
                return None
            self._licensors = self._page.find(text=key).parent.parent.findAll('a')
            for i in range(len(self._licensors)):
                self._licensors[i] = self._licensors[i].text
        return self._licensors

    @property
    def studios(self):
        try:
            self._studios
        except AttributeError:
            key = "Studios:"
            if key not in self._page.text:
                return None
            self._studios = self._page.find(text=key).findNext('a').text
        return self._studios

    @property
    def source(self):
        try:
            self._source
        except AttributeError:
            key = "Source:"
            if key not in self._page.text:
                return None
            self._source = self._page.find(text=key).next.strip(" \n")
        return self._source

    @property
    def genres(self):
        try:
            self._genres
        except AttributeError:
            key = "Genres:"
            if key not in self._page.text:
                return None
            self._genres = self._page.find(text=key).parent.parent.findAll('a')
            for i in range(len(self._genres)):
                self._genres[i] = self._genres[i].text
        return self._genres

    @property
    def duration(self):
        try:
            self._duration
        except AttributeError:
            key = "Duration:"
            if key not in self._page.text:
                return None
            self._duration = self._page.find(text=key).next.strip(" \n")
        return self._duration

    @property
    def rating(self):
        try:
            self._rating
        except AttributeError:
            key = "Rating:"
            if key not in self._page.text:
                return None
            self._rating = self._page.find(text=key).next.strip(" \n")
        return self._rating

    @property
    def score(self):
        try:
            self._score
        except AttributeError:
            key = "Score:"
            if key not in self._page.text:
                return None
            self._score = str(self._page.find(text=key).next.next.text)
        return self._score

    @property
    def rank(self):
        try:
            self._rank
        except AttributeError:
            key = "Ranked:"
            if key not in self._page.text:
                return None
            self._rank = str((self._page.find(text=key).next.strip(" \n"))[1:])
        return self._rank

    @property
    def popularity(self):
        try:
            self._popularity
        except AttributeError:
            key = "Popularity:"
            if key not in self._page.text:
                return None
            self._popularity = str((self._page.find(text=key).next.strip(" \n"))[1:])
        return self._popularity

    @property
    def members(self):
        try:
            self._members
        except AttributeError:
            key = "Members:"
            if key not in self._page.text:
                return None
            self._members = str(locale.atoi(self._page.find(text=key).next.strip(" \n")))
        return self._members

    @property
    def favorites(self):
        try:
            self._favorites
        except AttributeError:
            key = "Favorites:"
            if key not in self._page.text:
                return None
            self._favorites = str(locale.atoi(self._page.find(text=key).next.strip(" \n")))
        return self._favorites

    @property
    def synopsis(self):
        try:
            self._synopsis
        except AttributeError:
            key = "Synopsis"
            if key not in self._page.text:
                return None
            self._synopsis = self._page.find("span", itemprop="description").text
        return self._synopsis

    @property
    def adaptation(self):
        try:
            self._adaptation
        except AttributeError:
            key = "Adaptation:"
            if key not in self._page.text:
                return None
            self._adaptation = self._page.find(text=key).next.findAll('a')
            for i in range(len(self._adaptation)):
                self._adaptation[i] = self._adaptation[i].text
        return self._adaptation

    @property
    def sidestory(self):
        try:
            self._sidestory
        except AttributeError:
            key = "Side story:"
            if key not in self._page.text:
                return None
            self._sidestory = self._page.find(text=key).next.findAll('a')
            for i in range(len(self._sidestory)):
                self._sidestory[i] = self._sidestory[i].text
        return self._sidestory

    @property
    def alternative(self):
        try:
            self._alternative
        except AttributeError:
            key = "Alternative setting:"
            if key not in self._page.text:
                return None
            self._alternative = self._page.find(text=key).next.findAll('a')
            for i in range(len(self._alternative)):
                self._alternative[i] = self._alternative[i].text
        return self._alternative

    @property
    def sequel(self):
        try:
            self._sequel
        except AttributeError:
            key = "Sequel:"
            if key not in self._page.text:
                return None
            self._sequel = self._page.find(text=key).next.findAll('a')
            for i in range(len(self._sequel)):
                self._sequel[i] = self._sequel[i].text
        return self._sequel

    @property
    def summary(self):
        try:
            self._summary
        except AttributeError:
            key = "Summary:"
            if key not in self._page.text:
                return None
            self._summary = self._page.find(text=key).next.findAll('a')
            for i in range(len(self._summary)):
                self._summary[i] = self._summary[i].text
        return self._summary

    @property
    def other(self):
        try:
            self._other
        except AttributeError:
            key = "Other:"
            if key not in self._page.text:
                return None
            self._other = self._page.find(text=key).next.findAll('a')
            for i in range(len(self._other)):
                self._other[i] = self._other[i].text
        return self._other

    @property
    def prequel(self):
        try:
            self._prequel
        except AttributeError:
            key = "Prequel:"
            if key not in self._page.text:
                return None
            self._prequel = self._page.find(text=key).next.findAll('a')
            for i in range(len(self._prequel)):
                self._prequel[i] = self._prequel[i].text
        return self._prequel

    @property
    def spinoff(self):
        try:
            self._spinoff
        except AttributeError:
            key = "Spin-off:"
            if key not in self._page.text:
                return None
            self._spinoff = self._page.find(text=key).next.findAll('a')
            for i in range(len(self._spinoff)):
                self._spinoff[i] = self._spinoff[i].text
        return self._spinoff

    @property
    def character(self):
        try:
            self._character
        except AttributeError:
            key = "Character:"
            if key not in self._page.text:
                return None
            self._character = self._page.find(text=key).next.findAll('a')
            for i in range(len(self._character)):
                self._character[i] = self._character[i].text
        return self._character

    @property
    def version(self):
        try:
            self._version
        except AttributeError:
            key = "Alternative version:"
            if key not in self._page.text:
                return None
            self._version = self._page.find(text=key).next.findAll('a')
            for i in range(len(self._version)):
                self._version[i] = self._version[i].text
        return self._version

    @property
    def maincast(self):
        try:
            self._maincast
        except AttributeError:
            key = "Characters & Voice Actors"
            if key not in self._page.text:
                return None
            cast = os.linesep.join([s for s in self._page.find(text=key).next.text.splitlines() if s])
            tempcast = cast.split("\n")
            for i in range(len(tempcast)):
                tempcast[i] = tempcast[i].replace('\r', '')
                self._maincast = []
            for i in range(0, len(tempcast), 4):
                self._maincast.append([tempcast[i], tempcast[i + 1], tempcast[i + 2], tempcast[i + 3]])
        return self._maincast

    @property
    def staff(self):
        try:
            self._staff
        except AttributeError:
            key = "More staff"
            if key not in self._page.text:
                return None
            staff = os.linesep.join([s for s in self._page.find(text=key,
                                                                class_="floatRightHeader").next.next.next.next.next.text.splitlines()
                                     if s])
            tempstaff = staff.split("\n")
            for i in range(len(tempstaff)):
                tempstaff[i] = tempstaff[i].replace('\r', '')
            self._staff = []
            for i in range(0, len(tempstaff), 2):
                self._staff.append([tempstaff[i], tempstaff[i + 1]])
        return self._staff

    @property
    def op(self):
        try:
            self._op
        except AttributeError:
            key = "No opening themes have been added to this title."
            if key in self._page.text:
                return None
            tempop = self._page.findAll(class_="theme-song")
            tempop2 = []
            self._op = []
            inc = 0
            for i in range(len(tempop)):
                tempop2.append(tempop[i].text)
            if tempop2[0][0] != '#':
                return [tempop2[0]]
            for i in range(len(tempop2)):
                if tempop2[i][1].isdigit() and inc < int(tempop2[i][1]):
                    inc = int(tempop2[i][1])
                    self._op.append(tempop[i].text)
                else:
                    return self._op
        return self._op

    @property
    def ed(self):
        try:
            self._ed
        except AttributeError:
            key = "No ending themes have been added to this title."
            if key in self._page.text:
                return None
            temped = self._page.findAll(class_="theme-song")
            temped2 = []
            self._ed = []
            inc = 0
            index = 0
            for i in range(len(temped)):
                temped2.append(temped[i].text)
            if temped2[-1][0] != '#':
                return [temped2[-1]]
            if temped2[0][0] != '#':
                index = 1
            else:
                for i in range(1, len(temped2)):
                    if temped2[i][1].isdigit():
                        index += 1
                    else:
                        break
            for i in range(index, len(temped2)):
                if temped2[i][1].isdigit() and inc < int(temped2[i][1]):
                    inc = int(temped2[i][1])
                    self._ed.append(temped[i].text)
                else:
                    return self._ed
        return self._ed

    @property
    def watching(self):
        try:
            self._watching
        except AttributeError:
            key = "Watching:"
            if key not in self._page_stats.text:
                return None
            self._watching = int(locale.atoi(self._page_stats.find(text=key).next))
        return self._watching

    @property
    def completed(self):
        try:
            self._completed
        except AttributeError:
            key = "Completed:"
            if key not in self._page_stats.text:
                return None
            self._completed = int(locale.atoi(self._page_stats.find(text=key).next))
        return self._completed

    @property
    def onhold(self):
        try:
            self._onhold
        except AttributeError:
            key = "On-Hold:"
            if key not in self._page_stats.text:
                return None
            self._onhold = int(locale.atoi(self._page_stats.find(text=key).next))
        return self._onhold

    @property
    def dropped(self):
        try:
            self._dropped
        except AttributeError:
            key = "Dropped:"
            if key not in self._page_stats.text:
                return None
            self._dropped = int(locale.atoi(self._page_stats.find(text=key).next))
        return self._dropped

    @property
    def total(self):
        try:
            self._total
        except AttributeError:
            key = "Total:"
            if key not in self._page_stats.text:
                return None
            self._total = int(locale.atoi(self._page_stats.find(text=key).next))
        return self._total

    @property
    def ptw(self):
        try:
            self._ptw
        except AttributeError:
            key = "Plan to Watch:"
            if key not in self._page_stats.text:
                return None
            self._ptw = int(locale.atoi(self._page_stats.find(text=key).next))
        return self._ptw

    @property
    def scoredist(self):
        try:
            self._scoredist
        except AttributeError:
            key = "Score Stats"
            if key not in self._page_stats.text:
                return None
            scoredist = os.linesep.join(
                [s for s in self._page_stats.find('h2', text=key).next.next.next.text.splitlines() if s])
            tempscoredist = scoredist.split("\n")
            for i in range(len(tempscoredist)):
                tempscoredist[i] = tempscoredist[i].replace('\r', '').replace(u'\xa0', '')
            self._scoredist = []
            for i in range(0, len(tempscoredist), 2):
                self._scoredist.append([tempscoredist[i], tempscoredist[i + 1]])
        return self._scoredist

    @property
    def deviation(self):
        try:
            self._deviation
        except AttributeError:
            raw = self.scoredist
            vals = []
            freq = []
            for i in range(len(raw)):
                vals.append(int(raw[i][0]))
                temp = raw[i][1].replace("(", "sub")
                extract = re.search('sub(.*) votes', temp)
                freq.append(int(extract.group(1)))
            self._deviation = stats.std_(vals, freq)
        return self._deviation