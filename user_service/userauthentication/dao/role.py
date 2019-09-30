from userauthentication.core.make_database_connection import connect_to_geecoder


def create_role(role, cursor):
    sql = "insert into role(name) values('"+role+"')"
    cursor.execute(sql)



def get_latest_role():
    sql = "select * from role order by id desc limit 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    return {
                "id":result[0],
                "name":result[1]
    }


if __name__=="__main__":
    db, cursor = connect_to_geecoder()
    create_role("admin",cursor)
