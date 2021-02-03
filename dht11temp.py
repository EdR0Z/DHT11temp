# Script made by ElectroFactory
# Do not share without prior permission
# Do not modify without prior permission
# Discord https://discord.gg/4PvNBzg

# -*- coding: utf-8 -*-
#!/usr/bin/env python3

#Setup libs
import RPi.GPIO as GPIO
import dht11
import time
from time import sleep
import os

#Setup i/o
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

#Setup vars
instance = dht11.DHT11(pin=11)

#Start loop setup
while True:
    result = instance.read().temperature
    if result != 0:
        print(f'{result}°C')
#End loop setup