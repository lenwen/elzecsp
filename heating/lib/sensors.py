class SensorDht(object):
    def __init__(self, sensorId = None, activated = None, type=None, boxGpio=None, checkIntervale=None, logIntervale=None):
        self.sensorId = sensorId
        self.activated = activated
        self.type = type            #dht11      dht22       dht2302
        self.boxGpio = boxGpio
        self.checkIntervale = checkIntervale
        self.logIntervale = logIntervale
        self.Temperature = 0
        self.humidity = 0
        self.lastCheck = 0
        self.lastLog = 0

class SensorDs18b20(object):
    def __init__(self, sensorId = None, activated = None, type=None):
        self.sensorId = sensorId
        self.activated = activated
        self.type = type

class SensorUltrasonicHcSr04(object):
    def __init__(self, sensorId = None, activated = None, type=None, boxGpioTriger=None, boxGpioEcho=None, checkIntervale=None, logIntervale=None):
        self.sensorId = sensorId
        self.activated = activated
        self.type = type        #   hcsr04
        self.boxGpioTriger = boxGpioTriger
        self.boxGpioEcho = boxGpioEcho
        self.checkIntervale = checkIntervale
        self.logIntervale = logIntervale
        self.value = 0
        self.value2 = 0
        self.lastCheck = 0
        self.lastLog = 0

class SensorMall(object):
    def __init__(self, sensorId = None, activated = None, type=None):
        self.sensorId = sensorId
        self.activated = activated
        self.type = type





