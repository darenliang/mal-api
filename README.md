# Python MAL API

[![pypi Version](https://img.shields.io/pypi/v/mal-api.svg?color=informational)](https://pypi.org/project/mal-api/)

Here is an unofficial MyAnimeList API for Python 3 in response to the MyAnimeList's API shutdown.

Currently, the API does not feature any kind of rate limiting. Use the API in moderation and rate limit your queries (0.5 seconds is sufficient to my knowledge). This API uses cached webpage data to increase efficiency and save bandwidth. If you want to refresh your data, you must create a new object (a refresh option will most likely come in the future; no plans for dynamically updating info).

I am in the process of rewriting the whole API, some functionality is currently missing. More features are to come.

If there are any features that you wish to be supported, please raise an issue. Any feedback is also appreciated.

## Installation and Usage

To install the library: `pip install mal-api`

To import the library: `from mal import *`

## API Documentation

To call the API, you need to create an object.

```python
from mal import Anime

anime = Anime(1) # Cowboy Bebop

print(anime.score) # prints 8.82

anime.reload() # reload object

print(anime.score) # prints 8.81
```

List of properties currently supported:
```
Anime

Anime.mal_id
Anime.title
Anime.title_english
Anime.title_japanese
Anime.title_synonyms
Anime.url
Anime.image_url
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
Anime.scored_by
Anime.rank
Anime.popularity
Anime.members
Anime.favorites
Anime.synopsis
Anime.background
Anime.related_anime
Anime.opening_themes
Anime.ending_themes
```
```
Manga

Manga.mal_id
Manga.title
Manga.title_english
Manga.title_japanese
Manga.title_synonyms
Manga.url
Manga.image_url
Manga.type
Manga.status
Manga.genres
Manga.score
Manga.scored_by
Manga.rank
Manga.popularity
Manga.members
Manga.favorites
Manga.synopsis
Manga.background
Manga.favorites
Manga.synopsis
Manga.background
Manga.volumes
Manga.chapters
Manga.published
Manga.authors
Manga.related_manga
```
