class ALU:

    def __init__(self):
        self.lop: int = 0
        self.rop: int = 0
        self.out: int = 0

        self.z: int = 0
        self.n: int = 0
        self.c: int = 0
        self.v: int = 0

    def set_left_operand(self, op: int):
        self.lop = op

    def set_right_operand(self, op: int):
        self.rop = op

    def get_output(self) -> int:
        return self.out

    def inv_left_operand(self):
        self.lop = ~self.lop

    def inv_right_operand(self):
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

    def get_z(self) -> int:
        self.z = 1 if self.out == 0 else 0
        return self.z

    def get_n(self) -> int:
        self.n = 1 if self.out & 0x8000 != 0 else 0
        return self.n

    def get_c(self) -> int:
        self.c = 1 if self.out & 0x10000 != 0 else 0
        return self.c

    def get_v(self) -> int:
        self.v = (self.out & 0x10000) >> 16 ^ (self.out & 0x4000) >> 12
        return self.v

    def _2lb(self):
        self.out = self.out & 0xFFFF
