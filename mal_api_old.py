import locale
import os
import re

import requests
from bs4 import BeautifulSoup

import stats

genres_suffix = {
    "Action": "genre/1/Action",
    "Adventure": "genre/2/Adventure",
    "Cars": "genre/3/Cars",
    "Comedy": "genre/4/Comedy",
    "Dementia": "genre/5/Dementia",
    "Demons": "genre/6/Demons",
    "Mystery": "genre/7/Mystery",
    "Drama": "genre/8/Drama",
    "Ecchi": "genre/9/Ecchi",
    "Fantasy": "genre/10/Fantasy",
    "Game": "genre/11/Game",
    "Hentai": "genre/12/Hentai",
    "Historical": "genre/13/Historical",
    "Horror": "genre/14/Horror",
    "Kids": "genre/15/Kids",
    "Magic": "genre/16/Magic",
    "Martial Arts": "genre/17/Martial_Arts",
    "Mecha": "genre/18/Mecha",
    "Music": "genre/19/Music",
    "Parody": "genre/20/Parody",
    "Samurai": "genre/21/Samurai",
    "Romance": "genre/22/Romance",
    "School": "genre/23/School",
    "Sci-Fi": "genre/24/Sci-Fi",
    "Shoujo": "genre/25/Shoujo",
    "Shoujo Ai": "genre/26/Shoujo_Ai",
    "Shounen": "genre/27/Shounen",
    "Shounen Ai": "genre/28/Shounen_Ai",
    "Space": "genre/29/Space",
    "Sports": "genre/30/Sports",
    "Super Power": "genre/31/Super_Power",
    "Vampire": "genre/32/Vampire",
    "Yaoi": "genre/33/Yaoi",
    "Yuri": "genre/34/Yuri",
    "Harem": "genre/35/Harem",
    "Slice of Life": "genre/36/Slice_of_Life",
    "Supernatural": "genre/37/Supernatural",
    "Military": "genre/38/Military",
    "Police": "genre/39/Police",
    "Psychological": "genre/40/Psychological",
    "Thriller": "genre/41/Thriller",
    "Seinen": "genre/42/Seinen",
    "Josei": "genre/43/Josei",
}

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
regex = re.compile(
    r'^(?:http|ftp)s?://'
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r'(?::\d+)?'
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def parse_url(s):
    page_response = requests.get(s, timeout=5)
    return BeautifulSoup(page_response.content, "html.parser")


def get_anime_url(s):
    page_link = 'https://myanimelist.net/search/all?q=' + s
    page_content = parse_url(page_link)
    return page_content.find(id="anime").findNext('a').get('href')


def get_anime_image(s):
    page_content = url_select_parse(s)
    image = page_content.find('img', class_="ac")['src']
    return image


def get_anime_name(s):
    page_link = s
    page_content = parse_url(page_link)
    return page_content.find("span", itemprop="name").text


def url_select_parse(s):
    if re.match(regex, s) is not None:
        return parse_url(s)
    else:
        return parse_url(get_anime_url(s))


def url_select(s):
    if re.match(regex, s) is not None:
        return s
    else:
        return get_anime_url(s)


def get_anime_type(s):
    key = "Type:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return page_content.find(text=key).findNext('a').text


def get_anime_episodes(s):
    key = "Episodes:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return str(page_content.find(text=key).next)


def get_anime_status(s):
    key = "Status:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    temp = str(page_content.find('span', text=key).parent)
    no_whitespace = ''
    for i in temp:
        if i != '\n':
            no_whitespace += i
    status = re.search('</span>  (.*)  </div>', no_whitespace)
    return status.group(1)


def get_anime_aired(s):
    key = "Aired:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return page_content.find(text=key).next.strip(" \n")


def get_anime_premiered(s):
    key = "Premiered:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return page_content.find(text=key).findNext('a').text


def get_anime_broadcast(s):
    key = "Broadcast:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return page_content.find(text=key).next.strip(" \n")


def get_anime_producers(s):
    key = "Producers:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    producers = page_content.find(text=key).parent.parent.findAll('a')
    for i in range(len(producers)):
        producers[i] = producers[i].text
    return producers


def get_anime_licensors(s):
    key = "Licensors:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    licensors = page_content.find(text=key).parent.parent.findAll('a')
    for i in range(len(licensors)):
        licensors[i] = licensors[i].text
    return licensors


def get_anime_studios(s):
    key = "Studios:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return page_content.find(text=key).findNext('a').text


def get_anime_source(s):
    key = "Source:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return page_content.find(text=key).next.strip(" \n")


def get_anime_genres(s):
    key = "Genres:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    genres = page_content.find(text=key).parent.parent.findAll('a')
    for i in range(len(genres)):
        genres[i] = genres[i].text
    return genres


def get_anime_duration(s):
    key = "Duration:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return page_content.find(text=key).next.strip(" \n")


def get_anime_rating(s):
    key = "Rating:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return page_content.find(text=key).next.strip(" \n")


def get_anime_score(s):
    key = "Score:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return str(page_content.find(text=key).next.next.text)


def get_anime_rank(s):
    key = "Ranked:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return str((page_content.find(text=key).next.strip(" \n"))[1:])


def get_anime_popularity(s):
    key = "Popularity:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return str((page_content.find(text=key).next.strip(" \n"))[1:])


def get_anime_members(s):
    key = "Members:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return str(locale.atoi(page_content.find(text=key).next.strip(" \n")))


def get_anime_favorites(s):
    key = "Favorites:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return str(locale.atoi(page_content.find(text=key).next.strip(" \n")))


def get_anime_synopsis(s):
    key = "Synopsis"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    return page_content.find("span", itemprop="description").text


def get_anime_adaptation(s):
    key = "Adaptation:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    adaptation = page_content.find(text=key).next.findAll('a')
    for i in range(len(adaptation)):
        adaptation[i] = adaptation[i].text
    return adaptation


def get_anime_sidestory(s):
    key = "Side story:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    sidestory = page_content.find(text=key).next.findAll('a')
    for i in range(len(sidestory)):
        sidestory[i] = sidestory[i].text
    return sidestory


def get_anime_alternative(s):
    key = "Alternative setting:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    alternative = page_content.find(text=key).next.findAll('a')
    for i in range(len(alternative)):
        alternative[i] = alternative[i].text
    return alternative


def get_anime_sequel(s):
    key = "Sequel:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    sequel = page_content.find(text=key).next.findAll('a')
    for i in range(len(sequel)):
        sequel[i] = sequel[i].text
    return sequel


def get_anime_summary(s):
    key = "Summary:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    summary = page_content.find(text=key).next.findAll('a')
    for i in range(len(summary)):
        summary[i] = summary[i].text
    return summary


def get_anime_other(s):
    key = "Other:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    other = page_content.find(text=key).next.findAll('a')
    for i in range(len(other)):
        other[i] = other[i].text
    return other


def get_anime_prequel(s):
    key = "Prequel:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    prequel = page_content.find(text=key).next.findAll('a')
    for i in range(len(prequel)):
        prequel[i] = prequel[i].text
    return prequel


def get_anime_spinoff(s):
    key = "Spin-off:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    spinoff = page_content.find(text=key).next.findAll('a')
    for i in range(len(spinoff)):
        spinoff[i] = spinoff[i].text
    return spinoff


def get_anime_character(s):
    key = "Character:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    character = page_content.find(text=key).next.findAll('a')
    for i in range(len(character)):
        character[i] = character[i].text
    return character


def get_anime_version(s):
    key = "Alternative version:"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    version = page_content.find(text=key).next.findAll('a')
    for i in range(len(version)):
        version[i] = version[i].text
    return version


def get_anime_maincast(s):
    key = "Characters & Voice Actors"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    cast = os.linesep.join([s for s in page_content.find(text=key).next.text.splitlines() if s])
    tempcast = cast.split("\n")
    for i in range(len(tempcast)):
        tempcast[i] = tempcast[i].replace('\r', '')
    listcast = []
    for i in range(0, len(tempcast), 4):
        listcast.append([tempcast[i], tempcast[i + 1], tempcast[i + 2], tempcast[i + 3]])
    return listcast


def get_anime_staff(s):
    key = "More staff"
    page_content = url_select_parse(s)
    if key not in page_content.text:
        return None
    staff = os.linesep.join(
        [s for s in page_content.find(text=key, class_="floatRightHeader").next.next.next.next.next.text.splitlines() if
         s])
    tempstaff = staff.split("\n")
    for i in range(len(tempstaff)):
        tempstaff[i] = tempstaff[i].replace('\r', '')
    liststaff = []
    for i in range(0, len(tempstaff), 2):
        liststaff.append([tempstaff[i], tempstaff[i + 1]])
    return liststaff


def get_anime_op(s):
    key = "No opening themes have been added to this title."
    page_content = url_select_parse(s)
    if key in page_content.text:
        return None
    tempop = page_content.findAll(class_="theme-song")
    tempop2 = []
    op = []
    inc = 0
    for i in range(len(tempop)):
        tempop2.append(tempop[i].text)
    if tempop2[i][0] != '#':
        return [tempop2[0]]
    for i in range(len(tempop2)):
        if inc < int(tempop2[i][1]):
            inc = int(tempop2[i][1])
            op.append(tempop[i].text)
        else:
            return op
    return op


def get_anime_ed(s):
    key = "No ending themes have been added to this title."
    page_content = url_select_parse(s)
    if key in page_content.text:
        return None
    temped = page_content.findAll(class_="theme-song")
    temped2 = []
    ed = []
    inc = 0
    for i in range(len(temped)):
        temped2.append(temped[i].text)
    if temped2[0][0] != '#' and temped2[1][0] != '#':
        return [temped2[1]]
    for i in range(len(temped2)):
        if inc < int(temped2[i][1]):
            inc = int(temped2[i][1])
        else:
            ed.append(temped[i].text)
    return ed


def get_anime_watching(s):
    key = "Watching:"
    page_content = parse_url(url_select(s) + '/stats')
    if key not in page_content.text:
        return None
    return int(locale.atoi(page_content.find(text=key).next))


def get_anime_completed(s):
    key = "Completed:"
    page_content = parse_url(url_select(s) + '/stats')
    if key not in page_content.text:
        return None
    return int(locale.atoi(page_content.find(text=key).next))


def get_anime_onhold(s):
    key = "On-Hold:"
    page_content = parse_url(url_select(s) + '/stats')
    if key not in page_content.text:
        return None
    return int(locale.atoi(page_content.find(text=key).next))


def get_anime_dropped(s):
    key = "Dropped:"
    page_content = parse_url(url_select(s) + '/stats')
    if key not in page_content.text:
        return None
    return int(locale.atoi(page_content.find(text=key).next))


def get_anime_total(s):
    key = "Total:"
    page_content = parse_url(url_select(s) + '/stats')
    if key not in page_content.text:
        return None
    return int(locale.atoi(page_content.find(text=key).next))


def get_anime_ptw(s):
    key = "Plan to Watch:"
    page_content = parse_url(url_select(s) + '/stats')
    if key not in page_content.text:
        return None
    return int(locale.atoi(page_content.find(text=key).next))


def get_anime_scoredist(s):
    key = "Score Stats"
    page_content = parse_url(url_select(s) + '/stats')
    if key not in page_content.text:
        return None
    scoredist = os.linesep.join([s for s in page_content.find('h2', text=key).next.next.next.text.splitlines() if s])
    tempscoredist = scoredist.split("\n")
    for i in range(len(tempscoredist)):
        tempscoredist[i] = tempscoredist[i].replace('\r', '').replace(u'\xa0', '')
    scoredistlist = []
    for i in range(0, len(tempscoredist), 2):
        scoredistlist.append([tempscoredist[i], tempscoredist[i + 1]])
    return scoredistlist


def get_anime_deviation(s):
    raw = get_anime_scoredist(s)
    vals = []
    freq = []
    for i in range(len(raw)):
        vals.append(int(raw[i][0]))
        temp = raw[i][1].replace("(", "sub")
        extract = re.search('sub(.*) votes', temp)
        freq.append(int(extract.group(1)))
    return stats.std_(vals, freq)


def get_topanime(n):
    page_content = parse_url("https://myanimelist.net/topanime.php?limit=" + str(n - 1))
    return page_content.find("a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"}).text


def get_topairing(n):
    page_content = parse_url("https://myanimelist.net/topanime.php?type=airing&limit=" + str(n - 1))
    return page_content.find("a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"}).text


def get_topupcoming(n):
    page_content = parse_url("https://myanimelist.net/topanime.php?type=upcoming&limit=" + str(n - 1))
    return page_content.find("a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"}).text


def get_toptv(n):
    page_content = parse_url("https://myanimelist.net/topanime.php?type=tv&limit=" + str(n - 1))
    return page_content.find("a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"}).text


def get_topmovie(n):
    page_content = parse_url("https://myanimelist.net/topanime.php?type=movie&limit=" + str(n - 1))
    return page_content.find("a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"}).text


def get_topova(n):
    page_content = parse_url("https://myanimelist.net/topanime.php?type=ova&limit=" + str(n - 1))
    return page_content.find("a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"}).text


def get_topspecial(n):
    page_content = parse_url("https://myanimelist.net/topanime.php?type=special&limit=" + str(n - 1))
    return page_content.find("a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"}).text


def get_mostpopular(n):
    page_content = parse_url("https://myanimelist.net/topanime.php?type=bypopularity&limit=" + str(n - 1))
    return page_content.find("a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"}).text


def get_mostfavorite(n):
    page_content = parse_url("https://myanimelist.net/topanime.php?type=favorite&limit=" + str(n - 1))
    return page_content.find("a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"}).text


def get_toplist_name(l, s, f):
    if '?' in l:
        c = '&'
    else:
        c = '?'
    names = []
    while True:
        page_content = parse_url("https://myanimelist.net/" + l + c + "limit=" + str(s - 1))
        ranks = page_content.findAll("a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"})
        for i in range(50):
            names.append(ranks[i].text)
            s += 1
            if s > f - 1:
                return names


def get_toplist_url(l, s, f):
    if '?' in l:
        c = '&'
    else:
        c = '?'
    url = []
    while True:
        page_content = parse_url("https://myanimelist.net/" + l + c + "limit=" + str(s - 1))
        ranks = page_content.findAll("a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"})
        for i in range(50):
            url.append(ranks[i]['href'])
            s += 1
            if s > f - 1:
                return url


def get_genre_name(l, s, f):
    if l in genres_suffix:
        l = genres_suffix.get(l)
    else:
        return None
    sp = (s // 100) + 1
    ind = (s % 100) - 1
    names = []
    while True:
        page_content = parse_url('https://myanimelist.net/anime/' + l + '?page=' + str(sp))
        ranks = page_content.findAll("a", {"class": "link-title"})
        for i in range(ind, 100):
            names.append(ranks[i].text)
            s += 1
            if s > f - 1:
                return names
        sp += 1


def get_genre_url(l, s, f):
    if l in genres_suffix:
        l = genres_suffix.get(l)
    else:
        return None
    sp = (s // 100) + 1
    ind = (s % 100) - 1
    names = []
    while True:
        page_content = parse_url('https://myanimelist.net/anime/' + l + '?page=' + str(sp))
        ranks = page_content.findAll("a", {"class": "link-title"})
        for i in range(ind, 100):
            names.append(ranks[i]['href'])
            s += 1
            if s > f - 1:
                return names
        sp += 1


def get_key_name(l, s, f):
    sp = (s // 100) + 1
    ind = (s % 100) - 1
    names = []
    while True:
        page_content = parse_url('https://myanimelist.net/' + l + '?page=' + str(sp))
        ranks = page_content.findAll("a", {"class": "link-title"})
        for i in range(ind, 100):
            names.append(ranks[i].text)
            s += 1
            if s > f - 1:
                return names
        sp += 1


def get_key_url(l, s, f):
    sp = (s // 100) + 1
    ind = (s % 100) - 1
    urls = []
    while True:
        page_content = parse_url('https://myanimelist.net/' + l + '?page=' + str(sp))
        ranks = page_content.findAll("a", {"class": "link-title"})
        for i in range(ind, 100):
            urls.append(ranks[i]['href'])
            s += 1
            if s > f - 1:
                return urls
        sp += 1


def get_custom_name(l, s, f):
    while True:
        page_content = parse_url("https://myanimelist.net/" + l + "&show=" + str(s - 1))
        ranks = page_content.findAll("a", {"class": "hoverinfo_trigger fw-b fl-l"})
        names = []
        for i in range(50):
            names.append(ranks[i].text)
            s += 1
            if s > f - 1:
                return names


def get_custom_url(l, s, f):
    while True:
        page_content = parse_url("https://myanimelist.net/" + l + "&show=" + str(s - 1))
        ranks = page_content.findAll("a", {"class": "hoverinfo_trigger fw-b fl-l"})
        urls = []
        for i in range(50):
            urls.append(ranks[i]['href'])
            s += 1
            if s > f - 1:
                return urls


def get_season_name(l):
    l = l.split()
    year = l[1]
    season = l[0].lower()
    names = []
    page_content = parse_url('https://myanimelist.net/anime/season/' + year + '/' + season)
    ranks = page_content.findAll("a", {"class": "link-title"})
    for i in range(len(ranks)):
        names.append(ranks[i].text)
    return names


def get_season_url(l):
    l = l.split()
    year = l[1]
    season = l[0].lower()
    urls = []
    page_content = parse_url('https://myanimelist.net/anime/season/' + year + '/' + season)
    ranks = page_content.findAll("a", {"class": "link-title"})
    for i in range(len(ranks)):
        urls.append(ranks[i]['href'])
    return urls


def get_trending_anime():
    page_content = parse_url('https://myanimelist.net/')
    data = page_content.findAll("span", class_="title")
    for i in range(20):
        data[i] = data[i].text
    return data
