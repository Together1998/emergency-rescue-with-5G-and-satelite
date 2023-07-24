class Co2ModuleInfoEntity:
    co2Curve: float
    co2Etco2: float
    ICUID: int
    cabinID: int
    cabinType:int

    def __init__(self, var1, var2, var3, var4, var5):
        self.co2Curve = var1
        self.co2Etco2 = var2
        self.ICUID = var3
        self.cabinID = var4
        self.cabinType = var5