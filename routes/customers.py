from models import db, Issue, IssueSchema

customers = {
    1: {
        'name': "Иван",
        'middlename': "Иванович",
        'surname': "Иванов",
        'flat': 99,
        'house': "55a",
        'street': "Ивановская",
        'phone': "+79991234567",
        'email': "ivan@ivanov.com",
    },
    2: {
        'name': "Иван",
        'middlename': "Петрович",
        'surname': "Сидоров",
        'flat': 19,
        'house': "21",
        'street': "Сиреневая",
        'phone': "+79991234568",
        'email': "ivan@pertorv.com",
    },
    3: {
        'name': "Петр",
        'middlename': "Петрович",
        'surname': "Иванов",
        'flat': 139,
        'house': "87",
        'street': "Грушевая",
        'phone': "+79891234568",
        'email': "petr@pivanov.org",
    },
    4: {
        'name': "Петр",
        'middlename': "Иванович",
        'surname': "Петров",
        'flat': 9,
        'house': "34Б",
        'street': "Цветная",
        'phone': "+79891234569",
        'email': "petr@petrov.org",
    },

}

def get_customer(customer_id: int) -> tuple:
    customer = customers.get(customer_id)
    if customer:
        return customer, 200
    response = {
        'message': 'Customer with id {id} not found'.format(id=customer_id)
    }
    return response, 404

def create_issue(customer_id: int, body: dict) -> tuple:
    issue_schema = IssueSchema()
    issue_data = issue_schema.load(body).data

    new_issue = Issue(**issue_data)

    if customers.get(customer_id):
        new_issue.customer_id = customer_id
    else:
        response = {
            'message': 'Customer with id {id} not exists'.format(id=customer_id)
        }
        return response, 409

    db.session.add(new_issue)
    db.session.commit()

    issue_data = issue_schema.dump(new_issue).data

    return issue_data, 201
