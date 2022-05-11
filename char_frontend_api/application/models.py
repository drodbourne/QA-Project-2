from application import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(50))
    char_class = db.Column(db.String(50))
    char_attribute = db.Column(db.String(50))
    date_generated = db.Column(db.DateTime())
    def __str__(self):
        return f"{self.char_name}: {self.char_class} primary attribute {self.char_attribute}"
