import RPi.GPIO as GPIO

_low  = False
_high = True

class SR_74HC595:
    def __init__(self, name, a, shift_clk, reset, latch_clk, output_ena, use_board_nums=True):
        self.name          = f'{name} (74HC595)'
        self.PIN_NUMBERING = GPIO.BOARD if use_board_nums else GPIO.BCM
        self.A             = a
        self.SHIFT_CLK     = shift_clk
        self.RESET         = reset
        self.LATCH_CLK     = latch_clk
        self.OUTPUT_ENA    = output_ena
    
        GPIO.setwarnings(False)
        GPIO.setmode(self.PIN_NUMBERING)

        # Choose direction and default value for A
        GPIO.setup(self.A, GPIO.OUT)
        GPIO.output(self.A, _low)

        # Choose direction and default value for SHIFT_CLK
        GPIO.setup(self.SHIFT_CLK, GPIO.OUT)

        # Choose direction and default value for RESET
        GPIO.setup(self.RESET, GPIO.OUT)
        GPIO.output(self.RESET, _high)

        # Choose direction and default value for LATCH_CLK
        GPIO.setup(self.LATCH_CLK, GPIO.OUT)
        GPIO.output(self.LATCH_CLK, _high)

        # Choose direction and default value for OUTPUT_ENA
        GPIO.setup(self.OUTPUT_ENA, GPIO.OUT)
        GPIO.output(self.OUTPUT_ENA, _low)

        self.reset()
        print(f'{self.name}: Reset')

        print(f'{self.name}: Initialized')


    def output(self):
        PinMode = "GPIO.BOARD" if self.PIN_NUMBERING == GPIO.BOARD else "GPIO.BCM"

        print()
        print(f'=== {self.name} pin configuration ===')
        print(f'{PinMode} pin numbering mode')
        print()
        print("RPi pin\t\t74HC595 pin")
        print("===========================")
        print(f'{self.A:02d}     \t\t14')
        print(f'{self.SHIFT_CLK:02d}     \t\t11')
        print(f'{self.RESET:02d}     \t\t10')
        print(f'{self.LATCH_CLK:02d}     \t\t12')
        print(f'{self.OUTPUT_ENA:02d}     \t\t13')
        print()

#        InputOutputString = ""
#        print()
#        print('Register contents')
#        print('=================')
#        for i in range(InputQueue.qsize()):
#            InputOutputString += f'{InputQueue.get_nowait()} '

#        print(InputOutputString)
#        print()


    def pulse(self, pin, value):
        GPIO.output(pin, value)
        GPIO.output(pin, not value)


    def reset(self):
        # Reset shift register
        GPIO.output(self.RESET, _low)

        # Latch the shift register contents
        self.pulse(pin=self.LATCH_CLK, value=_low)

        # Enable output
        GPIO.output(self.OUTPUT_ENA, _low)


    def shift(self, value, quiet=True):
        try:
            # Make input value an integer
            value = int(value)

            # Boolean-ize input
            value = int(value == True)

            # Enable output
            GPIO.output(self.OUTPUT_ENA, _low)

            # Tie reset to disabled
            GPIO.output(self.RESET, _high)

            # Write value to A that will be shifted in
            GPIO.output(self.A, value)

            # Pulse Shift Clock to shift data into the register
            self.pulse(self.SHIFT_CLK, _low)

            # Latch shift register
            GPIO.output(self.LATCH_CLK, _low)
            self.pulse(self.LATCH_CLK, _high)

#            try:
#                InputQueue.put_nowait(value)
#            except Full:
#                InputQueue.get_nowait()
#                InputQueue.put_nowait(value)

            if not quiet:
                print(f'Wrote {value}')
        except ValueError:
            print('!!! Please provide valid input')
