# Exemple de création de classe en python
from json import dumps, loads
class Question():
	
    def __init__(self, position, title, text, image, id, possibleAnswers):
        self.id = id
        self.position = position 
        self.title = title
        self.text = text 
        self.image = image
        self.possibleAnswers = possibleAnswers


    def to_json(self):
        return {
            'id' : self.id,
            'position': self.position,
            'title': self.title,
            'text': self.text,
            'image': self.image,
            'possibleAnswers': loads(self.possibleAnswers)
        }
    
    def from_json(json_post):
        id = json_post.get('id')
        position = json_post.get('position')
        title = json_post.get('title')
        text = json_post.get('text')
        image = json_post.get('image')
        possibleAnswers = dumps(json_post.get('possibleAnswers'))
        return Question(id=id, position=position, title=title, text=text, image=image, possibleAnswers=possibleAnswers)
        

class Participation():

    def __init__(self, id, name, score):
        self.id = id
        self.name = name 
        self.score = score

    def to_json(self):
        return {
            'id' : self.id,
            'name': self.name,
            'score': self.score,
        } 
    