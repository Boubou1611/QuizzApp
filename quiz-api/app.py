from flask_cors import CORS
from flask import Flask, request
from jwt_utils import build_token, decode_token
from manageSQL import createQuestion, getQuestion

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
	payload = request.get_json()
	if payload["password"] == "flask2023":
		token = build_token()
		return {"token": token}, 200
	else:
		return {}, 401

@app.route('/questions', methods=['POST'])
def postQuestion():
	authorization = request.headers.get('Authorization')

	try:
		# Remove Bearer at the start of the key
		authorization = authorization.split(" ")[1]
		decode_token(authorization)
	except:
		return 'Unauthorized', 401
	
	payload = request.get_json()

	createQuestion(payload)
	return {"id": payload["position"]}, 200
	
@app.route('/questions/<int:id>', methods=['GET'])
def getQuestById(id):

	try:
		question = getQuestion(id, True)
	except:
		return 'This question doesn\'t exist', 404
	
	return question.to_json(), 200

@app.route('/questions', methods=['GET'])
def getQuestByPosition():
	position = request.args.get('position')

	try:
		question = getQuestion(position, False)
	except:
		return 'This question doesn\'t exist', 404
	
	return question.to_json(), 200

if __name__ == "__main__":
    app.run()