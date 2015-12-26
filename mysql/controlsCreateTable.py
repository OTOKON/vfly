import MySQLdb

db = MySQLdb.connect("localhost", "root", "otokon", "vfly")
cur = db.cursor()

cur.execute("CREATE TABLE controls(id INT AUTO_INCREMENT,\
    systemTime TIMESTAMP(2),\
    aileron SMALLINT,\
    elevator SMALLINT,\
    throttle SMALLINT,\
    rudder SMALLINT,\
    mode SMALLINT,\
    PRIMARY KEY(id))")
