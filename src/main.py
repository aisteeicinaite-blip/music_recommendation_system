from src.services.file_manager import FileManager
from src.services.recommendation_engine import RecommendationEngine
from src.patterns.strategy import GenreRecommendation, MoodRecommendation


def show_menu():
    print("\nMusic Recommendation System")
    print("1 - Recommend by genre")
    print("2 - Recommend by mood")
    print("3 - Exit")


def main():
    file_manager = FileManager()
    songs = file_manager.load_songs("data/songs.csv")

    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "1":
            user_input = input("Enter genre: ")
            strategy = GenreRecommendation()

        elif choice == "2":
            user_input = input("Enter mood: ")
            strategy = MoodRecommendation()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Wrong choice")
            continue

        engine = RecommendationEngine(strategy)
        results = engine.recommend(songs, user_input)

        print("\nRecommended songs:\n")

        for song in results:
            print(song)


if __name__ == "__main__":
    main()