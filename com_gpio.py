"""Provides Raspberry Pi GPIO communication"""

import time
import Rpi.GPIO as GPIO
from com_cli import ComClient

class ComGpio:
    """Provides communication with GPIO"""

    def __init__(self, gpio_port):
        """Object ComGpio constructor

        Args:
            gpio_port (int): gpio number based on GPIO.BCM
        """
        GPIO.setmode(GPIO.BCM) # BCM is GPIO number not port
        GPIO.setwarnings(True)
        self.gpio_port = gpio_port
        GPIO.setup(self.gpio_port, GPIO.IN)
        self.first_lecture = not GPIO.input(self.gpio_port)
        self.com = ComClient()

    def start_server(self):
        """Starts a simple server that will communicate when
        the GPIO reports a change on first_lecture.
        while"""
        # TODO change this to a real service
        while True:
            lecture = GPIO.input(self.gpio_port)
            if lecture != self.first_lecture:
                if lecture: # is dark
                    self.communicate_change(lecture)
                    print('\u263e')
                else:
                    self.communicate_change(lecture)
                    print('\u263c')
            self.first_lecture = lecture
            time.sleep(0.1)

    def communicate_change(self, lecture):
        """Communicates the change of lecture"""
        # TODO change device hardcoded
        device = 'light-sensor-device'
        self.com.post_change(device, lecture)
