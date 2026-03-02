import json

from src.log_reader import LogReader
from src.parser import ParseGames
from src.get_ranking import GetRanking


def main():
    log_reader = LogReader("data/games.log")

    # Executa parsing
    games = ParseGames(log_reader).execute()

    # ==========================
    # Geração do relatório JSON
    # ==========================
    report = {}

    for game in games:
        report[f"game_{game.game_id}"] = {
            "total_kills": game.total_kills,
            "players": list(game.players),
            "kills": game.kills
        }

    with open("data/report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

   
    ranking = GetRanking(games).execute()

    print("\n=== RANKING GLOBAL ===")
    for player, kills in ranking.items():
        print(f"{player}: {kills}")


if __name__ == "__main__":
    main()