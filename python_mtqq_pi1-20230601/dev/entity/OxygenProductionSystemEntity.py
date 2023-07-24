class OxygenProductionSystemEntity:
    opsState: int
    opsLevel: int
    opsO2Percent: float
    opsError: int
    cabinID: int
    cabinType: int

    def __init__(self, var1, var2, var3, var4,var5,var6):
        self.opsState = var1
        self.opsLevel = var2
        self.opsO2Percent = var3
        self.opsError = var4
        self.cabinID = var5
        self.cabinType = var6