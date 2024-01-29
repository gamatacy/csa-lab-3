from hw import *
from alu import ALU

MEMORY_SIZE = 256

class DataPath:

    def __init__(self):

        #alu
        self.alu: ALU = ALU()

        #mem
        self.instructionMemory: Memory = Memory(MEMORY_SIZE)
        self.dataMemory: Memory = Memory(MEMORY_SIZE)

        #regs
        #lalu
        self.AC: Register = Register()
        self.BR: Register = Register()
        self.IR: Register = Register()
        self.IAR: Register = Register()

        #ralu
        self.DR: Register = Register()
        self.PS: Register = Register()
        self.SP: Register = Register(len(self.dataMemory.memory))

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

        self.buffers = {
            0x735 : ['a','b','c']
        }

    def getAcZ(self) -> int:
        return 1 if self.AC.getValue() == 0 else 0
    
    def getAcN(self) -> int:
        return 1 if self.AC.getValue() < 0 else 0 
    
    def readBuffer(self, port: int) -> int:
        return ord(self.buffers[port].pop())
    
    def writeBuffer(self, port: int, value: int):
        return self.buffers[port].append(chr(value))

    def log_registers(self):

        print("======================")

        print("\nLEFT REGS:")
        print(f"   AC: {hex(self.AC.getValue())}")
        print(f"   BR: {hex(self.BR.getValue())}")
        print(f"   IR: {hex(self.IR.getValue())}")
        print(f"   IAR: {hex(self.IAR.getValue())}")

        print("\nRIGHT REGS:")
        print(f"   DR: {hex(self.DR.getValue())}")
        print(f"   PS: {hex(self.PS.getValue())}")
        print(f"   SP: {hex(self.SP.getValue())}")
        print(f"   AR: {hex(self.AR.getValue())}")

        print("\BUFFER:")
        print(self.buffers[0x735])
        # print("\nDataMemory")
        # for i in range(len(self.dataMemory.memory)):
        #     print(f"   ADDR: {i} VALUE: ", end="")
        #     print(f"{hex(self.dataMemory.getValue(i))}")


