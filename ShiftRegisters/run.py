#! /bin/python3

import RPi.GPIO as GPIO
import time
import sys

low        = False
high       = True
A          = -1
SHIFT_CLK  = -1
RESET      = -1
LATCH_CLK  = -1
OUT_ENA    = -1

def output():
    print('Print contents of register here')


    PIN_NUMBERING = 'GPIO.BCM  ' if PIN_NUMBERING == GPIO.BCM else 'GPIO.BOARD'
    print('RPi pin      \t\t74HC595 pin')
    print('====================================')
    print(f'{SHIFT_CLK:03d}, {PIN_NUMBERING}\t\t11')
    print(f'{A:03d}, {PIN_NUMBERING}\t\t14')
    print(f'{RESET:03d}, {PIN_NUMBERING}\t\t10')
    print(f'{LATCH_CLOCK:03d}, {PIN_NUMBERING}\t\t12')
    print(f'{OUT_ENA:03d}, {PIN_NUMBERING}\t\t13')


def shift(value, quiet=True):
    try:
        value = int(value)

        # Enable output
        GPIO.output(OUT_ENA, low)

        # Tie reset to disabled
        GPIO.output(RESET, high)

        # Write value to A that will be shifted in
        GPIO.output(A, value)

        # Pulse Shift Clock to shift data into the register
        pulse(SHIFT_CLK, low)

        # Latch shift register
        GPIO.output(LATCH_CLK, low)
        pulse(LATCH_CLK, high)

        if not quiet:
            print(f'Wrote {value}')
    except ValueError:
        print('!!! Please provide valid inut')


def reset():
    # Reset shift register
    GPIO.output(RESET, low)

    # Latch the shift register contents
    pulse(pin=LATCH_CLK, value=low)

    # Enable output
    GPIO.output(OUT_ENA, low)


def pulse(pin, value):
    GPIO.output(pin, value)
    GPIO.output(pin, not value)


def init(quiet=False):
    # Choose direction and default value for SHIFT_CLK
    GPIO.setup(SHIFT_CLK, GPIO.OUT)
    # GPIO.output(SHIFT_CLK, low)

    # Choose direction and default value for A
    GPIO.setup(A, GPIO.OUT)
    GPIO.output(A, low)

    # Choose direction and default value for RESET
    GPIO.setup(RESET, GPIO.OUT)
    GPIO.output(RESET, high)

    # Choose direction and default value for LATCH_CLK
    GPIO.setup(LATCH_CLK, GPIO.OUT)
    GPIO.output(LATCH_CLK, high)

    # Choose direction and default value for OUT_ENA
    GPIO.setup(OUT_ENA, GPIO.OUT)
    GPIO.output(OUT_ENA, low)

    if not quiet:
        print(f'{name} is initialized')


if __name__ == "__main__":
    A             = 23 # GPIO
    SHIFT_CLK     = 24 # GPIO
    RESET         = 25 # GPIO
    LATCH_CLK     = 8  # GPIO
    OUT_ENA       = 7  # GPIO

    PIN_NUMBERING = GPIO.BCM

    name          = f'(74HC595) - {input("Name: ")}'

    GPIO.setwarnings(False)
    GPIO.setmode(PIN_NUMBERING)

    init()

    print('Resetting')
    reset()

    if len(sys.argv) == 1:
        # Interactive input
        try:
            while True:
                value = int(input("Input: "))
                shift(value)
        except KeyboardInterrupt:
            print()
            print('Exiting')
    else:
        # Command line input
        for WriteVal in sys.argv[1]:
            shift(WriteVal, quiet=False)
