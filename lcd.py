import RPi.GPIO as GPIO
from RPLCD import CharLCD

#  Shoud come from server conn/socket
identification_code = 136

# general utils
def display_gpio_setup():
    GPIO.setmode(GPIO.BCM)

def destroy():
    GPIO.cleanup()

def parse_verification_code(code):
    four_digit_code = '{:04d}'.format(code)
    a = [int(digit) for digit in four_digit_code]
    return four_digit_code

def pickDigit(digit):
    for bit in digit_selection_pins:
        GPIO.output(bit,GPIO.LOW)
    GPIO.output(digit_selection_pins[digit], GPIO.HIGH)

def display_verification_code(identification_code):
    identification_code_array = parse_verification_code(identification_code)
    while True:
        lcd.cursor_pos = (0, 6) 
        lcd.write_string(identification_code_array)

if __name__ == '__main__':
    display_gpio_setup()
    lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=21, pin_e=20, pins_data=[5, 6, 13, 19])
    try:
        display_verification_code(identification_code)
    except KeyboardInterrupt:
        destroy()
