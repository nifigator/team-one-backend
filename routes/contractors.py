from models import db, Issue, IssueSchema

contractors = {
    1: {
        'name': "ИП Пупкин",
        'specializations': [
            "Сантехника",
        ],
        'rating': 4.7,
    },
    2: {
        'name': "ООО Рога и копыта",
        'specializations': [
            "Электрика",
            "Сантехника",
        ],
        'rating': 4.8,
    },
    3: {
        'name': "ООО Почини лифт",
        'specializations': [
            "Лифты",
        ],
        'rating': 4.9,
    }
}

def get_contractor(contractor_id: int) -> tuple:
    contractor = contractors.get(contractor_id)
    if contractor:
        return contractor, 200
    response = {
        'message': "Contractor with id {id} not found.".format(id=contractor_id)
    }
    return response, 404

def get_issues(contractor_id: int) -> tuple:
    issues = Issue.query.filter(Issue.contractor_id == contractor_id).all()
    issues_schema = IssueSchema(many=True)
    issues_data = issues_schema.dump(issues).data
    return issues_data, 200

