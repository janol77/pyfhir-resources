from db import db


class Test2(db.Document):

    title = db.StringField(max_length=60)
    text = db.StringField()
