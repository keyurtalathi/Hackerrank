def get_user_by_id(user_id, cursor):
    sql = "SELECT * FROM users \
           WHERE id=" + str(user_id)
    print sql

    cursor.execute(sql)
    results = cursor.fetchall()
    user_obj = {}
    for result in results:
        user_obj = {
            "id": result[0],
            "fname": result[1],
            "lname": result[2],
            "email": result[3],
            "password": result[4]
        }

    return user_obj


def get_all_user(cursor):
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    results = cursor.fetchall()
    user_obj = []
    for result in results:
        user_obj.append({
            "id": result[0],
            "fname": result[1],
            "lname": result[2],
            "email": result[3],
            "password": result[4]
        })
    return user_obj


def get_user_by_mail(email, cursor):
    sql = "select * from users where email = '" + email + "';"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return {
            "id": result[0],
            "fname": result[1],
            "lname": result[2],
            "email": result[3],
            "password": result[4]
        }
    return {}


def create_user(fname, lname, email, password, cursor):
    sql = "insert into users(fname,lname,email,password) values('" + fname + \
          "','" + lname + \
          "','" + email + \
          "','" + password + "')"

    cursor.execute(sql)
