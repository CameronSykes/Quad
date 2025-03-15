#! /bin/python3

from RangeSensor.RangeSensor import RangeSensor
from LightSensor.LightSensor import LightSensor
import dht11
import RPi.GPIO as GPIO
import time
import Globals
from multiprocessing import Process, Lock

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

SensorLocks = [Lock() for l in range(NUM_LOCKS)]

# Instantiate sensors
LightSensors = [LightSensor(SensorLocks[0], 0,  8,     "Light Sensor 0")]
RangeSensors = [RangeSensor(SensorLocks[1], 1, 12, 10, "Range Sensor 0")]

# Acquire locks to confirm instantiation
for lock in SensorLocks:
    lock.acquire()
    lock.release()

# Spawn sensor processes
for light_sensor in LightSensors:
    Process(target=light_sensor.LightSensor_AppMain).start()

for range_sensor in RangeSensor:
    Process(target=range_sensor.RangeSensor_AppMain).start()

# Continually poll sensors
try:
    while True:
        # Attempt to acquire locks from each sensor as
        # a signal that the sensor is done with its operation
        for lock in SensorLocks:
            lock.acquire()
            print("Lock acquired")

            # Release the lock so that the sensor can do its
            # next operation
            lock.release()
            print("Lock released")
except KeyboardInterrupt:
    for sensor in range(NUM_SENSORS):
        AppRunStates[sensor] = EXIT

    GPIO.cleanup()
