from flask.globals import session


def get_user_context():
    return {"username": session['username'],
            "groups": session['groups'],
            "last_name" : session["last_name"],
            "first_name" : session["first_name"],
            "userId" : str(session["user_id"])
    }
