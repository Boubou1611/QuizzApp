# Exemple de création de classe en python
class Question():
	
    def __init__(self, id, position, title, text, image):
        self.id = id
        self.position = position 
        self.title = title
        self.text = text 
        self.image = image


    def to_json(self):
        return {
            'id' : self.id,
            'position': self.position,
            'title': self.title,
            'text': self.text,
            'image': self.image
        }
    
    def from_json(json_post):
        id = json_post.get('id')
        position = json_post.get('position')
        title = json_post.get('title')
        text = json_post.get('text')
        image = json_post.get('image')
        return Question(id=id, position=position, title=title, text=text, image=image)
        
            
    