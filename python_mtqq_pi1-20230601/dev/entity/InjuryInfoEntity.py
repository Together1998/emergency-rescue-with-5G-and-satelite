class InjuryInfoEntity:
    injuryTime: str
    injuryAddress: str
    injuryType: str
    injuryParts: str
    injurySpecialCase: str
    injuryClassification: str

    def __init__(self, var1, var2, var3, var4, var5, var6):
        self.injuryTime = var1
        self.injuryAddress = var2
        self.injuryType = var3
        self.injuryParts = var4
        self.injurySpecialCase = var5
        self.injuryClassification = var6
