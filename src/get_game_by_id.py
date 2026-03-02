import json


def get_all_games():
    """
    Lê o arquivo report.json e retorna todos os jogos.
    """
    with open("data/report.json", "r", encoding="utf-8") as file:
        return json.load(file)


class GetGameById:
    """
    Caso de uso para buscar jogo por ID.
    """

    def execute(self, game_id: int):
        games = get_all_games()
        return games.get(str(game_id))