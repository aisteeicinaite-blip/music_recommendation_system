from src.models.music_item import MusicItem


class Song(MusicItem):
    def __init__(self, title, artist, genre, mood):
        super().__init__(title)
        self.artist = artist
        self.genre = genre
        self.mood = mood

    def get_artist(self):
        return self.artist

    def get_genre(self):
        return self.genre

    def get_mood(self):
        return self.mood

    def __str__(self):
        return f"{self._title} - {self.artist} ({self.genre}, {self.mood})"