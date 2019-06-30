from models import db, Issue, IssueSchema

def get_issues() -> tuple:
    issues = Issue.query.order_by(Issue.id).all()
    issues_schema = IssueSchema(many=True)
    issues_data = issues_schema.dump(issues).data
    return issues_data, 200

