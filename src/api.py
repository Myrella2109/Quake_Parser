from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.get_game_by_id import GetGameById, get_all_games
from src.get_ranking import GetRanking


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("\n=========== RESUMO DO SISTEMA ===========")

    games = get_all_games()

    total_games = len(games)
    total_kills_global = sum(game["total_kills"] for game in games.values())

    print(f"Total de jogos processados: {total_games}")
    print(f"Total global de kills: {total_kills_global}")

    ranking = GetRanking().execute()

    print("\n--- Ranking Global ---")

    for position, (player, kills) in enumerate(ranking.items(), start=1):
        print(f"{position}. {player} - {kills} kills")

    print("==========================================\n")

    yield


# 👇 ESSA LINHA É OBRIGATÓRIA
app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
   
    games = get_all_games()

    total_games = len(games)
    total_kills_global = sum(game["total_kills"] for game in games.values())

    ranking = GetRanking().execute()

    return {
        "total_games": total_games,
        "total_kills_global": total_kills_global,
        "ranking_global": ranking
    }


@app.get("/games/{game_id}")
def get_game(game_id: int):
    use_case = GetGameById()
    game = use_case.execute(game_id)

    if not game:
        return {"detail": "Game não encontrado"}

    return game


@app.get("/ranking")
def ranking():
    return GetRanking().execute()