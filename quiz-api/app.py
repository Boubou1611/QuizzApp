from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def GetPassword():
	payload = request.get_json(), 401

if __name__ == "__main__":
    app.run()