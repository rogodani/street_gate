import configparser
import RPi.GPIO as GPIO
from time import sleep

class StreetGateOpener:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.gate_gpio = int(self.config['DEFAULT']['GateGpio'])
        self.phone_book = self.config['access']['PhoneNumbers'].split(',')
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gate_gpio, GPIO.OUT)

    def phone_number_validation(self, number):
        return number[-11:-1] in self.phone_book

    def open_gate(self):
        GPIO.output(self.gate_gpio, GPIO.LOW)
        sleep(2)
        GPIO.output(self.gate_gpio, GPIO.HIGH)
        sleep(2)
        GPIO.cleanup()



if __name__ == '__main__':
    x = StreetGateOpener()
    x.open_gate()


