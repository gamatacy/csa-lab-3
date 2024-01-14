class Register():

    def __init__(self):
        self.value = 0 

    def getValue(self) -> int:
        return self.value

    def setValue(self, value: int):
        self.value = value


class Memory():
    
    def __init__(self, size: int):
        self.memory = [0] * size

    def getValue(self, addr: int) -> int:
        return self.memory[addr]

    def setValue(self, addr: int, value: int):
        pass

