# Libraries
import RPi.GPIO as GPIO
import time
import sys

class RangeSensor:
    def __init__(self, trig, echo, name, threshold=5):
        self.TRIG = trig
        self.ECHO = echo
        self.name = name
        self.threshold = threshold  # In cm
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.TRIG, GPIO.OUT) 
        GPIO.output(self.TRIG, False)

        GPIO.setup(self.ECHO, GPIO.OUT)
        GPIO.output(self.ECHO, False)
        
        GPIO.setup(self.ECHO, GPIO.IN)

        print(f'{self.name} is initialized')


    def RangeSensor_AppMain()
       from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start() 

    def isClose(self, lock, quiet=False):
        lock.acquire()
        distance = self.measure(quiet)
        if distance < self.threshold:
            return True
        else:
            return False


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
