class ALU:

    def __init__(self):
        self.lop: int = 0
        self.rop: int = 0
        self.out: int = 0

        self.z: int = 0
        self.n: int = 0
        self.c: int = 0
        self.v: int = 0

    def setLeftOperand(self, op: int):
        self.lop = op

    def setRightOperand(self, op: int):
        self.rop = op

    def getOutput(self) -> int:
        return self.out

    def invLeftOperand(self):
        self.lop = ~self.lop

    def invRightOperand(self):
        self.rop = ~self.rop

    def sum(self):
        self.out = 0
        self.out = self.lop + self.rop

    def inc(self):
        self.out += 1

    def conjuction(self):
        self.out = 0
        self.out = self.lop & self.rop

    def shlt(self):
        self.c = self.out & 0x8000
        self.out = self.out << 1

    def shrt(self):
        self.c = self.out & 0x0001
        self.out = self.out >> 1

    def getZ(self) -> int:
        self.z = 1 if self.out == 0 else 0
        return self.z

    def getN(self) -> int:
        self.n = 1 if self.out & 0x8000 != 0 else 0
        return self.n

    def getC(self) -> int:
        self.c = 1 if self.out & 0x10000 != 0 else 0
        return self.c

    def getV(self) -> int:
        self.v = (self.out & 0x10000) >> 16 ^ (self.out & 0x4000) >> 12
        return self.v

    def _2lb(self):
        self.out = self.out & 0xFFFF
