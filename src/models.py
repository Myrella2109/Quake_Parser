
class Game:
    """
    Entidade principal do sistema.
    Contém apenas regra de negócio.
    """

    def __init__(self, game_id: int):
        self.game_id = game_id
        self.total_kills = 0
        self.players = set()
        self.kills = {}

    def add_player(self, player: str):
        if player != "<world>":
            self.players.add(player)
            if player not in self.kills:
                self.kills[player] = 0

    def register_kill(self, killer: str, victim: str):
        self.total_kills += 1
        self.add_player(victim)

        if killer == "<world>":
            self.kills[victim] -= 1
        else:
            self.add_player(killer)
            self.kills[killer] += 1

    def to_dict(self):
        return {
            "id": self.game_id,
            "total_kills": self.total_kills,
            "players": list(self.players),
            "kills": self.kills
        }