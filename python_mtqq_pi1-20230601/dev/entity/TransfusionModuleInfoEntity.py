class TransfusionModuleInfoEntity:
    iState: str
    iMode: str
    iSpeed: int
    cabinID: int
    cabinType: int

    def __init__(self, var1, var2, var3,var4,var5):
        self.iState = var1
        self.iMode = var2
        self.iSpeed = var3
        self.cabinID = var4
        self.cabinType = var5