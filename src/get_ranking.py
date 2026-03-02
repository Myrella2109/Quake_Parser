import json


class GetRanking:
    """
    Caso de uso para gerar ranking global de jogadores.
    """

    def __init__(self):
        pass

    def _get_all_games(self):
        with open("data/report.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def execute(self):
        games = self._get_all_games()

        ranking = {}

        for game in games.values():
            for player, kills in game["kills"].items():
                ranking[player] = ranking.get(player, 0) + kills

        ranking_sorted = dict(
            sorted(ranking.items(), key=lambda item: item[1], reverse=True)
        )

        return ranking_sorted