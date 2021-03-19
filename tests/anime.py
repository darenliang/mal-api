import unittest

from mal import Anime


class TestAnime(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.anime = Anime(1)

    def test_anime(self):
        self.assertEqual(self.anime.mal_id, 1)
        self.assertEqual(self.anime.title, "Cowboy Bebop")
        self.assertEqual(self.anime.title_english, "Cowboy Bebop")
        self.assertEqual(self.anime.title_japanese, "カウボーイビバップ")
        self.assertEqual(self.anime.title_synonyms, [])
        self.assertEqual(self.anime.url, "https://myanimelist.net/anime/1/Cowboy_Bebop")
        self.assertEqual(
            self.anime.image_url, "https://cdn.myanimelist.net/images/anime/4/19644.jpg"
        )
        self.assertEqual(self.anime.type, "TV")
        self.assertEqual(self.anime.episodes, 26)
        self.assertEqual(self.anime.status, "Finished Airing")
        self.assertEqual(self.anime.aired, "Apr 3, 1998 to Apr 24, 1999")
        self.assertEqual(self.anime.premiered, "Spring 1998")
        self.assertEqual(self.anime.broadcast, "Saturdays at 01:00 (JST)")
        self.assertEqual(self.anime.producers, ["Bandai Visual"])
        self.assertEqual(self.anime.licensors, ["Funimation", "Bandai Entertainment"])
        self.assertEqual(self.anime.studios, ["Sunrise"])
        self.assertEqual(self.anime.source, "Original")
        self.assertEqual(
            self.anime.genres,
            ["Action", "Adventure", "Comedy", "Drama", "Sci-Fi", "Space"],
        )
        self.assertEqual(self.anime.duration, "24 min. per ep.")
        self.assertEqual(self.anime.rating, "R - 17+ (violence & profanity)")
        self.assertIsInstance(self.anime.score, float)
        self.assertIsInstance(self.anime.scored_by, int)
        self.assertIsInstance(self.anime.rank, int)
        self.assertIsInstance(self.anime.popularity, int)
        self.assertIsInstance(self.anime.members, int)
        self.assertIsInstance(self.anime.favorites, int)
        self.assertEqual(
            self.anime.synopsis,
            "In the year 2071, humanity has colonized several of the planets and moons "
            "of the solar system leaving the now uninhabitable surface of planet Earth "
            "behind. The Inter Solar System Police attempts to keep peace in the "
            'galaxy, aided in part by outlaw bounty hunters, referred to as "Cowboys." '
            "The ragtag team aboard the spaceship Bebop are two such individuals.  "
            "Mellow and carefree Spike Spiegel is balanced by his boisterous, "
            "pragmatic partner Jet Black as the pair makes a living chasing bounties "
            "and collecting rewards. Thrown off course by the addition of new members "
            "that they meet in their travels—Ein, a genetically engineered, highly "
            "intelligent Welsh Corgi; femme fatale Faye Valentine, an enigmatic "
            "trickster with memory loss; and the strange computer whiz kid Edward "
            "Wong—the crew embarks on thrilling adventures that unravel each member's "
            "dark and mysterious past little by little.  Well-balanced with high "
            "density action and light-hearted comedy, Cowboy Bebop is a space Western "
            "classic and an homage to the smooth and improvised music it is named "
            "after.  [Written by MAL Rewrite]",
        )
        self.assertEqual(
            self.anime.background,
            "When Cowboy Bebop first aired in spring of 1998 on TV Tokyo, only "
            "episodes 2, 3, 7-15, and 18 were broadcast, it was concluded with a recap "
            "special known as Yose Atsume Blues. This was due to anime censorship "
            "having increased following the big controversies over Evangelion, as a "
            "result most of the series was pulled from the air due to violent content. "
            "Satellite channel WOWOW picked up the series in the fall of that year and "
            "aired it in its entirety uncensored. Cowboy Bebop was not a ratings hit "
            "in Japan, but sold over 19,000 DVD units in the initial release run, and "
            "81,000 overall. Protagonist Spike Spiegel won Best Male Character, and "
            "Megumi Hayashibara won Best Voice Actor for her role as Faye Valentine in "
            "the 1999 and 2000 Anime Grand Prix, respectively.  Cowboy Bebop's biggest "
            "influence has been in the United States, where it premiered on Adult Swim "
            "in 2001 with many reruns since. The show's heavy Western influence struck "
            'a chord with American viewers, where it became a "gateway drug" to '
            "anime aimed at adult audiences.",
        )
        self.assertEqual(
            self.anime.related_anime,
            {
                "Adaptation": [
                    "Cowboy Bebop",
                    "Shooting Star Bebop: Cowboy Bebop",
                ],
                "Side story": [
                    "Cowboy Bebop: Tengoku no Tobira",
                    "Cowboy Bebop: Ein no Natsuyasumi",
                ],
                "Summary": ["Cowboy Bebop: Yose Atsume Blues"],
            },
        )
        self.assertEqual(
            self.anime.opening_themes, ['"Tank!" by The Seatbelts (eps 1-25)']
        )
        self.assertEqual(
            self.anime.ending_themes,
            [
                '"The Real Folk Blues" by The Seatbelts feat. Mai Yamane (eps 1-12, '
                "14-25)",
                '"Space Lion" by The Seatbelts (ep 13)',
                '"Blue" by The Seatbelts feat. Mai Yamane (ep 26)',
            ],
        )
        self.assertEqual(
            self.anime.staff, 
            ['Maseba, Yutaka', 'Minami, Masahiko', 'Watanabe, Shinichiro', 'Kobayashi, Katsuyoshi']
        )
        self.assertEqual(
            self.anime.characters, 
            ['Spiegel, Spike:Yamadera, Kouichi', 'Valentine, Faye:Hayashibara, Megumi', 'Wong Hau Pepelu Tivrusky IV, Edward:Tada, Aoi', 'Black, Jet:Ishizuka, Unshou', 'Ein:Yamadera, Kouichi', 'Vicious:Wakamoto, Norio', 'Julia:Takashima, Gara', 'Eckener, Grencia Mars Elijah Guo:Horiuchi, Kenyuu', 'Von de Oniyate, Andy:Ebara, Masashi', 'Mad Pierrot:Ginga, Banjou']
        )


if __name__ == "__main__":
    unittest.main()
