from cerberus import Validator

def create_event(request: any):
    body_validator = Validator({
        "data":{
            "type":"dict",
            "schema":{
                "name":{"type":"string", "required":True, "empty":False}
            }
        }
    })
    response = body_validator.validate(request.json)
    if response is False:
       raise Exception(body_validator.errors)