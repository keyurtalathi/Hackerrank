from userauthentication.core.make_database_connection import connect_to_geecoder


def create_user_group(user_id,role_id, cursor):
    sql = "insert into user_groups(user_id, role_id) values('" + str(user_id) + \
          "','" + str(role_id) +"')"

    cursor.execute(sql)


def get_roles(user_id, cursor):
    sql = "select r.name from role r, user_groups ug where r.id=ug.role_id and ug.user_id="+str(user_id)
    print "============++++++++++++++++"+sql
    cursor.execute(sql)
    result =[]
    for row in cursor.fetchall():
        result.append(row[0])
    return result


if __name__=="__main__":
    db, cursor = connect_to_geecoder()
    print get_roles(1,cursor)
    db.close()
    cursor.close()