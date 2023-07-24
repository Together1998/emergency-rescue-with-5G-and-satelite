class EndEntity:
    cabinId: int
    cabinType: int
    timestamp: str
    flag: int

    def __init__(self, var1, var2, var3, var4):
        self.cabinId = var1
        self.cabinType = var2
        self.timestamp = var3
        self.flag = var4
