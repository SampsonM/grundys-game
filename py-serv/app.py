from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# todo
# figure out which next move is best for current player
# track which players move the split it
# track if the current player wins/loses
# track the turn which allows the current player to win
	

def get_best_possible_position(positions, current_player, orig_player):
	# if no positions can be split, current player is loser
	# if positions can be split, split one and recurse to find loser

	next_player = 1 if current_player == 2 else 2
	result = False
	new_positions = ''
	
	for current_pos in positions.split(','):
		p = int(current_pos)

		if p > 2:
			stop_pos = math.floor(p/2)

			# for loop decrement -1 each time until halfway down
			for i in range(p-1, stop_pos, -1):
				bar = f"{i},{p-i}"
				new_positions = positions.replace(current_pos,  bar)
				result = get_best_possible_position(new_positions, next_player, orig_player)

				if result[0] != orig_player:
					break

	# no split happened
	if result == False:
		return [current_player, new_positions]
	else:
		return [result[0], new_positions]		



@app.route('/get-best-move', methods=['POST'])
def collection():
	if request.method == 'POST':
		data = request.get_json()

		if data and data['positions']:
			pos = get_best_possible_position(data['positions'], 1, 1)
			return jsonify(pos)
		else:
			return jsonify('No inputs found')



if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
