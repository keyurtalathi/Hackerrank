from datetime import datetime
from userauthentication.utils.datetime_utils import datetime_to_utcms


def get_session(token, cursor):
    current_date = datetime.now()
    epoch = datetime_to_utcms(current_date)
    sql = "select * from user_session where token like '" + token + \
          "' and expiry >" + str(epoch)
    cursor.execute(sql)
    results = cursor.fetchall()
    session = {}
    for result in results:
        session = {
            "token": result[0],
            "user_id": result[2]
        }
    return session


def create_user_session(user_id, token, cursor, expiry):
    sql = "insert into user_session(id,token,user_id,expiry) values('" + \
          token + "','" + \
          token + "'," + \
          str(user_id) + "," + \
          str(expiry) + ")"
    cursor.execute(sql)
