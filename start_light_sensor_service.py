"""Starts the communication with light sensor"""

import sys
from com_gpio import ComGpio

if __name__ == "__main__":
    com = ComGpio(int(sys.argv[1])) # GPIO 4
    com.start_server()
