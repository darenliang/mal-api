# Unofficial Python Mal API

Welcome! Here is an Unofficial MyAnimeList API in response to the MyAnimeList's API shutdown.

Hold on, this API is in early stages and is very unstable. Future updates may support more features and manga support.

Currently, the API does not feature any kind of sophisticated rate limiting. Use the API in moderation and rate limit your queries (0.5 seconds is sufficient to my knowledge). This API uses cached webpage data to increase efficiency and save bandwidth. If you want to refresh your data, you must create a new object (a refresh option will most likely come in the future; no plans for dynamically updating info).

## Usage

Import `mal_api.py` and install the required packages from `requirements.txt`

## API Documentation

To call the API, you need the anime's id number from MyAnimeList.

```python
from mal_api import Anime

anime = Anime(1) # Cowboy Bebop

print(anime.score) # prints 8.82
```

List of properties:
```
Anime.name
Anime.image
Anime.type
Anime.episodes
Anime.status
Anime.aired
Anime.premiered
Anime.broadcast
Anime.producers
Anime.licensors
Anime.studios
Anime.source
Anime.genres
Anime.duration
Anime.rating
Anime.score
Anime.rank
Anime.popularity
Anime.members
Anime.favorites
Anime.synopsis
Anime.adaptation
Anime.sidestory
Anime.alternative
Anime.sequel
Anime.prequel
Anime.summary
Anime.other
Anime.spinoff
Anime.character
Anime.version
Anime.maincast
Anime.staff
Anime.op
Anime.ed
Anime.watching
Anime.completed
Anime.onhold
Anime.dropped
Anime.total
Anime.ptw
Anime.scoredist
Anime.deviation
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
