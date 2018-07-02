import RPi.GPIO as GPIO
import time
import types

class KeyBoard(object):

    
    def __init__(self,
                 MENU=5,
                 DOWN=26,
                 UP=6,
                 ENTER=22):
        self.PIN_MENU = MENU
        self.PIN_DOWN = DOWN
        self.PIN_UP = UP
        self.PIN_ENTER = ENTER

        MODE = GPIO.BCM

        GPIO.setmode(MODE)

        GPIO.setup(self.PIN_MENU, GPIO.IN)
        GPIO.setup(self.PIN_DOWN, GPIO.IN)
        GPIO.setup(self.PIN_UP, GPIO.IN)
        GPIO.setup(self.PIN_ENTER, GPIO.IN)

    def get_key(self):
        menu = GPIO.input(self.PIN_MENU)
        up = GPIO.input(self.PIN_DOWN)
        down = GPIO.input(self.PIN_UP)
        enter = GPIO.input(self.PIN_ENTER)
        key_value = {'hasKey': False,
                     'value': None,
                     'state': None}
        if menu == 0 and up == 0 and down == 0 and enter == 0:
            pass
        
        elif menu == 1 and up == 0 and down == 0 and enter == 0:
            key_value['hasKey'] = True
            key_value['value'] = 'menu'
        
        elif menu == 0 and up == 1 and down == 0 and enter == 0:
            key_value['hasKey'] = True
            key_value['value'] = 'up'
          
        elif menu == 0 and up == 0 and down == 1 and enter == 0:
            key_value['hasKey'] = True
            key_value['value'] = 'down'
          
        elif menu == 0 and up == 0 and down == 0 and enter == 1:
            key_value['hasKey'] = True
            key_value['value'] = 'enter'
            
        else:
            pass
        
        return key_value
        
        
if __name__ == "__main__":
    e = KeyBoard(5, 6, 26, 22, 23)
    while True:
        time.sleep(1)
        val = e.get_key()
        print val
        
