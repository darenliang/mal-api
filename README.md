# mal-api

Comprehensive MyAnimeList WebScraper API

Welcome! Here is an Unofficial MyAnimeList API in response to the MyAnimeList's API shutdown.

Hold on, this API is in early stages. Future updates may support more features and manga support.

## To install

All you need to do is import the mal-api.py file into any Python 3 project. Also make sure that you have beautifulsoup4 installed.

Example:
```python
import mal-api

print(mal-api.get_anime_score("Made in Abyss")) # 8.89
```

## API Documentation

To call an API, you need either the anime's name or the MAL base url of an anime.

```python
get_anime_url(str) -> str
# returns MAL anime url

get_anime_type(str) -> str
# returns anime type (TV, Movie, OVA, etc)

get_anime_episodes(str) -> int
# returns number of episodes

get_anime_status(str) -> str
# returns current status of anime (Currently Airing, Finished Airing, etc)

get_anime_aired(str) -> str
# returns time interval in which anime was aired

get_anime_premiered(str) -> str
# returns season in which anime was premiered

get_anime_broadcast(str) -> str
# returns anime broadcast times

get_anime_producers(str) -> list
# returns anime producers

get_anime_licensors(str) -> list
# returns anime licensors

get_anime_studios(str) -> str
# returns anime studios

get_anime_source(str) -> str
# returns anime adaptation source

get_anime_genres(str) -> list
# returns anime genres

get_anime_duration(str) -> str
# returns duration of an episode

get_anime_rating(str) -> str
# returns anime age rating

get_anime_score(str) -> float
# returns anime score

get_anime_rank(str) -> int
# returns anime score rank

get_anime_popularity(str) -> int
# returns anime popularity rank

get_anime_members(str) -> int
# returns number of MAL members

get_anime_favorites(str) -> int
# returns number of MAL favorites

get_anime_adaptation(str) -> list
# returns adaptations of the anime

get_anime_sidestory(str) -> list
# returns sidestories of the anime

get_anime_alternative(str) -> list
# returns alternative settings of the anime

get_anime_sequel(str) -> list
# returns sequels of the anime

get_anime_prequel(str) -> list
# returns prequels of the anime

get_anime_summary(str) -> list
# returns summaries/compilations of the anime

get_anime_other(str) -> list
# returns other forms of media of the anime

get_anime_spinoff(str) -> list
# returns spinoffs of the anime

get_anime_character(str) -> list
# returns character snapshots of the anime

get_anime_version(str) -> list
# returns alternative versions of the anime

get_anime_maincast(str) -> list(list)
# returns the maincast of the anime
# Format: ['Name', 'Main/Supporting', 'Voice Actor Name', 'Country']

get_anime_staff(str) -> list(list)
# returns staff of the anime
# Format: ['Name', 'Role']

get_anime_op(str) -> list
# returns anime openings

get_anime_ed(str) -> list
# returns anime endings

get_anime_watching(str) -> int
# returns number of MAL users watching

get_anime_completed(str) -> int
# returns number of MAL users completed

get_anime_onhold(str) -> int
# returns number of MAL users onhold

get_anime_dropped(str) -> int
# returns number of MAL users dropped

get_anime_total(str) -> int
# returns number of MAL users total

get_anime_ptw(str) -> int
# returns number of MAL users plan to watch

get_anime_scoredist(str) -> list(list)
# returns score distribution
# Format: [Score, 'Frequency/Percentage']

get_anime_deviation(str) -> float
# returns anime score deviation
```
