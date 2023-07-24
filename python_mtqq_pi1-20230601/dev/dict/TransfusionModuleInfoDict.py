class TransfusionModuleInfoDict:
    pkgNum: int
    cabinType: int
    cabinId: int
    iState: int
    iMode: int
    iSpeed: int
    timestamp: str

    def __init__(self, d):
        self.__dict__ = d
        pass