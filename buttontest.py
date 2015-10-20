from time import sleep
import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(1.0, 1.0, 1.0)
lcd.clear()
lcd.message("How many photos to take?....")

while True:
    if (LCD.SELECT):
		lcd.message("you pressed sleect") 

    sleep(0.1);
