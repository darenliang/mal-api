# Unofficial Python Mal API

Welcome! Here is an Unofficial MyAnimeList API in response to the MyAnimeList's API shutdown.

Hold on, this API is in early stages and is unstable.

Currently, the API does not feature any kind of rate limiting. Use the API in moderation and rate limit your queries (0.5 seconds is sufficient to my knowledge). This API uses cached webpage data to increase efficiency and save bandwidth. If you want to refresh your data, you must create a new object (a refresh option will most likely come in the future; no plans for dynamically updating info).

## Notice

I am in the process of rewriting the whole API, some functionality is currently missing. More features are to come.

## Usage

Import `mal_api.py` and install the required packages from `requirements.txt`

## API Documentation

To call the API, you need to create an object.

```python
from mal_api import Anime

anime = Anime(1) # Cowboy Bebop

print(anime.score) # prints 8.82
```

To refresh or reload an object, call the method "reload".
```python
from mal_api import Anime

anime = Anime(1) # Cowboy Bebop

print(anime.score) # prints 8.82
anime.reload()
print(anime.score) # prints 8.81
```

List of properties:
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

manga.mal_id
manga.title
manga.title_english
manga.title_japanese
manga.title_synonyms
manga.url
manga.image_url
manga.type
manga.status
manga.genres
manga.score
manga.scored_by
manga.rank
manga.popularity
manga.members
manga.favorites
manga.synopsis
manga.background
manga.favorites
manga.synopsis
manga.background
manga.volumes
manga.chapters
manga.published
manga.authors
manga.related_manga
```
