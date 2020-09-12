import configparser
import RPi.GPIO as GPIO
from time import sleep

class StreetGateOpener:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.gate_gpio = int(self.config['DEFAULT']['GateGpio'])
        self.phone_book = self.config['access']['PhoneNumbers'].split(',')

    def phone_number_validation(self, number):
        print('PHONE BOOK: ', self.phone_book)
        print('NUMBER: ', number, "---", len(number), "------", number[-11:-1])
        return number[-11:-1] in self.phone_book

    def open_gate(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gate_gpio, GPIO.OUT)
        GPIO.output(self.gate_gpio, GPIO.LOW)
        sleep(2)
        GPIO.output(self.gate_gpio, GPIO.HIGH)
        sleep(2)
        GPIO.cleanup()



if __name__ == '__main__':
    x = StreetGateOpener()
    x.open_gate()


