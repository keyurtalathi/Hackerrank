from apigateway.core.user_context import get_user_context
import json


def get_header_dict(headers):
    header = {}
    for key in headers:
        header[key[0]] = key[1]
    user_context = get_user_context()
    header.update(user_context)
    header["groups"] = json.dumps(header["groups"])

    return header
