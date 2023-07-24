class CabinSystemEntity:
    cabinType: int
    cabinId: int
    cabinAltitude: float
    cabinVbat: float
    cabinInsideO2: float
    cabinInsideTemperature: float
    cabinInterStress: float

    def __init__(self, var1, var2, var3, var4, var5, var6,var7):
        self.cabinType = var1
        self.cabinId = var2
        self.cabinAltitude = var3
        self.cabinVbat = var4
        self.cabinInsideO2 = var5
        self.cabinInsideTemperature = var6
        self.cabinInterStress = var7


