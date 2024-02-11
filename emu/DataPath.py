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
        return self.buffers[port].append(chr(value))

    def log_registers(self, instr,tick):
        self.dump.write(f"<tick {tick}> --- AC: {hex(self.AC.getValue()).ljust(16)} DR: {hex(self.DR.getValue()).ljust(16)} BR: {hex(self.BR.getValue()).ljust(16)} PS: {hex(self.PS.getValue()).ljust(16)} IR: {hex(self.IR.getValue()).ljust(16)} SP: {hex(self.SP.getValue()).ljust(16)} IAR: {hex(self.IAR.getValue()).ljust(16)} AR: {hex(self.AR.getValue()).ljust(16)}\n")

    def buff_dump(self):
        self.dump.write(F"\n.bss\n")
        for buff in self.buffers:
            print(self.buffers[buff])
            self.dump.write(f"<port {buff}>: ")
            self.dump.write("".join(str(item) for item in self.buffers[buff]))
            self.dump.write("\n")

        # self.dump.write(F"\n.mem\n")
        # for idx, cell in enumerate(self.dataMemory.memory):
        #     self.dump.write(f"<addr>: {hex(idx)}  <value>: {hex(cell)}\n")

    def mem_dump(self):
        for idx, cell in enumerate(self.dataMemory.memory):
            self.memdump.write(f"<addr>: {hex(idx)}  <value>: {hex(cell)}\n")