from db import db


class Test(db.Document):

    title = db.StringField(max_length=60)
    text = db.StringField()
