def single(user_object,groups):
    return {
        "id": user_object["id"],
        "firstName": user_object["fname"],
        "lastName": user_object["lname"],
        "emailId": user_object["email"],
        "groups": groups
    }


def multiple(user_objects):
    print user_objects, "\n\n"
    return [single(user_object) for user_object in user_objects]
