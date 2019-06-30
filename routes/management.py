from models import db, Issue, IssueSchema

def get_issues(offset=0, limit=None, sort='') -> tuple:
    # issues = Issue.query.order_by(Issue.id).all()
    issues = Issue.query
    if sort:
        sort_fields = sorf.split(',')
    issues = issues.order_by(Issue.id)
    if offset >= 0 and (limit == None or limit > 0):
        limit = offset + limit if limit else None
        issues = issues.slice(offset, limit)
    else:
        issues = issues.all()
    issues_schema = IssueSchema(many=True)
    issues_data = issues_schema.dump(issues).data
    return issues_data, 200

