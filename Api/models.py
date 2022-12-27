from Api import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    rating = db.Column(db.Integer)

    def json(self):
        return {'id': self.id, 'title': self.title,
                'rating': self.rating}