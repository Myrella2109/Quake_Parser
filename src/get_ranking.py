class GetRanking:
    """
    Caso de uso para gerar ranking global.
    """

    def __init__(self, games):
        self.games = games

    def execute(self):
        ranking = {}

        for game in self.games:
            for player, kills in game.kills.items():
                ranking[player] = ranking.get(player, 0) + kills

        return dict(sorted(ranking.items(), key=lambda x: x[1], reverse=True))