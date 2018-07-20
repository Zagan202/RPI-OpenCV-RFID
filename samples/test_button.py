from button import *
import time

        
b = Button(17)

while True:
    if b.is_pressed():
        print(time.time())
