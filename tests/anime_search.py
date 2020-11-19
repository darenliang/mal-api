import unittest

from mal import AnimeSearch


class TestAnimeSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.anime_search = AnimeSearch("cowboy bebop")

    def test_anime_search(self):
        self.assertEqual(self.anime_search.results[0].mal_id, 1)
        self.assertEqual(
            self.anime_search.results[0].url,
            "https://myanimelist.net/anime/1/Cowboy_Bebop",
        )
        self.assertEqual(
            self.anime_search.results[0].image_url,
            "https://cdn.myanimelist.net/images/anime/4/19644.jpg",
        )
        self.assertEqual(self.anime_search.results[0].title, "Cowboy Bebop")
        self.assertEqual(
            self.anime_search.results[0].synopsis,
            "In the year 2071, humanity has colonized several of the planets and moons "
            "of the solar system leaving the now uninhabitable surface of planet Earth "
            "behind. The Inter Solar System Police attempts to ke...",
        )
        self.assertEqual(self.anime_search.results[0].type, "TV")
        self.assertEqual(self.anime_search.results[0].episodes, 26)
        self.assertIsInstance(self.anime_search.results[0].score, float)


if __name__ == "__main__":
    unittest.main()
