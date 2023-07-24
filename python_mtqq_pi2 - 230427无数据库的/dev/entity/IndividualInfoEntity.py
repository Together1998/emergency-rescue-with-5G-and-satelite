class IndividualInfoEntity:
    personId: str
    personName: str
    personGender: int
    personAge: int
    personBloodType: str
    personEmergencyContactName: str
    personEmergencyContactNumber: str
    personPmh: str
    personAllergies: str
    injuryTime: str
    injuryAddress: str
    injuryType: str
    injuryParts: str
    injurySpecialCase: str
    injuryClassification: str
    cabinType: int
    cabinID_w: int
    timestamp: str

    def __init__(self, var1, var2, var3, var4, var5, var6, var7, var8, var9,var10,var11,var12,var13,var14,var15,var16,var17,var18):
        self.personId = var1
        self.personName = var2
        self.personGender = var3
        self.personAge = var4
        self.personBloodType = var5
        self.personEmergencyContactName = var6
        self.personEmergencyContactNumber = var7
        self.personPmh = var8
        self.personAllergies = var9
        self.injuryTime = var10
        self.injuryAddress = var11
        self.injuryType = var12
        self.injuryParts = var13
        self.injurySpecialCase = var14
        self.injuryClassification = var15
        self.cabinType = var16
        self.cabinID_w = var17
        self.timestamp = var18
