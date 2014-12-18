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
import lib.settings as libSettings
import lib.sensor as sensorTypes


settings = libSettings.settings()



print "hej"

# region Test information
#print ("burning: " + str(settings.BoilerBurningConfiguration))
import lib.test1 as bbb

print "thread init"
thTest = bbb.testThread(1,"test",1,settings)
thTest.start()
settings.threads.append(thTest)
#endregion

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
#settings.screenEnable = False




print "starting"

def shutDown():
    print "Application will now shutdown"
    print "Stop all running threads"
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
    for sensor in settings.sensors:
        print ("id: " + str(sensor.sensorId))
        print ("type: " + str(sensor.type))


    print "------------------"
    time.sleep(2)

# test



