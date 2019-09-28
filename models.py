from datetime import datetime

from config import db, ma

class Issue(db.Model):
    __tablename__ = 'issues'
    id = db.Column(db.Integer, primary_key=True)
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'),
        default=2)
    category_id = db.Column(db.Integer,
        db.ForeignKey('categories.id'))
    customer_id = db.Column(db.Integer, nullable=False)
    body = db.Column(db.Text, nullable=False)
    create_data = db.Column(db.DateTime(), default=datetime.utcnow)
    rating = db.Column(db.Integer)
    contractor = db.Column(db.String(256))
    status = db.relationship('Status')
    category = db.relationship('Category')

    def __str__ (self):
        return self.name

    def __repr__(self):
        return '<Issue {id}>'.format(id=self.id)

class IssueSchema(ma.Schema):
    id = ma.Integer(only_load=True)
    status_id = ma.Integer()
    category_id = ma.Integer()
    customer_id = ma.Integer()
    body = ma.String()
    create_data = ma.String()
    rating = ma.Integer()
    contractor = ma.String()

    def __repr__(self):
        return '<IssueSchema {id}>'.format(id=self.id)

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image_path = db.Column(db.String(255))
    description = db.Column(db.Text)

    def __str__ (self):
        return self.name

    def __repr__(self):
        return '<Category {id}>'.format(id=self.id)

class CategorySchema(ma.Schema):
    id = ma.Integer(only_load=True)
    name = ma.String()
    image_name = ma.String()
    description = ma.String()

    def __str__ (self):
        return self.name

    def __repr__(self):
        return '<CategorySchema {id}>'.format(id=self.id)


class Status(db.Model):
    __tablename__ = 'statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Status {id}>'.format(id=self.id)

   
class StatusSchema(ma.Schema):
    id = ma.Integer(only_load=True)
    name = ma.String()
    description = ma.String()

    def __repr__(self):
        return '<StatusSchema {id}>'.format(id=self.id)


