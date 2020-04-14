from . import db

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(80))
    location = db.Column(db.String(100))
    biography = db.Column(db.Text)
    image_name = db.Column(db.String(80))
    date_created = db.Column(db.DateTime)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)