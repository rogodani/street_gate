import RPi.GPIO as GPIO

NUMBERS = ("0743144113")
GATE_GPIO = 18


class StreetGateOpener:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GATE_GPIO, GPIO.OUT)

