class ExitCommandDict:
    cabinId: int
    cabinType:int
    timestamp: str
    flag: int

    def __init__(self, d):
        self.__dict__ = d  # 将属性传给构建的字典