import MySQLdb
import os
import time

os.system("cd /home/username/workspace/maestro-linux/")

db = MySQLdb.connect("localhost", "root", "otokon", "vfly")
cur = db.cursor()

rowc = 1
time2 = time.time()


while 1:
    db.autocommit(True)
    cur.execute("select*from controls order by id desc limit 1")
    row = cur.fetchone()
    if row != rowc:
        # command = "./UscCmd --servo 0," + str(row[2])
        # os.system(command0)
        # command = "./UscCmd --servo 1," + str(row[3])
        # os.system(command)
        # command = "./UscCmd --servo 2," + str(row[4])
        # os.system(command)
        command = "./UscCmd --servo 3," + str(row[5])
        print command
    rowc = row
    time1 = time.time()
    time.sleep((time.time() - time1) < 0.1)


# os.system(command)
