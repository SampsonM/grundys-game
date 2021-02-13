from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/get-best-move', methods=['POST'])
def collection():
	if request.method == 'POST':
		data = request.get_json()
		foo = data['test'] if data else 'you provided no value here'

		return jsonify(foo)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
