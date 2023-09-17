import sys
from hello import *
import time 
import random

if __name__ == "__main__":
    getPort()
    setDevice1(relay1_ON)
    setDevice2(relay2_ON)
    readTemperature()
    readMoisture()