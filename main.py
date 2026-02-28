import json
from parser import LogParser

def main():
    parser = LogParser("games.log")
    games = parser.parse()
    print("Relatório por jogo: \n")
    for game in games:
        print(f"game_{game.game_id}:")
        print(json.dumps(game.get_data(), indent=4))
        print()
        print("Ranking geral:")
        print(json.dumps(parser.get_ranking(), indent=4))
        
        if __name__ == "__main__":
            main()
        