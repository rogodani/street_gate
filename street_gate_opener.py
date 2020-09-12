import configparser
import RPi.GPIO as GPIO
from time import sleep

class StreetGateOpener:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.gate_gpio = self.config['DEFAULT']['GateGpio']
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gate_gpio, GPIO.OUT)

    def open_gate(self):
        GPIO.output(self.gate_gpio, GPIO.LOW)
        sleep(2)
        GPIO.output(self.shelf1, GPIO.HIGH)


if __name__ == '__main__':
    x = StreetGateOpener()
    print(x.config['DEFAULT']['GateGpio'])
    x.gate_gpio


