from app import db


class Flaskr(db.Model):

    __tablename__ = 'flaskr'

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    @classmethod
    def get_all_posts(cls):
        return db.session.query(cls)

    def __repr__(self):
        return '<title {}>'.format(self.body)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
