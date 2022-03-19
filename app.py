import time
import RPi.GPIO as GPIO

# Display pins
SDI   = 17
RCLK  = 18
SRCLK = 27

# Constants
CODE_LEN = 4

identification_code = 2

# Functions to control display
def separate_four_digits(code):
    four_digit_code = '{:04d}'.format(code)
    return [int(digit) for digit in str(four_digit_code)]

def parse_verification_code(digit_array):
    hex_string = list()
    for digit in CODE_LEN:
        hex_string.append('0x{:02x}'.format(hex_string(digit)))
    return hex_string

def display_digit(digit):
    for bit in range(0, 8):
		GPIO.output(SDI, 0x80 & (digit << bit))
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.001)
		GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

def display_gpio_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(SDI, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(RCLK, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(SRCLK, GPIO.OUT, initial=GPIO.LOW)

def display_verification_code():
    identification_code_array = parse_verification_code(separate_four_digits(identification_code))
    for digit in identification_code_array:
        display_digit(digit)
        time.sleep(0.5)

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	display_gpio_setup()
	try:
		print(separate_four_digits(identification_code))
	except KeyboardInterrupt:
		destroy()
