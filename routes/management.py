from models import db, Issue, IssueSchema

from routes.customers import customers

def get_issues(offset=0, limit=None, sort='') -> tuple:
    # issues = Issue.query.order_by(Issue.id).all()
    issues = Issue.query
    # if sort:
    #     # sort_fields = sort.split(',')
    #     if sort.startswith('-'):
    #         print('Match desc')
    #     field = sort
    #     issue_schema = IssueSchema(many=True)
    #     fields = issue_schema.declared_fields.keys()
    #     if field in fields:
    #         print('Field match')
    #     # valid_sort_fields = list(set(fields) & set(sort_fields))
    #     # for field in valid_sort_fields:
    #     #     issues.order_by(field)
    # else:
    issues = issues.order_by(Issue.id)
    if offset >= 0 and (limit == None or limit > 0):
        limit = offset + limit if limit else None
        issues = issues.slice(offset, limit)
    else:
        issues = issues.all()
    issues_schema = IssueSchema(many=True)
    issues_data = issues_schema.dump(issues).data
    issues_with_custs = []
    for issue in issues_data:
        if issue.get('customer_id'):
            customer = customers.get(issue.get('customer_id'))
            if customer:
                issue['customer'] = customer

    return issues_data, 200

def get_issues_by_mgmt(management_id: int) -> tuple:
    issues = Issue.query.filter(Issue.management_id == management_id).all()
    issues_schema = IssueSchema(many=True)
    issues_data = issues_schema.dump(issues).data
    return issues_data, 200

