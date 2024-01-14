from hw import *
from alu import ALU

class DataPath:

    def __init__(self):

        #alu
        self.alu: ALU = ALU()

        #mem
        self.instructionMemoryL: Memory = Memory(2048)
        self.dataMemory: Memory = Memory(2048)

        #regs
        #lalu
        self.AC: Register = Register()
        self.BR: Register = Register()
        self.IR: Register = Register()
        self.IAR: Register = Register()

        #ralu
        self.DR: Register = Register()
        self.PS: Register = Register()
        self.SP: Register = Register()

        self.AR: Register = Register()

        self.mappedRegister: [Register] = [
                self.DR,
                self.SP,
                self.PS,
                self.AR,
                self.AC,
                self.BR,
                self.IAR
        ]
        
