#! /bin/python3

import RPi.GPIO as GPIO
import time
import sys
from queue import Queue

low        = False
high       = True
A          = -1
SHIFT_CLK  = -1
RESET      = -1
LATCH_CLK  = -1
OUT_ENA    = -1
InputQueue = Queue(maxsize=8)

def output():
    InputOutputString = ""
    print()
    print('Register contents')
    print('=================')
    for i in range(InputQueue.qsize()):
        InputOutputString += f'{InputQueue.get_nowait()} '

    print(InputOutputString)
    print()


#    PIN_NUMBERING = 'GPIO.BCM  ' if PIN_NUMBERING == GPIO.BCM else 'GPIO.BOARD'
#    print('RPi pin      \t\t74HC595 pin')
#    print('====================================')
#    print(f'{SHIFT_CLK:03d}, {PIN_NUMBERING}\t\t11')
#    print(f'{A:03d}, {PIN_NUMBERING}\t\t14')
#    print(f'{RESET:03d}, {PIN_NUMBERING}\t\t10')
#    print(f'{LATCH_CLOCK:03d}, {PIN_NUMBERING}\t\t12')
#    print(f'{OUT_ENA:03d}, {PIN_NUMBERING}\t\t13')


if __name__ == "__main__":
    A             = 23 # GPIO
    SHIFT_CLK     = 24 # GPIO
    RESET         = 25 # GPIO
    LATCH_CLK     = 8  # GPIO
    OUT_ENA       = 7  # GPIO

    PIN_NUMBERING = GPIO.BCM

    name          = f'(74HC595) - {input("Name: ")}'
    LoopCount     = 0

    try:
        if len(sys.argv) == 1:
            # Interactive input
            while True:
                if LoopCount % 8 == 0 and LoopCount != 0:
                    output()
                else:
                    value = int(input("Input: "))
                    shift(value)

                LoopCount += 1
        else:
            # Command line input
            for Position, WriteVal in enumerate(sys.argv[1]):
                shift(WriteVal)

                if Position % 7 == 0 and Position != 0:
                    output()
    except KeyboardInterrupt:
        print()
        print('Exiting')
