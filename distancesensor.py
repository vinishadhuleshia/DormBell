import RPi.GPIO as GPIO
import time


def get_distance():
	GPIO.setmode(GPIO.BCM)

	TRIG = 23
	ECHO = 24

	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)


	GPIO.output(TRIG, GPIO.LOW)
	print "Waiting..."
	time.sleep(2)
	print "Calculating Distance..."
	GPIO.output(TRIG, GPIO.HIGH)
	time.sleep(0.00001)

	GPIO.output(TRIG, GPIO.LOW)

	start= time.time()
	end = time.time()

	while GPIO.input(ECHO) == False:
		start = time.time()

	while GPIO.input(ECHO) == True:
		end = time.time()

	sig_time = end-start

	distance = (sig_time*34300)/2    
	print('Distance: {} cm'.format(distance))

	GPIO.cleanup()
	return distance
