import sys
from hello import *
import time 
import random

if __name__ == "__main__":
    getPort()
    setDevice1(True)
    setDevice2(True)
    test_temp = readTemperature()
    test_mois = readMoisture()
    print('Temperature and Moisture value is:', test_temp, '\n', test_mois)