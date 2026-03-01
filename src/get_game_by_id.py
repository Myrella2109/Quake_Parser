class GetGameById:
    """
    Caso de uso para buscar jogo por ID.
    """

    def __init__(self, games):
        self.games = games

    def execute(self, game_id: int):
        for game in self.games:
            if game.game_id == game_id:
                return game.to_dict()
        return None