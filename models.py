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
    management_id = db.Column(db.Integer)
    contractor = db.Column(db.String(256))
    contractor_id = db.Column(db.Integer)
    status = db.relationship('Status')
    category = db.relationship('Category')

    def __repr__(self):
        return '<Issue {id}>'.format(id=self.id)

class IssueSchema(ma.Schema):
    id = ma.Integer(only_load=True)
    status_id = ma.Integer()
    category_id = ma.Integer()
    customer_id = ma.Integer()
    management_id = ma.Integer()
    body = ma.String()
    create_data = ma.String()
    rating = ma.Integer()
    contractor = ma.String()
    contractor_id = ma.Integer()

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

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Status {name}>'.format(id=self.name)

   
class StatusSchema(ma.Schema):
    id = ma.Integer(only_load=True)
    name = ma.String()
    description = ma.String()

    def __repr__(self):
        return '<StatusSchema {name}>'.format(id=self.name)


class IssueHistory(db.Model):
    __tablename__ = 'issue_history'
    id = db.Column(db.Integer, primary_key=True)
    issue_id = db.Column(db.Integer, db.ForeignKey('issues.id'),
        nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'))
    create_time = db.Column(db.DateTime(), default=datetime.utcnow)
    reason = db.Column(db.Text)
    note = db.Column(db.Text)
    issue = db.relationship('Issue')
    status = db.relationship('Status')


class IssueHistorySchema(ma.Schema):
    id = ma.Integer(only_load=True)
    issue_id = ma.Integer()
    status_id = ma.Integer()
    customer_id = ma.Integer()
    create_time = ma.String()
    reason = ma.String()
    note = ma.String()


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    dt = db.Column(db.DateTime(), default=datetime.utcnow)
    event_type = db.Column(db.String(128), nullable=False)
    payload = db.Column(db.Text)
    state = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Event {id}>'.format(id=self.id)


class EventSchema(ma.Schema):
    id = ma.Integer(only_load=True)
    dt = ma.String()
    event_type = ma.String()
    payload = ma.String()
    state = ma.Integer()


class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(128), nullable=False)
    handler_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Subscriber {id}>'.format(id=self.id)


class SubscriberSchema(ma.Schema):
    id = ma.Integer(only_load=True)
    event_type = ma.String()
    handler_id = ma.Integer()


class Handler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.Text)
    cmd = db.Column(db.Text)

    def __repr__(self):
        return '<Handler {id}>'.format(id=self.id)


class HandlerSchema(ma.Schema):
    id = ma.Integer(only_load=True)
    about = ma.String()
    cmd = ma.String()
