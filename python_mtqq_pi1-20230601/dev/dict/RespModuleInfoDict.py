class RespModuleInfoDict:
    pkgNum: int
    cabinType: int
    cabinId: int
    bMode: str
    bState: str
    bO2_11: int
    bVte: int
    bPmb: float
    bPeepPmb: float
    bHz: int
    bFztql: float
    bTinsp: float
    bPeak: float
    bPlatform: float
    bAvg: float
    timestamp: str

    def __init__(self, d):
        self.__dict__ = d
