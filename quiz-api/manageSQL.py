from flask import Flask, request
import sqlite3
from question import Question
from json import dumps


def createQuestion(payload):
	db_connection = sqlite3.connect('./database.db')
	db_connection.isolation_level = None
	cur = db_connection.cursor()

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
	
	cur.execute("DELETE FROM QUESTIONS WHERE id = ?", (id,))
	deleted_rows = cur.rowcount
	
	db_connection.commit()
	db_connection.close()

	return deleted_rows != 0

def deleteAll():
	
	db_connection = sqlite3.connect('./database.db')
	db_connection.isolation_level = None
	cur = db_connection.cursor()
	
	cur.execute("DELETE FROM QUESTIONS")
	
	db_connection.commit()
	db_connection.close()

def updateQuestion(id, payload):
	
	db_connection = sqlite3.connect('./database.db')
	db_connection.isolation_level = None
	cur = db_connection.cursor()
	
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

	
	