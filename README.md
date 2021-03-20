# Python MAL API

[![pypi Version](https://img.shields.io/pypi/v/mal-api.svg?color=informational)](https://pypi.org/project/mal-api/)

An unofficial MyAnimeList API for Python 3.

Currently, the API does not feature any kind of rate limiting. Use the API in moderation
and rate limit your queries (0.5 seconds is sufficient to my knowledge). This API uses
cached webpage data to increase efficiency and save bandwidth. If you want to refresh
your data, you must manually refresh the object.

The API is currently incomplete. More features are to come.

If there are any features that you wish to be supported, please raise an issue. Any
feedback is also appreciated.

## API Documentation

[ReadTheDocs Documentation](https://mal-api.readthedocs.io)

## Installation and Usage

To install the library:

```
pip install -U mal-api
```

To import the library:

```python
from mal import *
```

## Example

To call the API, you need to create an object.

#### ID Query Example

```python
from mal import Anime

anime = Anime(1)  # Cowboy Bebop

print(anime.score)  # prints 8.82

anime.reload()  # reload object

print(anime.score)  # prints 8.81
```

#### Search Query Example

```python
from mal import AnimeSearch

search = AnimeSearch("cowboy bebop")  # Search for "cowboy bebop"

print(search.results[0].title)  # Get title of first result
```

## Configuration

To configure timeout (default timeout is 5 seconds):

```python
from mal import Anime

from mal import config

config.TIMEOUT = 1  # Import level config

anime = Anime(1, timeout=1)  # Object level config
```
