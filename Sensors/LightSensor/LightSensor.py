import time
import sys
import RPi.GPIO as GPIO
import GlobalData as gs

class LightSensor:
    def __init__(self, lock, taskId, pin, name, threshold=28):
        self.lock      = lock
        self.taskId    = taskId
        self.PIN       = pin
        self.name      = name
        self.threshold = threshold # Experimentally determined to be light level at dusk

        self.lock.acquire()

        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BOARD)
        print(f'{self.name} is initialized')

        self.lock.release()
    
    def LightSensor_AppMain(self):
        while True:
            print(self.name)
            with self.lock:
                self.lock.acquire(1)

                reading = self.measure(quiet=False)

                if reading < threshold:
                    # Take corrective action
                    print("TOO DARK")

                self.lock.release()


    # Returns time it took for the capacitor to dischiarge in int(seconds * 1000)
    def measure(self, quiet=True):
        count = 0
        timeout = 60

        # Reset the pin to low
        GPIO.setup(self.PIN, GPIO.OUT)
        GPIO.output(self.PIN, GPIO.LOW)
        
        time.sleep(0.1)
        GPIO.setup(self.PIN, GPIO.IN)

        startTime = time.time()
        while GPIO.input(self.PIN) == GPIO.LOW:
            count += 1
            if (time.time() - startTime) > timeout:
                print(f"Reading on pin {self.PIN} timed out after {timeout} seconds. Connect the live wire")
                sys.exit(1)
        
        if quiet:
            print(f"Light level for sensor on pin {self.PIN}:\t\t\t\t\t{count}")

        return count
