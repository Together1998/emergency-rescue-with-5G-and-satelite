class OxygenProductionSystemDict:
    pkgNum: int
    cabinType: int
    cabinId: int
    opsState: int
    opsLevel: int
    opsO2Percent: float
    opsError: int
    timestamp: str

    def __init__(self, d):
        self.__dict__ = d
