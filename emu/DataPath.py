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
        self.SP: Register = Register(2048)

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
            735 : ['a','b','c']
        }
        

        self.dump = open("emu.dump", "w")
        self.memdump = open("mem.dump", "w")

    def getAcZ(self) -> int:
        return 1 if self.AC.getValue() == 0 else 0
    
    def getAcN(self) -> int:
        return 1 if self.AC.getValue() < 0 else 0 
    
    def readBuffer(self, port: int) -> int:
        val = ord(self.buffers[port].pop())
        return val
    
    def writeBuffer(self, port: int, value: int):
        print(chr(value))
        return self.buffers[port].append(chr(value))

    def log_registers(self, instr,tick):

        
        self.dump.write("\n===================================\n")
        self.dump.write(f"================{instr}=================\n")
        self.dump.write("===================================\n")
        self.dump.write("LEFT REGS".ljust(20) + "RIGHT REGS\n")
        self.dump.write(f"AC: {hex(self.AC.getValue()).ljust(16)}DR: {hex(self.DR.getValue())}\n")
        self.dump.write(f"BR: {hex(self.BR.getValue()).ljust(16)}PS: {hex(self.PS.getValue())}\n")
        self.dump.write(f"IR: {hex(self.IR.getValue()).ljust(16)}SP: {hex(self.SP.getValue())}\n")
        self.dump.write(f"IAR: {hex(self.IAR.getValue()).ljust(15)}AR: {hex(self.AR.getValue())}\n")
        self.dump.write("\nBUFFER:\n")
        self.dump.write(str(self.buffers[735]) + "\n")

        self.dump.write(F"==============tick: {tick}=================\n")

    def mem_dump(self):
        for idx, cell in enumerate(self.dataMemory.memory):
            self.memdump.write(f"ADDR: {hex(idx)}  VALUE: {hex(cell)}\n")