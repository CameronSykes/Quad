#! /bin/python3

from RangeSensor.RangeSensor import RangeSensor
from LightSensor.LightSensor import LightSensor
import dht11
import RPi.GPIO as GPIO
import time
import GlobalData as gs
from multiprocessing import Process, Lock

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

SensorLocks = [Lock() for l in range(gs.NUM_SENSORS)]

# Instantiate sensors
LightSensors = [LightSensor(SensorLocks[0], 0,  8,     "Light Sensor 0")]
RangeSensors = [RangeSensor(SensorLocks[1], 1, 12, 10, "Range Sensor 0")]

LightSensorProcesses = []
RangeSensorProcesses = []

# Acquire locks to confirm instantiation
for lock in SensorLocks:
    lock.acquire()
    lock.release()

# Create and start sensor processes
for num, light_sensor in enumerate(LightSensors):
    LightSensorProcesses.append(Process(target=light_sensor.LightSensor_AppMain))
    LightSensorProcesses[num].start()

for num, range_sensor in enumerate(RangeSensors):
    RangeSensorProcesses.append(Process(target=range_sensor.RangeSensor_AppMain) )
    RangeSensorProcesses[num].start()

# Continually poll sensors
try:
    while True:
        # Attempt to acquire locks from each sensor as
        # a signal that the sensor is done with its operation
        for lock in SensorLocks:
            lock.acquire()

            # Release the lock so that the sensor can do its
            # next operation
            lock.release()
except KeyboardInterrupt:
    for light_sensor in LightSensorProcesses:
        while light_sensor.is_alive():
            light_sensor.join()
            time.sleep(.5)

        print("joined LS")

    for range_sensor in RangeSensorProcesses:
        while range_sensor.is_alive():
            range_sensor.join()
            time.sleep(.5)

        print("joined RS")


    GPIO.cleanup()
