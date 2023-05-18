from flask_cors import CORS
from flask import Flask, request
from jwt_utils import build_token, decode_token
from manageSQL import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	size, participations = getQuizSizeAndScore()
	return {"size": size, "scores": participations}, 200

@app.route('/login', methods=['POST'])
def GetPassword():
	payload = request.get_json()
	if payload["password"] == "flask2023":
		token = build_token()
		return {"token": token}, 200
	else:
		return {}, 401

@app.route('/rebuild-db', methods=['POST'])
def rebuildDb():

	rebuildDatabase()

	return "Ok", 200


@app.route('/questions', methods=['POST'])
def postQuestion():

	try:
		authorize_request(request)
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

@app.route('/questions/<int:id>', methods=['DELETE'])
def deleteQuestionById(id):

	try:
		authorize_request(request)
	except:
		return 'Unauthorized', 401
	
	try:
		row_deleted = deleteQuestion(id)
	except:
		return 'This question doesn\'t exist', 404
	
	return {}, 204

	# if row_deleted:
	# 	return {}, 204
	# else:
	# 	return 'This question doesn\'t exist', 404
	
@app.route('/questions/all', methods=['DELETE'])
def deleteAllQuestions():

	try:
		authorize_request(request)
	except:
		return 'Unauthorized', 401

	deleteAllQuest()

	return {}, 204

@app.route('/questions/<int:id>', methods=['PUT'])
def updateQuestionById(id):

	payload = request.get_json()
	try:
		row_deleted = updateQuestion(id, payload)
	except:
		return 'This question doesn\'t exist', 404
	
	return {}, 204

	# if row_deleted:
	# 	return {}, 204
	# else:
	# 	return 'This question doesn\'t exist', 404
	
@app.route('/participations/all', methods=['DELETE'])
def deleteAllParticipations():
    
    try:
        authorize_request(request)
    except:
        return 'Unauthorized', 401
    
    deleteAllPart()
    return {}, 204

@app.route('/participations', methods=['POST'])
def postParticipation():
    
    paylod = request.get_json()
    try :
        score = addParticipation(paylod)
    except :
        return 'Bad Request', 400

    return {"playerName":paylod["playerName"],"score":score}, 200


def authorize_request(request):

	authorization = request.headers.get('Authorization')

	# Remove Bearer at the start of the key
	authorization = authorization.split(" ")[1]
	decode_token(authorization)

if __name__ == "__main__":
    app.run()