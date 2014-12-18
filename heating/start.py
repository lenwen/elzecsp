#   elzECSp
#   Home Heating system
#
#   Build for Raspberry Pi B+

class version:
    Main = 0
    Release = 0
    Build = 1



#   Imported statements
import RPi.GPIO as GPIO
import wiringpi2
import atexit
import cPickle as pickle
import errno
import fnmatch
import io
import os
import pygame
import threading
import signal
import sys
import time
import datetime
import Adafruit_DHT
from pygame.locals import *
from subprocess import call
from flask import *
from multiprocessing import Process
import glob
import sqlite3 as dblite
from cgitb import text
from __builtin__ import str, int
from warnings import catch_warnings
from _ast import Str

from .lib.settings import settings # as ClassSettings
from .lib.sensors import * # SensorDht as ClassSensorDht, SensorDs18b20 as ClassSensorDs18b20, SensorUltrasonicHcSr04 as ClassSensorHcSr04


# region Args
#   args init relays GRIO
relayGPIO_args = { 1: 12,
        		2: 16,
				3: 20,
                4: 21}

#   args init DhtSensors from Adafruit
sensor_args = { 'dht11': Adafruit_DHT.DHT11,
        		'dht22': Adafruit_DHT.DHT22,
				'dht2302': Adafruit_DHT.AM2302 }
# endregion


#settings = ClassSettings()
settings.screenEnable = False




print "starting"

def shutDown():
    print "Application will now shutdown"
    print "Stop all runnings threads"
    for t in settings.threads:
        print(str(t.getName()) + ' will now stop()')
        t.stop()
    print "Wait 5 sec for threads to end"
    print "Threads are joining before exit"
    for t in settings.threads:
        t.join()
    print "GPIO cleanup"
    GPIO.cleanup()
    print "Application is ready to exit"
    # if boxDoRestart:
    #     os.system('sudo reboot')
    sys.exit(0)

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    shutDown()

#   Allow CTRL + c to shutdown the system
signal.signal(signal.SIGINT, signal_handler)

while(True):
    print "Data in main tread"
    print str(settings.screenEnable)
    print "------------------"

# test


