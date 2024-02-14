from emu.alu import ALU
from emu.hw import Memory, Register

MEMORY_SIZE = 256


class DataPath:

    def __init__(self):

        # alu
        self.alu: ALU = ALU()

        # mem
        self.instructionMemory: Memory = Memory(MEMORY_SIZE)
        self.dataMemory: Memory = Memory(MEMORY_SIZE)

        # regs
        # lalu
        self.AC: Register = Register()
        self.BR: Register = Register()
        self.IR: Register = Register()
        self.IAR: Register = Register()

        # ralu
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
            735: ["a", "b", "c"]
        }

        self.dump = open("emu.dump", "w")
        self.memdump = open("mem.dump", "w")

    def get_ac_z(self) -> int:
        return 1 if self.AC.get_value() == 0 else 0

    def get_ac_n(self) -> int:
        return 1 if self.AC.get_value() < 0 else 0

    def read_buffer(self, port: int) -> int:
        return ord(self.buffers[port].pop())

    def write_buffer(self, port: int, value: int):
        return self.buffers[port].append(chr(value))

    def log_registers(self, instr, tick):
        self.dump.write(
            f"<tick {tick}> --- AC: {hex(self.AC.get_value()).ljust(16)} DR: {hex(self.DR.get_value()).ljust(16)} BR: {hex(self.BR.get_value()).ljust(16)} PS: {hex(self.PS.get_value()).ljust(16)} IR: {hex(self.IR.get_value()).ljust(16)} SP: {hex(self.SP.get_value()).ljust(16)} IAR: {hex(self.IAR.get_value()).ljust(16)} AR: {hex(self.AR.get_value()).ljust(16)}\n")

    def buff_dump(self):
        self.dump.write("\n.bss\n")
        for buff in self.buffers:
            self.dump.write(f"<port {buff}>: ")
            self.dump.write("".join(str(item) for item in self.buffers[buff]))
            self.dump.write("\n")

    def mem_dump(self):
        for idx, cell in enumerate(self.dataMemory.memory):
            self.memdump.write(f"<addr>: {hex(idx)}  <value>: {hex(cell)}\n")
