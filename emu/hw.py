class Register:

    def __init__(self, value = 0):
        self.value: int = value

    def getValue(self) -> int:
        return self.value

    def setValue(self, value: int):
        self.value = value

    def inc(self):
        self.value += 1

class Memory:

    def __init__(self, size: int):
        self.memory: [int] = [0] * size

    def getValue(self, addr: int) -> int:
        if addr < 0:
            addr = len(self.memory) - 1 + addr
        return self.memory[addr]

    def setValue(self, addr: int, value: int):
        if addr < 0:
            addr = len(self.memory) - 1 + addr
        self.memory[addr] = value
