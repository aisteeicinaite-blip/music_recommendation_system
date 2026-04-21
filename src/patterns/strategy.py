class GenreRecommendation:
    def recommend(self, songs, genre):
        results = []

        for song in songs:
            if song.get_genre().lower() == genre.lower():
                results.append(song)

        return results


class MoodRecommendation:
    def recommend(self, songs, mood):
        results = []

        for song in songs:
            if song.get_mood().lower() == mood.lower():
                results.append(song)

        return results