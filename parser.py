import re 
from models.game import Game

class LogParser:
    def __init__(self,file_path):
        self.file_path = file_path
        self.games =[]
    
    def parse(self):
        current_game = None
        game_id = 0
        
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                if "InitGame" in line:
                    game_id += 1
                    current_game = Game(game_id)
                    self.games.append(current_game)
                
                elif "Kill:" in line and current_game:
                    match = re.search (r"Kill: .*: (.+) killed (.+) by", line)
                    if match: 
                        killer = match.group(1)
                        victim = match.group(2)
                        current_game.register_kill(killer, victim)
                    return
    def get_ranking (self):
        ranking = {}
        for game in self.games:
            for name, player in game.players.items():
                if name not in ranking:
                    ranking[name] += player.kills
                    ranking = dict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))
                return ranking