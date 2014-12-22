class settings:
    circulationPumps = []
    sensors = []
    threads = []
    burningConfigurations = []

    #   Folder configuration for installation
    PathCore = '/home/pi/elzecsp/'
    Pathicon = PathCore + 'icons'
    PathOneWireA = '/sys/bus/w1/devices/'


    #   OneWire GPO configuration
    oneWireCrcWaitingTime = 30


    screenEnable = False

    #   Boiler Configurations
    BoilerBurningConfigurationRunning = 2
    BoilerBurningIsOn = False
    BoilerBurningModeAuto = False

    #   Debug settings
    BoxDebug = True
    BoxDebugFile = PathCore + 'debug.log'

    #   Box restart values
    boxDoRestart = False

    #   Database Settings
    PathDb =  PathCore + 'ecs.db'
    dbVersionFromDatabase = 0




