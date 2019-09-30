def add_language(language,cursor):
    sql = "insert into languages(name) values('" + language + "')"
    cursor.execute(sql)


def get_recent_language(cursor):
    sql = "select * from languages order by id  desc limit 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return {
            "id": result[0],
            "name": result[1]
        }
    return {}


def get_language_by_id(language_id, cursor):
    sql = "SELECT * FROM languages \
               WHERE id=" + str(language_id)
    print sql

    cursor.execute(sql)
    result = cursor.fetchone()
    language_obj = {}
    if result:
        language_obj = {
            "id": result[0],
            "name": result[1],
        }

    return language_obj


def get_all_languages(cursor):
    sql = "SELECT * FROM languages"
    print sql

    cursor.execute(sql)
    results = cursor.fetchall()
    languages = []
    for result in results:
        language_obj = {
            "id":result[0],
            "name": result[1],
        }
        languages.append(language_obj)

    return languages