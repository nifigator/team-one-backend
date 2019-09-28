from models import db, Issue, IssueSchema, IssueHistory, IssueHistorySchema

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

def get_customers() -> tuple:
    response = [{**customers[c], 'id': c} for c in customers.keys()]
    return response, 200

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

    issue_history = IssueHistory(
        issue_id=new_issue.id,
        status_id=1,
    )

    db.session.add(issue_history)
    db.session.commit()

    issue_data = issue_schema.dump(new_issue).data

    return issue_data, 201

def get_issues(customer_id: int) -> tuple:
    if customers.get(customer_id) is None:
        response = {
            'message': 'Customer with id {id} not exists'.format(id=customer_id)
        }
        return response, 409

    issues = Issue.query.filter(Issue.customer_id == customer_id).all()
    issues_schema = IssueSchema(many=True)
    issues_data = issues_schema.dump(issues).data
    return issues_data, 200

def get_all_issues() -> tuple:
    issues = Issue.query.order_by(Issue.id).all()
    issues_schema = IssueSchema(many=True)
    issues_data = issues_schema.dump(issues).data
    return issues_data, 200

def get_issue(customer_id: int, issue_id: int) -> tuple:
    if customers.get(customer_id) is None:
        response = {
            'message': 'Customer with id {id} not exists'.format(id=customer_id)
        }
        return response, 409

    issue = (
        Issue.query
        .filter(Issue.customer_id == customer_id)
        .filter(Issue.id == issue_id)
        .one_or_none() 
    )

    if issue is None:
        response = {
            'message': 'Issue with id {id} not found'.format(id=issue_id)
        }
        return response, 404

    issue_schema = IssueSchema()
    issue_data = issue_schema.dump(issue).data
    return issue_data, 200

def update_issue(customer_id: int, issue_id: int, body: dict) -> tuple:
    if customers.get(customer_id) is None:
        response = {
            'message': 'Customer with id {id} not exists'.format(id=customer_id)
        }
        return response, 409

    issue = (
        Issue.query
        .filter(Issue.customer_id == customer_id)
        .filter(Issue.id == issue_id)
        .one_or_none() 
    )

    if issue is None:
        response = {
            'message': 'Issue with id {id} not found'.format(id=issue_id)
        }
        return response, 404

    if body.get('status_id') is not None and body['status_id'] != issue.status_id:
        issue_history = IssueHistory(
            issue_id=issue.id,
            status_id=body['status_id'],
        )
        db.session.add(issue_history)

    for key in body.keys():
        setattr(issue, key, body[key])

    db.session.add(issue)
    db.session.commit()

    issue_schema = IssueSchema()
    issue_data = issue_schema.dump(issue).data

    return issue_data, 200

def get_issue_history(issue_id: int) -> tuple:
    issue_history = (
        IssueHistory.query
        .filter(IssueHistory.issue_id == issue_id)
        .all() 
    )

    if issue_history is None:
        response = {
            'message': 'Issue with id {id} not found'.format(id=issue_id)
        }
        return response, 404

    issue_history_schema = IssueHistorySchema(many=True)
    issue_history_data = issue_history_schema.dump(issue_history).data
    return issue_history_data, 200


