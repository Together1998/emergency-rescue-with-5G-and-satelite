class SateliteInforDict:#具体内容待定
    pkgNum: int
    cabinType: int
    cabinId: int
    ICUID: int
    co2Curve: float
    co2Etco2: float
    timestamp: str

    def __init__(self, d):
        self.__dict__ = d