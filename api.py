from flask import Flask, jsonify
from parser import LogParser

app = Flask(__name__)
parser =LogParser("games.log")
games = parser.parse()

@app.route("/games/<int:game_id>")
def get_game(game_id):
    for game in games:
        if game.game_id == game_id:
            return
    jsonify({f"game_{game_id}": game.get_data()})
    return jsonify({"error": "Game not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)