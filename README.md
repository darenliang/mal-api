# Unofficial Python Mal API

Welcome! Here is an Unofficial MyAnimeList API in response to the MyAnimeList's API shutdown.

Hold on, this API is in early stages and is very unstable. Future updates may support more features and manga support.

This API has its issues. I will hopefully clean up the API to make it more easy to use.

## Future updates!

A new version of the mal-api is on its way. It will be much easier and faster to use. Stay tuned for updates.

## To install

All you need to do is import the mal-api.py file into any Python 3 project.

Make sure that your Python 3 distributions has access to these libraries.

```
numpy
# pip Installer: pip install numpy
beautifulsoup4
# pip Installer: pip install beautifulsoup4
requests
# pip Installer: pip install requests
```

Example:
```python
import mal_api

print(mal_api.get_anime_score("Made in Abyss"))
# prints 8.89
```

## API Documentation

Currently, there are 63 API functions implemented in mal-api.

To call an API, you need either the anime's name or the MAL base url of an anime.

```python
get_anime_url(str) > str
# returns MAL anime url

get_anime_name(str) > str
# returns anime name from MAL anime url

get_anime_type(str) > str
# returns anime type (TV, Movie, OVA, etc)

get_anime_episodes(str) > int
# returns number of episodes

get_anime_status(str) > str
# returns current status of anime (Currently Airing, Finished Airing, etc)

get_anime_aired(str) > str
# returns time interval in which anime was aired

get_anime_premiered(str) > str
# returns season in which anime was premiered

get_anime_broadcast(str) > str
# returns anime broadcast times

get_anime_producers(str) > list
# returns anime producers

get_anime_licensors(str) > list
# returns anime licensors

get_anime_studios(str) > str
# returns anime studios

get_anime_source(str) > str
# returns anime adaptation source

get_anime_genres(str) > list
# returns anime genres

get_anime_duration(str) > str
# returns duration of an episode

get_anime_rating(str) > str
# returns anime age rating

get_anime_synopsis(str) > str
# returns anime synopsis

get_anime_score(str) > float
# returns anime score

get_anime_rank(str) > int
# returns anime score rank

get_anime_popularity(str) > int
# returns anime popularity rank

get_anime_members(str) > int
# returns number of MAL members

get_anime_favorites(str) > int
# returns number of MAL favorites

get_anime_adaptation(str) > list
# returns adaptations of the anime

get_anime_sidestory(str) > list
# returns sidestories of the anime

get_anime_alternative(str) > list
# returns alternative settings of the anime

get_anime_sequel(str) > list
# returns sequels of the anime

get_anime_prequel(str) > list
# returns prequels of the anime

get_anime_summary(str) > list
# returns summaries/compilations of the anime

get_anime_other(str) > list
# returns other forms of media of the anime

get_anime_spinoff(str) > list
# returns spinoffs of the anime

get_anime_character(str) > list
# returns character snapshots of the anime

get_anime_version(str) > list
# returns alternative versions of the anime

get_anime_maincast(str) > list(list)
# returns the maincast of the anime
# Format: ['Name', 'Main/Supporting', 'Voice Actor Name', 'Country']

get_anime_staff(str) > list(list)
# returns staff of the anime
# Format: ['Name', 'Role']

get_anime_op(str) > list
# returns anime openings

get_anime_ed(str) > list
# returns anime endings

get_anime_watching(str) > int
# returns number of MAL users watching

get_anime_completed(str) > int
# returns number of MAL users completed

get_anime_onhold(str) > int
# returns number of MAL users onhold

get_anime_dropped(str) > int
# returns number of MAL users dropped

get_anime_total(str) > int
# returns number of MAL users total

get_anime_ptw(str) > int
# returns number of MAL users plan to watch

get_anime_scoredist(str) > list(list)
# returns score distribution
# Format: [Score, 'Frequency/Percentage']

get_anime_deviation(str) > float
# returns anime score deviation

get_anime_trending() > list
# returns list of trending anime (only 20 anime)

get_topanime(n) > str
# returns anime of the same top rank

get_topairing(n) > str
# returns top airing anime of the same rank

get_topupcoming(n) > str
# returns top upcoming anime of the same rank

get_toptv(n) > str
# returns top tv anime of the same rank

get_topmovie(n) > str
# returns top movie anime of the same rank

get_topova(n) > str
# returns top OVA anime of the same rank

get_topspecial(n) > str
# returns top special anime of the same rank

get_mostpopular(n) > str
# returns most popular anime of the same rank

get_mostfavorite(n) > str
# returns most favorite anime of the same rank

get_toplist_name(l, s, f) > list
# returns list of names of top anime in a specified category
# Format: ('url suffix', start, finish)

get_toplist_url(l, s, f) > list
# returns list of urls of top anime in a specified category
# Format: ('url suffix', start, finish)

get_key_name(l, s, f) > list
# returns list of names of anime in a specified pseudo-static category
# Format: ('url suffix', start, finish)

get_key_url(l, s, f) > list
# returns list of urls of anime in a specified pseudo-static category
# Format: ('url suffix', start, finish)

get_custom_name(l, s, f) > list
# returns list of names of anime in a custom search
# Format: ('complete url suffix', start, finish)

get_custom_url(l, s, f) > list
# returns list of urls of anime in a custom search
# Format: ('complete url suffix', start, finish)

get_season_name(l) > list
# returns list of names of anime in a season
# Format: 'season year'
# Example: 'Spring 2017'

get_season_url(l) > list
# returns list of urls of anime in a season
# Format: 'season year'

get_genre_name(l, s, f) > list
# returns list of names of anime of specified genre
# Format: ('category', start, finish)

get_genre_url(l, s, f) > list
# returns list of urls of anime specified genre
# Format: ('category', start, finish)
```

Formats for genres

Valid Categories:
- Action
- Adventure
- Cars
- Comedy
- Dementia
- Demons
- Drama
- Ecchi
- Fantasy
- Game
- Harem
- Hentai
- Historical
- Horror
- Josei
- Kids
- Magic
- Martial Arts
- Mecha
- Military
- Music
- Mystery
- Parody
- Police
- Psychological
- Romance
- Samurai
- School
- Sci-Fi
- Seinen
- Shoujo
- Shoujo Ai
- Shounen
- Shounen Ai
- Slice of Life
- Space
- Sports
- Super Power
- Supernatural
- Thriller
- Vampire
- Yaoi
- Yuri

## Using the discord-anime-bot

Using the discord-anime-bot is simple:

Prefixes are ? and !

Call functions listed above, but in this format:
- !get_anime_score str
- Use quotations if you need a mutliple parameters and separate with spaces

Some new functions you can use:
- !get_anime_info
- !get_anime_polarization
- !get_random_anime
