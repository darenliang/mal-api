import unittest

from mal import Manga


class TestManga(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manga = Manga(1)

    def test_manga(self):
        self.assertEqual(self.manga.mal_id, 1)
        self.assertEqual(self.manga.title, "Monster")
        self.assertEqual(self.manga.title_english, "Monster")
        self.assertEqual(self.manga.title_japanese, "MONSTER")
        self.assertEqual(self.manga.title_synonyms, [])
        self.assertEqual(self.manga.url, "https://myanimelist.net/manga/1/Monster")
        self.assertEqual(
            self.manga.image_url, "https://cdn.myanimelist.net/images/manga/3/54525.jpg"
        )
        self.assertEqual(self.manga.type, "Manga")
        self.assertEqual(self.manga.status, "Finished")
        self.assertEqual(
            self.manga.genres, ["Mystery", "Drama", "Psychological", "Seinen"]
        )
        self.assertIsInstance(self.manga.score, float)
        self.assertIsInstance(self.manga.scored_by, int)
        self.assertIsInstance(self.manga.rank, int)
        self.assertIsInstance(self.manga.popularity, int)
        self.assertIsInstance(self.manga.members, int)
        self.assertIsInstance(self.manga.favorites, int)
        self.assertEqual(
            self.manga.synopsis,
            "Kenzou Tenma, a renowned Japanese neurosurgeon working in post-war "
            "Germany, faces a difficult choice: to operate on Johan Liebert, an orphan "
            "boy on the verge of death, or on the mayor of Düsseldorf. In the end, "
            "Tenma decides to gamble his reputation by saving Johan, effectively "
            "leaving the mayor for dead.  As a consequence of his actions, hospital "
            "director Heinemann strips Tenma of his position, and Heinemann's daughter "
            "Eva breaks off their engagement. Disgraced and shunned by his colleagues, "
            "Tenma loses all hope of a successful career—that is, until the mysterious "
            "killing of Heinemann gives him another chance.  Nine years later, Tenma "
            "is the head of the surgical department and close to becoming the director "
            "himself. Although all seems well for him at first, he soon becomes "
            "entangled in a chain of gruesome murders that have taken place throughout "
            "Germany. The culprit is a monster—the same one that Tenma saved on that "
            "fateful day nine years ago.  [Written by MAL Rewrite]",
        )
        self.assertEqual(
            self.manga.background,
            "Monster won the Grand Prize at the 3rd annual Tezuka Osamu Cultural Prize "
            "in 1999, as well as the 46th Shogakukan Manga Award in the General "
            "category in 2000.  The series was published in English by VIZ Media under "
            "the VIZ Signature imprint from February 21, 2006 to December 16, 2008, "
            "and again in 2-in-1 omnibuses (subtitled The Perfect Edition) from July "
            "15, 2014 to July 19, 2016. The manga was also published in Brazilian "
            "Portuguese by Panini Comics/Planet Manga from June 2012 to April 2015, in "
            "Polish by Hanami from March 2014 to February 2017, in Spain by Planeta "
            "Cómic from June 16, 2009 to September 21, 2010, and in Argentina by LARP "
            "Editores.",
        )
        self.assertEqual(self.manga.volumes, 18)
        self.assertEqual(self.manga.chapters, 162)
        self.assertEqual(self.manga.published, "Dec  5, 1994 to Dec  20, 2001")
        self.assertEqual(self.manga.authors, ["Urasawa, Naoki"])
        self.assertEqual(
            self.manga.related_manga,
            {
                "Adaptation": ["Monster"],
                "Side story": [
                    "Mou Hitotsu no Monster: The Investigative Report",
                ],
            },
        )


if __name__ == "__main__":
    unittest.main()
