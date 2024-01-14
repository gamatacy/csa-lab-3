class MicroCode:

    def getMicroCode(self) -> int:
        pass


class OperationMicroCode(MicroCode):

    def __init__(self, value: int):
        self.value = value & 0x00007FFF

    def getMicroCode(self) -> int:
        return self.value
    
class ControlMicroCode(MicroCode):

    def __init__(self, value: int):
        self.value = value & 0x0000FFFF

    def getMicroCode(self) -> int:
        return self.value
    

