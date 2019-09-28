from models import db, Category, CategorySchema

def create_category(body: dict) -> tuple:

    existing_category = (
        Category.query
        .filter(Category.name == body.get('name'))
        .one_or_none()
    )

    if existing_category:
        response = {
            'code': 409,
            'message': 'Category {name} already exists'.format(
                name=body.get('name'))
        }
        return response, 409

    # if body.get('id') or body.get('id') == 0:
    #     del body['id']
    category_schema = CategorySchema()
    category_data = category_schema.load(body).data

    new_category = Category(**category_data)

    db.session.add(new_category)
    db.session.commit()

    category_data = category_schema.dump(new_category).data

    return category_data, 201

def get_categories() -> tuple:
    categories = Category.query.order_by(Category.id).all()

    categories_schema = CategorySchema(many=True)
    categories_data = categories_schema.dump(categories).data
    return categories_data, 200

def get_category(category_id: int) -> tuple:

    category = Category.query.filter_by(id=category_id).one_or_none()
    if category:
        category_schema = CategorySchema(only=('name','image_path','description'))
        category_data = category_schema.dump(category).data
        return category_data, 200
    else:
        response = {
            'code': 404,
            'message': 'Category with id {id} not found'.format(id=category_id)
        }
        return response, 404

def update_category(category_id: int, body: dict) -> tuple:
    category = Category.query.filter_by(id=category_id).one_or_none()

    if category is None:
        response = {
            'code': 404,
            'message': 'Category with id {id} not found'.format(id=category_id)
        }
        return response, 404

    existing_name = (
        Category.query
        .filter(Category.name == body.get('name'))
        .filter(Category.id != category_id)
        .one_or_none()
    )

    if existing_name:
        response = {
            'code': 409,
            'message': 'Category name {name} already exists'.format(
                name=body.get('name'))
        }
        return response, 409
    elif category:
        if body.get('id') or body.get('id') == 0:
            del body['id']

        for key in body.keys():
            setattr(category, key, body[key])

        db.session.add(category)
        db.session.commit()

        # Serialize and return the newly created category in the response
        category_schema = CategorySchema(only=('name','image_path','description'))
        category_data = category_schema.dump(category).data

        return category_data, 200

def delete_category(category_id: int) -> tuple:
    category = Category.query.filter_by(id=category_id).one_or_none()

    if category:
        db.session.delete(category)
        db.session.commit()
        response = {
            'code': 200,
            'message': 'Category with id {id} removed'.format(id=category_id)
        }
        return response, 200
    else:
        response = {
            'code': 404,
            'message': 'Category with id {id} not found'.format(id=category_id)
        }
        return response, 404

