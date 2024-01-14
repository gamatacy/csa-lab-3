from hw import *

class DataPath:

    def __init__(self):
        self.instructionMemory = Memory(2048)
        self.dataMemory = Memory(2048)

        #l
        self.AC = Register()
        self.BR = Register()
        self.IR = Register()
        self.IAR = Register()

        self.DR = Register()
        self.PS = Register()
        self.SP = Register()
        self.AR = Register()