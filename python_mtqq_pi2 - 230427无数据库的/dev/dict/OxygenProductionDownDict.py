class OxygenProductionDownDict:
    cabinId: int
    opsState: int
    opsLevel: int

    def __init__(self, d):
        self.__dict__ = d