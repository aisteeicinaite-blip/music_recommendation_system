class MusicItem:
    def __init__(self, title):
        self._title = title

    def get_title(self):
        return self._title

    def __str__(self):
        return f"Title: {self._title}"