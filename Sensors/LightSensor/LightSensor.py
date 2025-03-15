import time
import sys
import RPi.GPIO as GPIO

class LightSensor:
    def __init__(self, pin, name):
        self.PIN = pin
        self.name = name
        # self.threshold = 28 # Experimentally determined to be light level at dusk

        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BOARD)
        print(f'{self.name} is initialized')
    

    # Returns time it took for the capacitor to discharge in int(seconds * 1000). Convert to large int to maintain SOME accuracy and allow isDark() to work on a range
    def chargeTiming(self, quiet=False):
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


    # Less light/more darkness = higher reading
    # Returns True if the reading is darker than the threshold
    # def isDark(self):
        # thresholdRange = list(range(self.threshold - 2, self.threshold + 2)) # Removes ringing
        
        # reading = self.chargeTiming()
        # return any([reading > i for i in thresholdRange])
