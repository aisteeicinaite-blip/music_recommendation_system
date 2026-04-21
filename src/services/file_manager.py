import csv
from src.models.song import Song


class FileManager:
    def load_songs(self, file_name):
        songs = []

        file = open(file_name, "r", encoding="utf-8")
        reader = csv.DictReader(file)

        for row in reader:
            song = Song(
                row["title"],
                row["artist"],
                row["genre"],
                row["mood"]
            )
            songs.append(song)

        file.close()

        return songs