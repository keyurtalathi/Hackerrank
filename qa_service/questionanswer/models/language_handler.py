from questionanswer.dao.language import add_language, get_recent_language, get_language_by_id, get_all_languages
from questionanswer.exceptions.unauthorised_exception import UnauthorisedException
from questionanswer.core.make_database_connection import connect_to_geecoder
from questionanswer.views import language as language_view


def get_handler(language_id):
    db, cursor = connect_to_geecoder()
    if language_id:
        language= get_language_by_id(language_id, cursor)
        cursor.close()
        db.close()
        if language:
            language = language_view.single(language)
        return language
    languages = get_all_languages(cursor)
    if languages:
        languages = language_view.multiple(languages)
    cursor.close()
    db.close()
    return languages


def post_handler(payload,user_context,cursor):

    if "teacher" in user_context["groups"]:
        language = payload["language"]
        add_language(language,cursor)
        res = get_recent_language(cursor)
        return res

    else:
        raise UnauthorisedException
