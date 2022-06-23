import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
cardRead = SimpleMFRC522()

print("Scanning for a card...")

try:
	id,text = cardRead.read()
	print(id)
	print(text)
finally:
	gpio.cleanup()