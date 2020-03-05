# main.py -- put your code here!
from machine import Pin
import time

counter = 5
p = Pin(2,Pin.OUT)

while(1):
    p.on()
    time.sleep(1)
    p.off()
    time.sleep(1)

print("termino")