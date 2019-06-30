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
