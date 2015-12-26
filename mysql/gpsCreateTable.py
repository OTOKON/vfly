import MySQLdb

db = MySQLdb.connect("localhost", "root", "otokon", "vfly")
cur = db.cursor()

cur.execute("CREATE TABLE gps(id INT AUTO_INCREMENT,\
    systemTime TIMESTAMP(2),\
    gpsTime TIME(2),\
    lattitude FLOAT(8,6),\
    latType CHAR,\
    longitude FLOAT(8,6),\
    lonType CHAR,\
    fix INT,\
    numOfSatellites SMALLINT,\
    altitude FLOAT,\
    speed FLOAT,\
    PRIMARY KEY(id))")
