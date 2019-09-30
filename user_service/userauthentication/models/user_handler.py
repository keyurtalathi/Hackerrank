from userauthentication.dao.user import get_user_by_id, get_all_user, \
    get_user_by_mail, create_user
from userauthentication.dao.user_group import create_user_group, get_roles
from userauthentication.dao.session import get_session
from userauthentication.views import user as userview
from userauthentication.core.make_database_connection import connect_to_geecoder
from userauthentication.exceptions.already_object_exist import AlreadyExist


def get_user_handler(headers, user_id):
    db, cursor = connect_to_geecoder()
    user_session = get_session(headers['X-Authorization-Token'], cursor)
    current_user_id = user_session['user_id']

    if user_id:
        user = get_user_by_id(user_id, cursor)
        groups = get_roles(user["id"], cursor)
    else:
        user = get_user_by_id(current_user_id, cursor)
        groups = get_roles(user["id"], cursor)
    if not user:
        cursor.close()
        db.close()
        return {}
    cursor.close()
    db.close()
    return userview.single(user, groups)


def post_user_handler(payload):
    db, cursor = connect_to_geecoder()
    email = payload['email']
    user = get_user_by_mail(email, cursor)
    if user:
        raise AlreadyExist

    create_user(payload["firstName"],
                payload["lastName"],
                payload["email"],
                payload["password"],
                cursor)
    user = get_user_by_mail(email, cursor)
    create_user_group(user["id"], payload["role_id"], cursor)
    groups = get_roles(user["id"], cursor)
    db.commit()
    cursor.close()
    db.close()
    return userview.single(user, groups)
