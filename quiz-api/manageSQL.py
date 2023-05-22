from flask import Flask, request
import sqlite3
from question import Question
from json import dumps, loads
from datetime import datetime



def rebuildDatabase():

	db_connection = sqlite3.connect('./database.db') 
	cur = db_connection.cursor()

	cur.execute("DROP TABLE IF EXISTS PARTICIPATIONS")
	cur.execute("DROP TABLE IF EXISTS QUESTIONS")

	cur.execute("""
        CREATE TABLE PARTICIPATIONS (
            id INTEGER PRIMARY KEY,
            playerName TEXT NOT NULL,
            score INTEGER NOT NULL,	    	
			date TEXT
        )
    """)
	
	db_connection.commit()

	cur.execute("""
        CREATE TABLE QUESTIONS (
            position INTEGER NOT NULL,
            title TEXT NOT NULL,
            text TEXT NOT NULL,
            image TEXT,
            id INTEGER PRIMARY KEY,
            possibleAnswers TEXT
        )
    """)

	db_connection.commit()
	db_connection.close()

def getQuizSizeAndScore():

	db_connection = sqlite3.connect('./database.db')
	db_connection.isolation_level = None
	cur = db_connection.cursor()

	cur.execute("SELECT COUNT(*) FROM QUESTIONS")
	count = cur.fetchone()[0]

	cur.execute("SELECT id, playerName, score, date FROM PARTICIPATIONS ORDER BY score DESC")

	rows = cur.fetchall()
	column_names = ["id", "playerName", "score", "date"]
	json_data = [dict(zip(column_names, row)) for row in rows]
        
    # Close the connection
	db_connection.close()

	return count, json_data 


def createQuestion(payload):
	db_connection = sqlite3.connect('./database.db')
	db_connection.isolation_level = None
	cur = db_connection.cursor()
        
	cur.execute("SELECT id FROM QUESTIONS WHERE position >= ?", (payload["position"],))
	rows = cur.fetchall()
	for row in rows:
		cur.execute("UPDATE QUESTIONS SET position = position + 1 WHERE id = ?", (row[0],))

	cur.execute("INSERT INTO 'QUESTIONS' (position, title, text, image, possibleAnswers) VALUES (?, ?, ?, ?, ?)", 
	     (payload["position"], payload["title"], payload["text"], payload["image"], dumps(payload["possibleAnswers"])))    
        
	db_connection.commit()
	db_connection.close()

def getQuestion(parameter, isId):

	db_connection = sqlite3.connect('./database.db')
	db_connection.isolation_level = None
	cur = db_connection.cursor()

	if isId:
		cur.execute("SELECT * FROM QUESTIONS WHERE id = "+str(parameter)+"")
	else:
		cur.execute("SELECT * FROM QUESTIONS WHERE position = "+parameter+"")

	result = cur.fetchone()
	db_connection.close()
	return Question(result[0], result[1], result[2], result[3], result[4], result[5])

def deleteQuestion(id):

	db_connection = sqlite3.connect('./database.db')
	db_connection.isolation_level = None
	cur = db_connection.cursor()

	cur.execute("SELECT position FROM QUESTIONS WHERE id = ?", (id,))
	deleted_position = cur.fetchone()[0]

	cur.execute("UPDATE QUESTIONS SET position = position - 1 WHERE position > ?", (deleted_position,))
	
	cur.execute("DELETE FROM QUESTIONS WHERE id = ?", (id,))
	deleted_rows = cur.rowcount
	
	db_connection.commit()
	db_connection.close()

	return deleted_rows != 0

def deleteAllQuest():
	
	db_connection = sqlite3.connect('./database.db')
	db_connection.isolation_level = None
	cur = db_connection.cursor()
	
	cur.execute("DELETE FROM QUESTIONS")
	
	db_connection.commit()
	db_connection.close()

def getAllQuestions():

	db_connection = sqlite3.connect('./database.db')
	cur = db_connection.cursor()
	cur.execute("SELECT * FROM QUESTIONS")

	rows = cur.fetchall()
	keys = [description[0] for description in cur.description]

	result = []
	for row in rows:
		result.append(dict(zip(keys, row)))

	db_connection.close()
    
	return dumps(result)

def updateQuestion(id, payload):
	
	db_connection = sqlite3.connect('./database.db')
	db_connection.isolation_level = None
	cur = db_connection.cursor()

	# est ce que la position change ?
	cur.execute("SELECT position FROM QUESTIONS WHERE id = ?", (id,))
	current_position = cur.fetchone()[0]

	if current_position != payload["position"]:
		if current_position < payload["position"]:
			cur.execute(
                "UPDATE QUESTIONS SET position = position - 1 WHERE position > ? AND position <= ?",
                (current_position, payload["position"])
            )
		else:
			cur.execute(
                "UPDATE QUESTIONS SET position = position + 1 WHERE position >= ? AND position < ?",
                (payload["position"], current_position)
            )

	
	cur.execute("""
        UPDATE QUESTIONS 
        SET position = ?, title = ?, text = ?, image = ?, possibleAnswers = ? 
        WHERE id = ?""",
        (payload["position"], payload["title"], payload["text"], 
         payload["image"], dumps(payload["possibleAnswers"]), id))
	
	updated_questions = cur.rowcount
	
	db_connection.commit()
	db_connection.close()

	return updated_questions != 0

def deleteAllPart() :
    
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()

    cur.execute("DELETE FROM PARTICIPATIONS")
    
    db_connection.commit()
    db_connection.close()

def addParticipation(paylod) :
    
    if len(paylod["answers"]) != 10:
        raise ValueError("Bad Request. Le nombre de réponses est incorrect.")

    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()

    score = 0
    current_date  = datetime.now().strftime('%Y-%m-%d')

    for index, answer in enumerate(paylod["answers"]):
        question = cur.execute("SELECT * FROM QUESTIONS WHERE position = ?", (index + 1,)).fetchone()
        if not question:
            db_connection.close()
            raise ValueError("La question {} n'a pas été trouvée.".format(index + 1))

        possible_answers = loads(question[5])

        if not 1 <= answer <= len(possible_answers):
            db_connection.close()
            raise ValueError("La réponse à la question {} est invalide.".format(index + 1))

        selected_answer = possible_answers[answer - 1]

        if selected_answer["isCorrect"]:
            score += 1
	    
    cur.execute("INSERT INTO PARTICIPATIONS (playerName, score, date) VALUES (?, ?, ?)",(paylod["playerName"], score, current_date))
    
    db_connection.commit()
    db_connection.close()
    
    return score

	
	