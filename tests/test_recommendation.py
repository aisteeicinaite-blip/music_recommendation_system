import unittest

from src.models.song import Song
from src.patterns.strategy import GenreRecommendation, MoodRecommendation


class TestRecommendation(unittest.TestCase):
    def setUp(self):
        self.songs = [
            Song("Song1", "Artist1", "Pop", "Happy"),
            Song("Song2", "Artist2", "Rock", "Sad"),
            Song("Song3", "Artist3", "Pop", "Happy"),
        ]

    def test_genre(self):
        strategy = GenreRecommendation()
        result = strategy.recommend(self.songs, "Pop")
        self.assertTrue(len(result) > 0)

    def test_mood(self):
        strategy = MoodRecommendation()
        result = strategy.recommend(self.songs, "Happy")
        self.assertTrue(len(result) > 0)

    def test_max_3_results(self):
        strategy = GenreRecommendation()
        result = strategy.recommend(self.songs, "Pop")
        self.assertTrue(len(result) <= 3)

    def test_case_insensitive_input(self):
        strategy = GenreRecommendation()
        result = strategy.recommend(self.songs, "pop")
        self.assertTrue(len(result) > 0)


    def test_empty_song_list(self):
        strategy = MoodRecommendation()
        result = strategy.recommend([], "Happy")
        self.assertEqual(result, [])

    
if __name__ == "__main__":
    unittest.main()