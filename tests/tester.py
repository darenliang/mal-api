"""This test file contains tests for various apis"""
import time
from unittest import TestCase

from mal_api import Anime, Manga

anime = Anime(1)


class TestAnime(TestCase):

    def test_reload(self):
        time.sleep(5)
        anime.reload()
        self.assertIsInstance(anime, Anime)

    def test_get_mal_id(self):
        self.assertEqual(anime.mal_id, 1)

    def test_get_title(self):
        self.assertEqual(anime.title, "Cowboy Bebop")

    def test_get_title_english(self):
        self.assertEqual(anime.title_english, "Cowboy Bebop")

    def test_get_title_japanese(self):
        self.assertEqual(anime.title_japanese, "カウボーイビバップ")

    def test_get_title_synonyms(self):
        self.assertEqual(anime.title_synonyms, [])

    def test_get_url(self):
        self.assertEqual(anime.url, "https://myanimelist.net/anime/1/Cowboy_Bebop")

    def test_get_image_url(self):
        self.assertEqual(anime.image_url, "https://cdn.myanimelist.net/images/anime/4/19644.jpg")

    def test_get_type(self):
        self.assertEqual(anime.type, "TV")

    def test_get_episodes(self):
        self.assertEqual(anime.episodes, 26)

    def test_get_status(self):
        self.assertEqual(anime.status, "Finished Airing")

    def test_get_aired(self):
        self.assertEqual(anime.aired, "Apr 3, 1998 to Apr 24, 1999")

    def test_get_premiered(self):
        self.assertEqual(anime.premiered, "Spring 1998")

    def test_get_broadcast(self):
        self.assertEqual(anime.broadcast, "Saturdays at 01:00 (JST)")

    def test_get_producers(self):
        self.assertEqual(anime.producers, ["Bandai Visual"])

    def test_get_licensors(self):
        self.assertEqual(anime.licensors, ["Funimation", "Bandai Entertainment"])

    def test_get_studios(self):
        self.assertEqual(anime.studios, ["Sunrise"])

    def test_get_source(self):
        self.assertEqual(anime.source, "Original")

    def test_get_genres(self):
        self.assertEqual(anime.genres, ["Action", "Adventure", "Comedy", "Drama", "Sci-Fi", "Space"])

    def test_get_duration(self):
        self.assertEqual(anime.duration, "24 min. per ep.")

    def test_get_rating(self):
        self.assertEqual(anime.rating, "R - 17+ (violence & profanity)")

    def test_get_score(self):
        self.assertIsInstance(anime.score, float)

    def test_get_score_by(self):
        self.assertIsInstance(anime.scored_by, int)

    def test_get_rank(self):
        self.assertIsInstance(anime.rank, int)

    def test_get_popularity(self):
        self.assertIsInstance(anime.popularity, int)

    def test_get_members(self):
        self.assertIsInstance(anime.members, int)

    def test_get_favorites(self):
        self.assertIsInstance(anime.favorites, int)

    def test_get_synopsis(self):
        self.assertIsInstance(anime.synopsis, str)

    def test_get_background(self):
        self.assertIsInstance(anime.background, str)

    def test_get_related_anime(self):
        self.assertEqual(anime.related_anime, {'Adaptation': ['Cowboy Bebop', 'Shooting Star Bebop: Cowboy Bebop'],
                                               'Side story': ['Cowboy Bebop: Tengoku no Tobira',
                                                              'Cowboy Bebop: Ein no Natsuyasumi'],
                                               'Summary': ['Cowboy Bebop: Yose Atsume Blues']})

    def test_get_opening_themes(self):
        self.assertEqual(anime.opening_themes, ['"Tank!" by The Seatbelts (eps 1-25)'])

    def test_get_ending_themme(self):
        self.assertEqual(anime.ending_themes,
                         ['"The Real Folk Blues" by The Seatbelts feat. Mai Yamane (eps 1-12, 14-25)',
                          '"Space Lion" by The Seatbelts (ep 13)', '"Blue" by The Seatbelts feat. Mai Yamane (ep 26)'])


manga = Manga(1)


class TestManga(TestCase):

    def test_reload(self):
        time.sleep(5)
        anime.reload()
        self.assertIsInstance(manga, Manga)

    def test_get_mal_id(self):
        self.assertEqual(manga.mal_id, 1)

    def test_get_title(self):
        self.assertEqual(manga.title, "Monster")

    def test_get_title_english(self):
        self.assertEqual(manga.title_english, "Monster")

    def test_get_title_japanese(self):
        self.assertEqual(manga.title_japanese, "MONSTER")

    def test_get_title_synonyms(self):
        self.assertEqual(manga.title_synonyms, [])

    def test_get_url(self):
        self.assertEqual(manga.url, "https://myanimelist.net/manga/1/Monster")

    def test_get_image_url(self):
        self.assertEqual(manga.image_url, "https://cdn.myanimelist.net/images/manga/3/54525.jpg")

    def test_get_type(self):
        self.assertEqual(manga.type, "Manga")

    def test_get_status(self):
        self.assertEqual(manga.status, "Finished")

    def test_get_genres(self):
        self.assertEqual(manga.genres, ['Mystery', 'Drama', 'Psychological', 'Seinen'])

    def test_get_score(self):
        self.assertIsInstance(manga.score, float)

    def test_get_score_by(self):
        self.assertIsInstance(manga.scored_by, int)

    def test_get_rank(self):
        self.assertIsInstance(manga.rank, int)

    def test_get_popularity(self):
        self.assertIsInstance(manga.popularity, int)

    def test_get_members(self):
        self.assertIsInstance(manga.members, int)

    def test_get_favorites(self):
        self.assertIsInstance(manga.favorites, int)

    def test_get_synopsis(self):
        self.assertIsInstance(manga.synopsis, str)

    def test_get_background(self):
        self.assertIsInstance(manga.background, str)

    def test_get_volumes(self):
        self.assertEqual(manga.volumes, 18)

    def test_get_chapters(self):
        self.assertEqual(manga.chapters, 162)

    def test_get_published(self):
        self.assertEqual(manga.published, "Dec  5, 1994 to Dec  20, 2001")

    def test_get_authors(self):
        self.assertEqual(manga.authors, ['Urasawa, Naoki'])

    def test_get_related_anime(self):
        self.assertEqual(manga.related_manga, {'Side story': ['Mou Hitotsu no Monster: The Investigative Report'],
                                               'Adaptation': ['Monster']})
