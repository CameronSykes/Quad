#! /bin/python3

from RangeSensor.RangeSensor import RangeSensor
from LightSensor.LightSensor import LightSensor
import dht11
import RPi.GPIO as GPIO
import time
from multiprocessing import Process, Lock

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

lock = Lock()
TIMEOUT_SEC = .5

distanceSensor = RangeSensor(12, 10, "Range Sensor")
lightSensor = LightSensor(8, "Light Sensor")
# tempHumiditySensor = dht11.DHT11(pin = 10)
print("")

try:
    while True:

        if distanceSensor.isClose():
            # Take corrective action
            print("TOO CLOSE")

        lightSensor.chargeTiming()
        
#       result = tempHumiditySensor.read()
#       if result.is_valid():
#           print(f"Temperature and Humidity Sensor - Temperature:\t{result.temperature:-3.1f} C")
#           print(f"Temperature and Humidity Sensor - Humidity:\t{result.humidity:-3.1f}%")
        
        time.sleep(.5)
        print("")
except KeyboardInterrupt:
    GPIO.cleanup()
