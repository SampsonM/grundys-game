from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# returns best position
# positions - a string of positions in game
# player - the player who's turn it is to move
def get_best_possible_position(positions, player):
	# if no positions can be split player past is loser
	# if positions can be split, split one and recurse

@app.route('/get-best-move', methods=['POST'])
def collection():
	if request.method == 'POST':
		data = request.get_json()

		if data and data['positions']:
			pos = get_best_possible_position(data['positions'], 1)
			return jsonify(pos)
		else:
			return jsonify('No inputs found')



if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
