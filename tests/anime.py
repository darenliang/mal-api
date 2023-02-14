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
            ["Action", "Award Winning", "Sci-Fi"],
        )
        self.assertEqual(self.anime.themes, ["Adult Cast", "Space"])
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
            "Crime is timeless. By the year 2071, humanity has expanded across the galaxy, filling the surface of other planets with settlements like those on Earth. These new societies are plagued by murder, drug use, and theft, and intergalactic outlaws are hunted by a growing number of tough bounty hunters.  Spike Spiegel and Jet Black pursue criminals throughout space to make a humble living. Beneath his goofy and aloof demeanor, Spike is haunted by the weight of his violent past. Meanwhile, Jet manages his own troubled memories while taking care of Spike and the Bebop, their ship. The duo is joined by the beautiful con artist Faye Valentine, odd child Edward Wong Hau Pepelu Tivrusky IV, and Ein, a bioengineered Welsh Corgi.  While developing bonds and working to catch a colorful cast of criminals, the Bebop crew's lives are disrupted by a menace from Spike's past. As a rival's maniacal plot continues to unravel, Spike must choose between life with his newfound family or revenge for his old wounds.  [Written by MAL Rewrite]",
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
                '"The Real Folk Blues" by The Seatbelts feat. Mai Yamane (eps  1-12, 14-25)',
                '"Space Lion" by The Seatbelts (eps 13)',
                '"Blue" by The Seatbelts feat. Mai Yamane (eps 26)',
            ]
        )
        self.assertEqual(self.anime.characters[0].name, "Spiegel, Spike")
        self.assertEqual(self.anime.characters[0].role, "Main")
        self.assertEqual(self.anime.characters[0].voice_actor, "Yamadera, Kouichi")
        self.assertEqual(self.anime.staff[0].name, "Maseba, Yutaka")
        self.assertEqual(self.anime.staff[0].role, "Producer")


if __name__ == "__main__":
    unittest.main()
