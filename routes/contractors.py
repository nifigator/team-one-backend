contractors = {
    1: {
        'name': "ИП Пупкин",
        'specializations': [
            "Сантехника",
        ],
    },
    2: {
        'name': "ООО Рога и копыта",
        'specializations': [
            "Электрика",
            "Сантехника",
        ],
    },
    3: {
        'name': "ООО Почини лифт",
        'specializations': [
            "Лифты",
        ]
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