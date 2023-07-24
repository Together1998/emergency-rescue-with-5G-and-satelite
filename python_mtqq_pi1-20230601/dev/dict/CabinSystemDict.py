class CabinSystemDict:
    pkgNum: int
    cabinType: int
    cabinId: int
    cabinAltitude: float
    cabinVbat: float
    cabinInsideO2: float
    cabinInsideTemperature: float
    cabinInterStress: float
    timestamp: str

    def __init__(self, d):
        self.__dict__ = d  # 将属性传给构建的字典


