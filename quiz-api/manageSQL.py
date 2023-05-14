from flask import Flask, request
import sqlite3
from question import Question
# create a connection
db_connection = sqlite3.connect('./database.db')
print(db_connection)

# set the sqlite connection in "manual transaction mode"
# (by default, all execute calls are performed in their own transactions, not what we want)
db_connection.isolation_level = None

# start transaction
# Ajouter un élément
def createQuestion(payload):
	db_connection = sqlite3.connect('./database.db', timeout=30)
	db_connection.isolation_level = None
	cur = db_connection.cursor()

	cur.execute("INSERT INTO 'QUESTIONS' (position, title, text, image) VALUES (?, ?, ?, ?)", (payload["position"], payload["title"], payload["text"], payload["image"],))
	db_connection.commit()
	db_connection.close()

def getQuestion(payload):
	db_connection = sqlite3.connect('./database.db', timeout=30)
	db_connection.isolation_level = None
	cur = db_connection.cursor()

	cur.execute("SELECT * FROM QUESTIONS WHERE id = ?", (payload["position"],))

	result = cur.fetchone()
	question = Question(result[0], result[1], result[2], result[3])
	return question 
	

# save the question to db
# insertion_result = cur.execute(
# 	f"insert into Question (title) values"
# 	f"('{input_question.title}')")

# send the request
#cur.execute("commit")

# in case of exception, rollback the transaction
#cur.execute('rollback')