#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
    while True:
        text =raw_input("Name? ")
        print("Now scan a tag to write")
        id, text = reader.write(text) 
        print("written")
        
        print(id)
        print(text)
finally:
    print("cleaning up")
    GPIO.cleanup()
