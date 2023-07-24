class RespModuleInfoEntity:
    bMode: str
    bState: str
    bO2_11: int
    bVte: int
    bPmb: float
    bPeepPmb: float
    bHz: int
    bFztql: float
    bTinsp: float
    bPeak: float
    bPlatform: float
    bAvg: float
    cabinID: int
    cabinType: int

    def __init__(self, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14):
        self.bMode = var1
        self.bState = var2
        self.bO2_11 = var3
        self.bVte = var4
        self.bPmb = var5
        self.bPeepPmb = var6
        self.bHz = var7
        self.bFztql = var8
        self.bTinsp = var9
        self.bPeak = var10
        self.bPlatform = var11
        self.bAvg = var12
        self.cabinID = var13
        self.cabinType = var14
