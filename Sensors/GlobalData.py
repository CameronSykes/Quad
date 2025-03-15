class RunStates(Enum):
    RESERVED = 0 # No sensor has been assigned for this slot yet
    INIT     = 1 # A sensor has been assigned for this slot but isn't running
    RUN      = 2 # A sensor is actively collecting information
    STOP     = 3 # A sensor is still active but not collecting information
    EXIT     = 4 # The sensor is to be decommisioned


NUM_SENSORS = 2


global AppRunStates = [RunStates.RESERVED for sensor in range(NUM_SENSORS)]
