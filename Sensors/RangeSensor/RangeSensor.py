# Libraries
import RPi.GPIO as GPIO
import time
import sys
from multiprocessing import Lock
import GlobalData as Globals


class RangeSensor:
    def __init__(self, lock, taskId, trig, echo, name, threshold=5):
        self.lock      = lock
        self.taskId    = taskId
        self.TRIG      = trig
        self.ECHO      = echo
        self.name      = name
        self.threshold = threshold # In cm

        self.lock.acquire()

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.TRIG, GPIO.OUT) 
        GPIO.output(self.TRIG, False)

        GPIO.setup(self.ECHO, GPIO.OUT)
        GPIO.output(self.ECHO, False)
        
        GPIO.setup(self.ECHO, GPIO.IN)

        print(f'{self.name} is initialized')

        self.lock.release()


    def RangeSensor_AppMain():
        while Globals.AppRunStates[taskId] == RUN:
            with self.lock:
                self.lock.acquire()
    
                distance = self.measure(quiet=False)

                if distance < threshold:
                    # take corrective measures
                    print("TOO CLOSE")

                self.lock.release()


    def measure(self, quiet=True):
        # Send sonic signal
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        startTime = time.time()
        endTime = time.time()

        while GPIO.input(self.ECHO) == 0:
            startTime = time.time()
        
        while GPIO.input(self.ECHO) == 1:
            endTime = time.time()

        timeElapsed = endTime - startTime
        
        # Speed of sound = 34300 cm/s
        d = (34300 * timeElapsed) / 2

        if not quiet:
            print(f"{self.name} distance:\t\t\t\t{d}cm")

        return d
