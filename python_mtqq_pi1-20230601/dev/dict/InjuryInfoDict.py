class InjuryInfoDict:
    injuryTime: str
    injuryAddress: str
    injuryType: str
    injuryParts: str
    injurySpecialCase: str
    injuryClassification: str

    def __init__(self, d):
        self.__dict__ = d
