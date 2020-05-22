import sys
import Adafruit_DHT
import time
import MySQLdb

db = MySQLdb.connect(host="localhost", user="user", passwd="pass", db="database")
cur = db.cursor()

sensor = Adafruit_DHT.DHT11
gpio = 17 # sample

humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
temp = (temperature)
humidity = (humidity)

while True:

    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    temp = (temperature)
    humidity = (humidity)
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    print datetimeWrite
    print temp
    print humidity
    sql = "INSERT INTO some_table (datetime, temp, humidity) VALUES (%s, %s, %s)", (datetimeWrite, temp, humidity)
    try:
        print "Writing to database..."

        cur.execute(*sql)
        db.commit()
        print "Write Complete"

    except:

        db.rollback()
        print "Failed writing to database"

    time.sleep(60)
