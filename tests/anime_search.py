import unittest

from mal import AnimeSearch


class TestAnimeSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.anime_search = AnimeSearch("cowboy bebop")

    def test_anime_search(self):
        result = self.anime_search.results[1]

        self.assertEqual(result.mal_id, 1)
        self.assertEqual(
            result.url,
            "https://myanimelist.net/anime/1/Cowboy_Bebop",
        )
        self.assertEqual(
            result.image_url,
            "https://cdn.myanimelist.net/images/anime/4/19644.jpg",
        )
        self.assertEqual(result.title, "Cowboy Bebop")
        self.assertEqual(
            result.synopsis,
            "In the year 2071, humanity has colonized several of the planets and moons "
            "of the solar system leaving the now uninhabitable surface of planet Earth "
            "behind. The Inter Solar System Police attempts to ke...",
        )
        self.assertEqual(result.type, "TV")
        self.assertEqual(result.episodes, 26)
        self.assertIsInstance(result.score, float)


if __name__ == "__main__":
    unittest.main()
