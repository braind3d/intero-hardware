import RPi.GPIO as GPIO
from pi74HC595 import pi74HC595

# Display pins
SDI   = 17
RCLK  = 18
SRCLK = 27

digit_selection_pins = (5, 20, 21, 6)

# Constants
CODE_LEN = 4
SHIFT_REG_LEN = 8

#  Shoud come from server conn/socket
identification_code = 136

# general utils
def display_gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    for i in digit_selection_pins:
        GPIO.setup(i, GPIO.OUT)

def destroy():
    GPIO.cleanup()

def clearDisplay():
    for i in range(SHIFT_REG_LEN):
        GPIO.output(SDI, GPIO.HIGH)
        GPIO.output(SRCLK, GPIO.HIGH)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.LOW)    


def parse_verification_code(code):
    four_digit_code = '{:04d}'.format(code)
    return [int(digit) for digit in four_digit_code]

def pickDigit(digit):
    for bit in digit_selection_pins:
        GPIO.output(bit,GPIO.LOW)
    GPIO.output(digit_selection_pins[digit], GPIO.HIGH)

def display_digit(digit):
    for bit in range(SHIFT_REG_LEN):
        GPIO.output(SDI, 0x80 & (digit << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.LOW)


def display_verification_code(identification_code):
    identification_code_array = parse_verification_code(identification_code)
    while True:
        for i in range (CODE_LEN):
            clearDisplay() 
            pickDigit(i)
            display_digit(identification_code_array[i])

if __name__ == '__main__':
    display_gpio_setup()
    shift_register = pi74HC595(SDI, RCLK, SRCLK)
    lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=21, pin_e=20, pins_data=[5, 6, 13, 19])
    try:
        display_verification_code(identification_code)
    except KeyboardInterrupt:
        destroy()
