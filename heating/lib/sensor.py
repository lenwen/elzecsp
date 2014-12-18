
class SensorDht(object):
    def __init__(self, sensorId = None, activated = None, type=None, boxGpio=None, checkIntervale=None, logIntervale=None, name=None, info=None,status=None):
        self.sensorId = sensorId
        self.activated = activated
        self.type = type            #dht11      dht22       dht2302
        self.boxGpio = boxGpio
        self.checkInterval = checkIntervale
        self.logInterval = logIntervale
        self.Temperature = 0
        self.humidity = 0
        self.lastCheck = 0
        self.lastLog = 0
        self.name = name
        self.info = info
        self.status = status

class SensorDs18b20(object):
    def __init__(self, sensorId = None, activated = None, type=None, connectedTo=None, romId=None, checkIntervale=None, logIntervale=None, name=None, info=None,status=None):
        self.sensorId = sensorId
        self.activated = activated
        self.type = type        #ds18b20
        self.connectedTo = connectedTo
        self.romId = romId
        self.health = 0
        self.checkIntervale = checkIntervale
        self.logIntervale = logIntervale
        self.Temperature = 0
        self.lastCheck = 0
        self.lastLog = 0
        self.name = name
        self.info = info
        self.status = status

class SensorUltrasonicHcSr04(object):
    def __init__(self, sensorId = None, activated = None, type=None, boxGpioTriger=None, boxGpioEcho=None, checkIntervale=None, logIntervale=None, name=None, info=None,status=None):
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
        self.name = name
        self.info = info
        self.status = status

class SensorMall(object):
    def __init__(self, sensorId = None, activated = None, type=None, name=None, info=None,status=None):
        self.sensorId = sensorId
        self.activated = activated
        self.type = type
        self.name = name
        self.info = info
        self.status = status







