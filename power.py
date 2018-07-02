import RPi.GPIO as GPIO
from screen import Screen
import time


class Power(object):
    
    
    screen = Screen()
    last = ['bay bay !']
    
    def __init__(self, RESET=23, LED=18):
        self.PIN_LED = LED
        self.PIN_RESET = RESET
        MODE = GPIO.BCM
        GPIO.setmode(MODE)
        GPIO.setup(self.PIN_RESET,
                   GPIO.IN,
                   pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.PIN_LED, GPIO.OUT)
        
    def is_reset_down(self):
        if GPIO.input(self.PIN_RESET) != 0:
            return False
        time.sleep(.3)
        if GPIO.input(self.PIN_RESET) != 0:
            return False
        return True

    def is_reset_still_down(self):
        for i in range(10):
            if self.is_reset_down() is False:
                self.light_led()
                return False
            else:
                self.high_light_led()
        screen.display(last)
        return True
    
    def light_led(self):
        GPIO.output(self.PIN_LED, True)
        time.sleep(.2)
        GPIO.output(self.PIN_LED, False)
        time.sleep(.2)
        
    def high_light_led(self):
        print"led_test"
        GPIO.output(self.PIN_LED, False)

