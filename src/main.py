from src.services.file_manager import FileManager


def main():
    file_manager = FileManager()
    songs = file_manager.load_songs("data/songs.csv")

    print("Loaded songs:\n")

    for song in songs:
        print(song)


if __name__ == "__main__":
    main()