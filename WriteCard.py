import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
cardWrite = SimpleMFRC522()
try:
	text = raw_input()
	print("Place your tag to write...")
	cardWrite.write(text)
	print("Write succesfully")
finally:
	gpio.cleanup()