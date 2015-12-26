import MySQLdb
from datetime import datetime

db = MySQLdb.connect("localhost", "root", "otokon", "vfly")
cur = db.cursor()

curTime = str(datetime.now())

# cur.execute("insert into gps(systemTime, gpsTime, lattitude, latType, \
# longitude, lonType, fix, numOfSatellites, altitude, speed)\
# values('%s','11:11:11.111', '32.333333', 'n', '12.222222', 'e', '11',
# '11', '21.12', '2.21')"%(curTime))

cur.execute("insert into controls(systemTime, aileron, elevator, throttle, rudder, mode)\
    values('%s', '330', '5300', '300', '133', '1')" % (curTime))

db.commit()
