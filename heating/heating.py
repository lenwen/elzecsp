#   elzECSp
#   Home Heating system
#
#   Build for Raspberry Pi B+
vMain = 0
vRelease = 0
vBuild = 1

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


#   args init relays GRIO
relayGPIO_args = { 1: 12,
        		2: 16,
				3: 20,
                4: 21}

#   args init DhtSensors from Adafruit
sensor_args = { 'dht11': Adafruit_DHT.DHT11,
        		'dht22': Adafruit_DHT.DHT22,
				'dht2302': Adafruit_DHT.AM2302 }



class settings:
    circulationPumps = []
    sensors = []
    threads = []
    screenEnable = True

print "starting"




# test
