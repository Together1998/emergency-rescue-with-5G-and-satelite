class CareModuleInfoEntity:
    ecgI: float
    ecgIi: float
    ecgIii: float
    ecgAvr: float
    ecgAvl: float
    ecgAvf: float
    ecgV1: float
    ecgV2: float
    ecgV3: float
    ecgV4: float
    ecgV5: float
    ecgV6: float
    respWave: float
    respRate: int
    heartRate: int
    cabinID: int
    cabinType: int

    def __init__(self, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15,var16,var17):
        self.ecgI = var1
        self.ecgIi = var2
        self.ecgIii = var3
        self.ecgAvr = var4
        self.ecgAvl = var5
        self.ecgAvf = var6
        self.ecgV1 = var7
        self.ecgV2 = var8
        self.ecgV3 = var9
        self.ecgV4 = var10
        self.ecgV5 = var11
        self.ecgV6 = var12
        self.respWave = var13
        self.respRate = var14
        self.heartRate = var15
        self.cabinID = var16
        self.cabinType = var17
