

def single(language_object):
    return {
        "id": language_object["id"],
        "language":language_object["name"]
    }


def multiple(language_objects):
    return [single(language_object) for language_object in language_objects]