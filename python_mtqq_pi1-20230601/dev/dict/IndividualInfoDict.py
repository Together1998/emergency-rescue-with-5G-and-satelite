class IndividualInfoDict:
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
    cabinID_w: int
    cabinType: int
    hospitalInfor:str
    timestamp: str

    def __init__(self, d):
        self.__dict__ = d
