import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()
print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
print 'pressure = {0:0.1f} hPa'.format(float(sensor.read_pressure())/100 +40) # correcting pressure for Lj
print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())
print 'Altitude = {0:0.2f} m'.format(float(sensor.read_altitude()))
