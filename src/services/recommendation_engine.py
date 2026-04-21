class RecommendationEngine:
    def __init__(self, strategy):
        self.strategy = strategy

    def recommend(self, songs, value):
        return self.strategy.recommend(songs, value)