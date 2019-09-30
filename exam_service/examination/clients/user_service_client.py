import json
import requests
from flask import current_app as app
from examination.utils.redis_decorators import get_custom_memoizer
from examination.exceptions.vaidation_exception import ValidationException


def authenticate_user(username, password, app=None):
    url = app.config["USER_SERVICE_URL"] + 'userservice/uservalidationlmd/'
    params = {'emailId': username, 'password': password,
              "rememberMe": False}  # Now you are just somebody that I used to know..
    headers = {'content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(params))
    response_data = response.json()
    if response.status_code != 200:
        error_message = "The email or password you entered is incorrect"

        if "responseData" in response_data:
            if "errorMessage" in response_data["responseData"]:
                error_message = response_data["responseData"]["errorMessage"]
        return (None, response.status_code, [error_message])

    token = response_data["responseData"][app.auth_header_name] if (
        "responseData" in response_data and app.auth_header_name in
        response_data[
            "responseData"]) else None
    return token


@get_custom_memoizer("get_active_user")
def get_active_user(token=None, app=None):
    print "<url---->", app.config["USER_SERVICE_URL"]
    url = app.config["USER_SERVICE_URL"] + '/userservice/user'
    print "User examination ===>", url
    headers = {app.auth_header_name: token,
               "content-type": "application/json", }
    try:
        response = requests.get(url, headers=headers)
    except:
        raise ValidationException(errorMessage="Wrong password/username")
    # if response.status_code != 200:
    # 	return (None, response.status_code, ["Unauthorised user"])
    response_data = response.json()
    print response_data
    # if "responseData" in response_data:
    # 	response_data = response_data["responseData"]
    # 	return (response_data, response.status_code, [])

    # return (None, response.status_code, ["Something went wrong"])
    return response_data.get("responseData")
