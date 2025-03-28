#! /bin/python3

import RPi.GPIO as GPIO
import time
import sys
from SR_74HC595.SR_74HC595 import SR_74HC595

if __name__ == "__main__":
    # Instantiate shift register
    ShiftReg1 = SR_74HC595(name="Shift Register 1", a=23, shift_clk=24, reset=25, latch_clk=8, output_ena=7, use_board_nums=False)
    ShiftReg1.output()

    try:
        if len(sys.argv) == 1:
            # Interactive input
            while True:
                value = int(input("Input: "))
                ShiftReg1.shift(value)
        else:
            pass
            # Command line input
            for WriteVal in sys.argv[1]:
                ShiftReg1.shift(WriteVal)
    except KeyboardInterrupt:
        print()
        print('Exiting')
