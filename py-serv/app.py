from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-best-move', methods=['GET'])
def collection():
	if request.method == 'GET':
		data = request.form
		foo = data['test'] if data else 'you provided no value here'

		return jsonify(foo)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
