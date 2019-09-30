from flask import request
import json


def get_user_context():
    return {"username": request.headers['username'],
            "first_name":request.headers['first_name'],
            "last_name": request.headers['last_name'],
            "groups": json.loads(request.headers['groups'])
            }
