from emu.data_path import DataPath
from emu.instruction import Instruction, OpCodes


class ControlUnit:

    def __init__(self):
        self.tick = 0

    def runclk(self, data_path: DataPath):
        instruction: Instruction
        raw_instruction: int

        while True:
            raw_instruction = data_path.instructionMemory.get_value(
                data_path.IAR.get_value()
            )

            data_path.IR.set_value(raw_instruction)

            instruction = OpCodes[(raw_instruction >> 24)]

            if self.execute_instruction(data_path, instruction):
                break

    def execute_instruction(self, data_path: DataPath, instruction: Instruction):

        if instruction is Instruction.NOP:
            data_path.mem_dump()
            return True

        if instruction is Instruction.HLT:
            data_path.mem_dump()
            data_path.buff_dump()
            return True

        mcodes: [int] = instruction.value

        for mcode in mcodes:

            if mcode & 0x80000000:
                self.execute_control_micro_code(data_path, mcode)
            else:
                self.execute_operation_microcode(data_path, mcode)

            data_path.log_registers(instruction.name, self.tick)
            self.tick += 1

    def execute_operation_microcode(self, data_path: DataPath, mcode: int):
        self.execute_micro_code(data_path, mcode)

        # save alu output to registers
        for offset in range(7):
            if mcode & (0x10000 << offset):
                data_path.mappedRegister[offset].set_value(data_path.alu.get_output())

        if mcode & 0x7800000 and (data_path.IR.get_value() & 0x1FFFF) and (data_path.IR.get_value() >> 24) != 0x10:
            data_path.AR.set_value(
                data_path.IR.get_value() & 0xFFFF
            )

        if mcode & 0x800000:
            data_path.DR.set_value(
                data_path.dataMemory.get_value(
                    data_path.AR.get_value()
                )
            )
        elif mcode & 0x1000000:
            data_path.dataMemory.set_value(
                data_path.AR.get_value(),
                data_path.DR.get_value()
            )
        elif mcode & 0x2000000:
            data_path.DR.set_value(
                data_path.read_buffer(data_path.AR.get_value())
            )
        elif mcode & 0x4000000:
            data_path.write_buffer(data_path.AR.get_value(),
                                   data_path.AC.get_value()
                                   )

    def execute_control_micro_code(self, data_path: DataPath, mcode: int):
        self.execute_micro_code(data_path, mcode)

        flags_mask: int = (mcode & 0x0F0000) >> 16
        not_flags_masks: int = (mcode & 0x300000) >> 20

        alu_flags: int = data_path.get_ac_z()
        alu_flags += (data_path.get_ac_n() << 1)

        if flags_mask == alu_flags and not_flags_masks == 0 or flags_mask == 0 and not_flags_masks != alu_flags:
            data_path.IAR.set_value(
                data_path.IAR.get_value() + 1
            )
            data_path.log_registers("Branch", self.tick)

    def execute_micro_code(self, data_path: DataPath, mcode: int):
        # clear alu
        data_path.alu.set_left_operand(0)
        data_path.alu.set_right_operand(0)

        # set right alu operand
        if mcode & 0x1:
            data_path.alu.set_right_operand(data_path.DR.get_value())
        elif mcode & 0x2:
            data_path.alu.set_right_operand(data_path.SP.get_value())
        elif mcode & 0x4:
            data_path.alu.set_right_operand(data_path.PS.get_value())

        # set left alu operand
        if mcode & 0x10:
            data_path.alu.set_left_operand(data_path.AC.get_value())
        elif mcode & 0x20:
            data_path.alu.set_left_operand(data_path.BR.get_value())
        elif mcode & 0x40:
            data_path.alu.set_left_operand(data_path.IAR.get_value())
        elif mcode & 0x80:
            data_path.alu.set_left_operand(data_path.IR.get_value())

        # inverse operands
        if mcode & 0x200:
            data_path.alu.inv_left_operand()

        if mcode & 0x100:
            data_path.alu.inv_right_operand()

        # sum/and
        if mcode & 0x400:
            data_path.alu.sum()
        elif mcode & 0x800:
            data_path.alu.conjuction()

        # increment
        if mcode & 0x4000:
            data_path.alu.inc()

        # only 2 lower bytes
        if mcode & 0x8000:
            data_path.alu._2lb()

        # shift
        if mcode & 0x1000:
            data_path.alu.shlt()
        elif mcode & 0x2000:
            data_path.alu.shrt()
