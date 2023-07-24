class Co2ModuleInfoDict:
    pkgNum: int
    cabinType: int
    cabinId: int
    ICUID: int
    co2Curve: float
    co2Etco2: float
    h_temp1: float
    h_temp2: float
    h_bpressh: int
    h_bpressl: int
    h_bpressv: int
    timestamp: str

    def __init__(self, d):
        self.__dict__ = d