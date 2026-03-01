import re
from src.models import Game


class ParseGames:
    """
    Caso de uso responsável por transformar
    o log em objetos Game.
    """

    def __init__(self, log_reader):
        self.log_reader = log_reader

    def execute(self):
        games = []
        current_game = None
        game_id = 0

        lines = self.log_reader.read_lines()

        for line in lines:

            if "InitGame" in line:
                game_id += 1
                current_game = Game(game_id)
                games.append(current_game)

            elif "Kill:" in line and current_game:
                match = re.search(
                    r'Kill:\s+\d+\s+\d+\s+\d+:\s+(.*?)\s+killed\s+(.*?)\s+by',
                    line
                )

                if match:
                    killer = match.group(1)
                    victim = match.group(2)
                    current_game.register_kill(killer, victim)

        return games