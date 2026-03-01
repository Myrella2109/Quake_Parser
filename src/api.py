from fastapi import FastAPI, HTTPException


from src.get_game_by_id import GetGameById
from src.get_ranking import GetRanking



app = FastAPI(
    title="Quake Parser API",
    description="API para consulta de jogos e ranking do Quake",
    version="1.0.0"
)



@app.get("/")
def read_root():
    """
    Rota principal apenas para verificar
    se a API está funcionando.
    """
    return {"message": "API Quake Parser está funcionando 🚀"}



@app.get("/games/{game_id}")
def get_game(game_id: int):
    """
    Retorna um jogo específico pelo ID.
    """

    game = GetGameById(game_id)

    if not game:
        raise HTTPException(status_code=404, detail="Game não encontrado")

    return game



@app.get("/ranking")
def ranking():
    """
    Retorna o ranking global de jogadores.
    """

    return GetRanking()
