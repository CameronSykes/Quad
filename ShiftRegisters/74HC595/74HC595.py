import RPi.GPIO as GPIO

_low  = False
_high = True

class 74HC595:
    def __init__(self, name, use_board_nums=True, a, shift_clk, reset, latch_clk, output_ena):
        self.name          = f'(74HC595) - {name}'
        self.PIN_NUMBERING = GPIO.BOARD if use_board_nums else GPIO.BCM
        self.A             = a
        self.SHIFT_CLK     = shift_clk
        self.RESET         = reset
        self.LATCH_CLK     = latch_clk
        self.OUTPUT_ENA    = output_ena
    
        GPIO.setwarnings(False)
        GPIO.setmode(self.PIN_NUMBERING)

        # Choose direction and default value for A
        GPIO.setup(A, GPIO.OUT)
        GPIO.output(A, low)

        # Choose direction and default value for SHIFT_CLK
        GPIO.setup(SHIFT_CLK, GPIO.OUT)

        # Choose direction and default value for RESET
        GPIO.setup(RESET, GPIO.OUT)
        GPIO.output(RESET, high)

        # Choose direction and default value for LATCH_CLK
        GPIO.setup(LATCH_CLK, GPIO.OUT)
        GPIO.output(LATCH_CLK, high)

        # Choose direction and default value for OUT_ENA
        GPIO.setup(OUT_ENA, GPIO.OUT)
        GPIO.output(OUT_ENA, low)

        print(f'{name} is initialized')

        print(f'Resetting {name}')
        self.reset()

    def __str__(self):
        print('Print contents of register here')
        print(f'Primary pin #{self.primaryShiftClock} ==> ShiftClock, pin 11')
        print(f'Primary pin #{self.primary_A} ==> A, pin 14')


    def pulse(pin, value):
        GPIO.output(pin, value)
        GPIO.output(pin, not value)


    def shift(self, value):
        # Write value to pin 14 (A) that will be shifted in
        GPIO.output(self.A, value)

        # Pulse pin 11 (Shift Clock) to shift data into the register
       GPIO.output(self.SHIFT_CLK, True)
       GPIO.output(self.SHIFT_CLK, False)
