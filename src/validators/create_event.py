from cerberus import Validator

def create_event_validator(request:any):
    data : {
        "type": "dict",
        "schema" : {
            "name": {"type": "string", "required": True, "empty": False},
        }
    }
    body = Validator(schema)
    response = body.validate(request.json)

    if response is False:
        return body.errors
    return response