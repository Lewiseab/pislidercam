import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
shutter_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24

GPIO.setup(shutter_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

def backwards(delay, steps, photos, shutter, photorun,bulb):
	while photos >= 1:
		time.sleep(1)
		GPIO.output(shutter_pin, 1)
		time.sleep(bulb) #Used to ensure camera senses trigger - hard defined alomgside user inputs
		GPIO.output(shutter_pin, 0)
		time.sleep(shutter)
		photos = photos - 1
		print "\n" * 40 #Used to clear the console
		print "There are",photos, "photo(s) remaining to be shot of the",photorun, "you asked for."
		print "\n"
		remtime = ((shutter+2)*photos)/60
		print "Bear with me, this will take roughly" ,remtime, "minute(s) to finish..."
		for i in range(0, steps):
			setStep(1, 0, 0, 1)
			time.sleep(delay)
			setStep(0, 1, 0, 1)
			time.sleep(delay)
			setStep(0, 1, 1, 0)
			time.sleep(delay)
			setStep(1, 0, 1, 0)
			time.sleep(delay)

def setStep(w1, w2, w3, w4):
	GPIO.output(coil_A_1_pin, w1)
	GPIO.output(coil_A_2_pin, w2)
	GPIO.output(coil_B_1_pin, w3)
	GPIO.output(coil_B_2_pin, w4)

while True:
	delay = raw_input("Delay between steps (milliseconds)?")
	photos = raw_input("How many photos to take?")
	shutter = raw_input("How long is your shutter speed (seconds)?")
	steps = raw_input("How many steps backwards for each shot?")
	photorun = photos
	backwards(int(delay) / 1000.0, int(steps), int(photos), int(shutter) + 1, int(photorun),bulb=0.5)
