from models.player import Player

class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        self.total_kills = 0
        self.players = {}
    
    def add_player(self, name):
        if name not in self.players:
            self.players[name] = Player(name)
    
    def register_kill(self, killer, victim):
        self.total_kills += 1

        if killer == "<world>":
            if victim in self.players:
                self.players[victim].remove_kill() 
            return
        
        self.add_player(killer)
        self.add_player(victim)
        self.players[killer].add_kill()

    def get_data(self):
        return {
            "total_kills":
            self.total_kills, "players":
            list(self.players.keys()), "kills":{name: player.kills for name, player in self.players.items()},
        }
                