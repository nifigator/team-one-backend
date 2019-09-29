from models import db, Event, EventSchema, Subscriber, SubscriberSchema, \
    Handler, HandlerSchema

def create_event(body: dict) -> tuple:

    event_schema = EventSchema()
    event_data = event_schema.load(body).data

    new_event = Event(**event_data)

    db.session.add(new_event)
    db.session.commit()

    event_data = event_schema.dump(new_event).data

    return event_data, 201

def get_events() -> tuple:
    events = Event.query.order_by(Event.id).all()

    events_schema = EventSchema(many=True)
    events_data = events_schema.dump(events).data
    return events_data, 200

def get_event(event_id: int) -> tuple:

    event = Event.query.filter_by(id=event_id).one_or_none()
    if event:
        event_schema = EventSchema(
            only=('dt', 'event_type', 'payload', 'state'))
        event_data = event_schema.dump(event).data
        return event_data, 200
    else:
        response = {
            'code': 404,
            'message': 'Event with id {id} not found'.format(id=event_id)
        }
        return response, 404

def update_event(event_id: int, body: dict) -> tuple:
    event = Event.query.filter_by(id=event_id).one_or_none()

    if event is None:
        response = {
            'code': 404,
            'message': 'event with id {id} not found'.format(id=event_id)
        }
        return response, 404

    if event:
        if body.get('id') or body.get('id') == 0:
            del body['id']

        for key in body.keys():
            setattr(event, key, body[key])

        db.session.add(event)
        db.session.commit()

        # Serialize and return the newly created status in the response
        event_schema = EventSchema(
            only=('dt', 'event_type', 'payload', 'state'))
        event_data = event_schema.dump(event).data

        return event_data, 200

def delete_event(event_id: int) -> tuple:
    event = Event.query.filter_by(id=event_id).one_or_none()

    if event:
        db.session.delete(event)
        db.session.commit()
        response = {
            'code': 200,
            'message': 'Event with id {id} removed'.format(id=event_id)
        }
        return response, 200
    else:
        response = {
            'code': 404,
            'message': 'Event with id {id} not found'.format(id=event_id)
        }
        return response, 404

def create_subscriber(body: dict) -> tuple:

    subscriber_schema = SubscriberSchema()
    subscriber_data = subscriber_schema.load(body).data

    new_subscriber = Subscriber(**subscriber_data)

    db.session.add(new_subscriber)
    db.session.commit()

    subscriber_data = subscriber_schema.dump(new_subscriber).data

    return subscriber_data, 201

def get_subscribers() -> tuple:
    subscribers = Subscriber.query.order_by(Subscriber.id).all()

    subscribers_schema = SubscriberSchema(many=True)
    subscribers_data = subscribers_schema.dump(subscribers).data
    return subscribers_data, 200

def get_subscriber(subscriber_id: int) -> tuple:

    subscriber = Subscriber.query.filter_by(id=subscriber_id).one_or_none()
    if subscriber:
        subscriber_schema = SubscriberSchema(
            only=('event_type', 'handler_id'))
        subscriber_data = subscriber_schema.dump(subscriber).data
        return subscriber_data, 200
    else:
        response = {
            'code': 404,
            'message': 'Event with id {id} not found'.format(id=subscriber_id)
        }
        return response, 404

def update_subscriber(subscriber_id: int, body: dict) -> tuple:
    subscriber = Subscriber.query.filter_by(id=subscriber_id).one_or_none()

    if subscriber is None:
        response = {
            'code': 404,
            'message': 'Subscriber with id {id} not found'.format(id=subscriber_id)
        }
        return response, 404

    if subscriber:
        if body.get('id') or body.get('id') == 0:
            del body['id']

        for key in body.keys():
            setattr(subscriber, key, body[key])

        db.session.add(subscriber)
        db.session.commit()

        # Serialize and return the newly created status in the response
        subscriber_schema = SubscriberSchema(only=('event_type', 'handler_id'))
        subscriber_data = subscriber_schema.dump(subscriber).data

        return subscriber_data, 200

def delete_subscriber(subscriber_id: int) -> tuple:
    subscriber = Subscriber.query.filter_by(id=subscriber_id).one_or_none()

    if subscriber:
        db.session.delete(subscriber)
        db.session.commit()
        response = {
            'code': 200,
            'message': 'Subscriber with id {id} removed'.format(id=subscriber_id)
        }
        return response, 200
    else:
        response = {
            'code': 404,
            'message': 'Subscriber with id {id} not found'.format(id=subscriber_id)
        }
        return response, 404

def create_handler(body: dict) -> tuple:

    handler_schema = HandlerSchema()
    handler_data = handler_schema.load(body).data

    new_handler = Handler(**handler_data)

    db.session.add(new_handler)
    db.session.commit()

    handler_data = handler_schema.dump(new_handler).data

    return handler_data, 201

def get_handlers() -> tuple:
    handler = Handler.query.order_by(Handler.id).all()

    handler_schema = HandlerSchema(many=True)
    handler_data = handler_schema.dump(handler).data
    return handler_data, 200

def get_handler(handler_id: int) -> tuple:

    handler = Handler.query.filter_by(id=handler_id).one_or_none()
    if handler:
        handler_schema = HandlerSchema(
            only=('about', 'cmd'))
        handler_data = handler_schema.dump(handler).data
        return handler_data, 200
    else:
        response = {
            'code': 404,
            'message': 'Handler with id {id} not found'.format(id=handler_id)
        }
        return response, 404

def update_handler(handler_id: int, body: dict) -> tuple:
    handler = Handler.query.filter_by(id=handler_id).one_or_none()

    if handler is None:
        response = {
            'code': 404,
            'message': 'Handler with id {id} not found'.format(id=handler_id)
        }
        return response, 404

    if handler:
        if body.get('id') or body.get('id') == 0:
            del body['id']

        for key in body.keys():
            setattr(handler, key, body[key])

        db.session.add(handler)
        db.session.commit()

        # Serialize and return the newly created status in the response
        handler_schema = HandlerSchema(only=('about', 'cmd'))
        handler_data = handler_schema.dump(handler).data

        return handler_data, 200

def delete_handler(handler_id: int) -> tuple:
    handler = Handler.query.filter_by(id=handler_id).one_or_none()

    if handler:
        db.session.delete(handler)
        db.session.commit()
        response = {
            'code': 200,
            'message': 'Handler with id {id} removed'.format(id=handler_id)
        }
        return response, 200
    else:
        response = {
            'code': 404,
            'message': 'Handler with id {id} not found'.format(id=handler_id)
        }
        return response, 404

