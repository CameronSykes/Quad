#! /bin/python3

import RPi.GPIO as GPIO
import time

def output():
    print('Print contents of register here')


    PIN_NUMBERING = 'GPIO.BCM  ' if PIN_NUMBERING == GPIO.BCM else 'GPIO.BOARD'
    print('RPi pin      \t\t74HC595 pin')
    print('====================================')
    print(f'{SHIFT_CLK:03d}, {PIN_NUMBERING}\t\t11')
    print(f'{A:03d}, {PIN_NUMBERING}\t\t14')
    print(f'{RESET:03d}, {PIN_NUMBERING}\t\t10')


def shift(value):
    # Write value to A that will be shifted in
    GPIO.output(A, value)

    # Pulse pin 11 (Shift Clock) to shift data into the register
    GPIO.output(SHIFT_CLK, True)
    GPIO.output(SHIFT_CLK, False)


if __name__ == "__main__":
    name          = f'({input("Name: ")}) - 74HC595'
    A             = 23 # GPIO
    SHIFT_CLK     = 24 # GPIO
    RESET         = 25 # GPIO
    PIN_NUMBERING = GPIO.BCM
    NUM_BLINKS    = 20

    GPIO.setwarnings(False)
    GPIO.setmode(PIN_NUMBERING)

    # Choose direction and default value for SHIFT_CLK
    GPIO.setup(SHIFT_CLK, GPIO.OUT)
    GPIO.output(SHIFT_CLK, False)

    # Choose direction and default value for A
    GPIO.setup(A, GPIO.OUT)
    GPIO.output(A, False)

    # Choose direction and default value for RESET
    GPIO.setup(RESET, GPIO.OUT)
    GPIO.output(RESET, True)

    print(f'{name} is initialized')

    for WriteVal in range(NUM_BLINKS):
        print(f'Writing: {WriteVal % 2}')
        shift(WriteVal % 2)
        time.sleep(2)

        if WriteVal > 7:
            print(f'Expected Output: {(WriteVal - 8) % 2}')
