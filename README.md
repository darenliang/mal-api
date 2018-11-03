# mal-api

Comprehensive MyAnimeList WebScraper API

Welcome! Here is an Unofficial MyAnimeList API in response to the MyAnimeList's API shutdown.

## To install

All you need to do is import the mal-api.py file into any Python 3 project. Also make sure that you have beautifulsoup4 installed.

Example:
```python
import mal-api
print(mal-api.get_anime_score("Made in Abyss")) # 8.89
```

## API Documentation

```python
get_anime_url(str)
# given anime's name, returns MAL anime url
```
