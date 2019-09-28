from models import db, Status, StatusSchema

def create_status(body: dict) -> tuple:

    existing_status = (
        Status.query
        .filter(Status.name == body.get('name'))
        .one_or_none()
    )

    if existing_status:
        response = {
            'code': 409,
            'message': 'Status {name} already exists'.format(
                name=body.get('name'))
        }
        return response, 409

    status_schema = StatusSchema()
    status_data = status_schema.load(body).data

    new_status = Status(**status_data)

    db.session.add(new_status)
    db.session.commit()

    status_data = status_schema.dump(new_status).data

    return status_data, 201

def get_statuses() -> tuple:
    statuses = Status.query.order_by(Status.id).all()

    statuses_schema = StatusSchema(many=True)
    statuses_data = statuses_schema.dump(statuses).data
    return statuses_data, 200

def get_status(status_id: int) -> tuple:

    status = Status.query.filter_by(id=status_id).one_or_none()
    if status:
        status_schema = StatusSchema(only=('name', 'description'))
        status_data = status_schema.dump(status).data
        return status_data, 200
    else:
        response = {
            'code': 404,
            'message': 'Status with id {id} not found'.format(id=status_id)
        }
        return response, 404

def update_status(status_id: int, body: dict) -> tuple:
    status = Status.query.filter_by(id=status_id).one_or_none()

    if status is None:
        response = {
            'code': 404,
            'message': 'Status with id {id} not found'.format(id=status_id)
        }
        return response, 404

    existing_name = (
        Status.query
        .filter(Status.name == body.get('name'))
        .filter(Status.id != status_id)
        .one_or_none()
    )

    if existing_name:
        response = {
            'code': 409,
            'message': 'Status name {name} already exists'.format(
                name=body.get('name'))
        }
        return response, 409
    elif status:
        if body.get('id') or body.get('id') == 0:
            del body['id']

        for key in body.keys():
            setattr(status, key, body[key])

        db.session.add(status)
        db.session.commit()

        # Serialize and return the newly created status in the response
        status_schema = StatusSchema(only=('name', 'description'))
        status_data = status_schema.dump(status).data

        return status_data, 200

def delete_status(status_id: int) -> tuple:
    status = Status.query.filter_by(id=status_id).one_or_none()

    if status:
        db.session.delete(status)
        db.session.commit()
        response = {
            'code': 200,
            'message': 'Status with id {id} removed'.format(id=status_id)
        }
        return response, 200
    else:
        response = {
            'code': 404,
            'message': 'Status with id {id} not found'.format(id=status_id)
        }
        return response, 404

