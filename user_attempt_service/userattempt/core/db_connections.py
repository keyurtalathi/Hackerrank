import MySQLdb

def connect_to_geecoder():
    db = MySQLdb.connect("127.0.0.1", "root",
                         "as2d2p", "geecoder_database")
    cursor = db.cursor()
    return db, cursor