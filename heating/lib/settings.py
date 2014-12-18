class settings:
    circulationPumps = []
    sensors = []
    threads = []
    burningConfigurations = []

    #   Folder configuration for installation
    PathCore = '/home/pi/elzecsp/'
    Pathicon = PathCore + 'icons'
    PathOneWireA = '/sys/bus/w1/devices/'
    PathDb =  PathCore + 'ecs.db'

    #   OneWire GPO configuration
    oneWireCrcWaitingTime = 30


    screenEnable = False

    #   Boiler Configurations
    BoilerBurningConfigurationRunning = 2
    BoilerBurningIsOn = False
    BoilerBurningModeAuto = False

    #   Debug settings
    BoxDebug = True
    BoxDebugFile = 'debug.log'



