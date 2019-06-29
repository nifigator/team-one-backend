from datetime import datetime

from config import db

class Issue(db.Model):
    __tablename__ = 'issues'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(128))
    catrgory = db.Column(db.String(128), nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)
    body = db.Column(db.Text, nullable=False)
    create_data = db.Column(db.DateTime(), default=datetime.utcnow)
    rating = db.Column(db.Integer)

    def __repr__(self):
        return '<Issues {id}>'.format(id=self.id)
