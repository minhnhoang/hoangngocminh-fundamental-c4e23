from mongoengine import Document, StringField, IntField

class Movie(Document): #Movie inherite Document's characteristics & functionality
    title = StringField()
    image = StringField()
    year = IntField()
    