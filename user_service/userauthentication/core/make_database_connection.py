import MySQLdb
from userauthentication.utils.config_utils import get_env_config


def connect_to_geecoder():
    config = get_env_config()
    db = MySQLdb.connect(config.USER_DB_URL, config.USER_DB_USER,
                         config.USER_DB_PASSWORD, config.USER_DATABASE)
    cursor = db.cursor()
    return db, cursor

# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > '%d'" % (1000)
# try:
#    # Execute the SQL command
#    cursor.execute(sql)
#    # Fetch all the rows in a list of lists.
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#       # Now print fetched result
#       print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
#              (fname, lname, age, sex, income )
# except:
#    print "Error: unable to fecth data"
#
# # disconnect from server
# db.close()
