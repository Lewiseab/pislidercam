import RPi.GPIO as GPIO
import time
import os
import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(1.0, 1.0, 1.0)
lcd.clear()
lcd.message(" --= Lewis' =--  \n --= Slider =--")



#set the pins for the motor
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
		os.system("gphoto2 --capture-image-and-download --keep --filename %d%m%y-%H%M%S.jpg") #takes the photo, downloads it and time/date stamps it
		photos = photos - 1
		print "\n" * 60 #Used to clear the console
		print "There are",photos, "photo(s) remaining to be shot of the",photorun, "you asked for."
		print "\n"

		remtime = ((shutter+2)*photos) #Used to clauclate remianing time in seconds
		remtime_mins = int(remtime/60)
		remtime_secs = remtime%60
		print "Bear with me, this will take roughly" ,remtime_mins, "minute(s) and" ,remtime_secs ,"seconds to finish..."
		lcd.clear()
		lcd_rem_time = str(remtime_mins) + ' minutes and \n' + str(remtime_secs) + ' second(s).'
		lcd.message(str(lcd_rem_time))
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
	delay = 8 #delay between each magnet powering on in steper motor
	photos = raw_input("How many photos to take?")

	#runnning the script to retrieve the shutterspeed settings from the camera and store in variable tree
	tree = os.popen("gphoto2 --get-config shutterspeed").read()

	#save variable tree as a ext file for processing
	with open("Shutterspeed.txt", "w") as text_file:
    		text_file.write(format(tree))

	#Lets read the file and retrieve the line with the current shutterspeed
	f=open('Shutterspeed.txt')
	shutterspeed_line=f.readlines()
	shutter_speed =  shutterspeed_line[2]
	shutter = int(shutter_speed[9:]) + 2

	steps = raw_input("Move how far between shots?")
        lcd.clear()
        lcd.message("Let's begin....")
        lcd.set_color(0.0, 1.0, 0.0)
	photorun = photos
	backwards(int(delay) / 1000.0, int(steps), int(photos), float(shutter) + 1, int(photorun),bulb=0.5)
