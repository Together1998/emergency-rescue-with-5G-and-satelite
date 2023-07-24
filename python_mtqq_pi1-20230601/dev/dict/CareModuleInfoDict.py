class CareModuleInfoDict:
    pkgNum: int
    ecgI: float
    ecgIi: float
    ecgIii: float
    ecgAvr: float
    ecgAvl: float
    ecgAvf: float
    ecgV1: float
    ecgV2: float
    ecgV3: float
    ecgV4: float
    ecgV5: float
    ecgV6: float
    respWave: float
    respRate: int
    heartRate: int
    cabinType: int
    cabinId: int
    timestamp: str

    def __init__(self, d):
        self.__dict__ = d
