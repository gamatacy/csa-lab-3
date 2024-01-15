from enum import Enum

class Instruction(Enum):
    LD = (
        0x00800000,
        0x00100401,
        0x00100411
    )
    HLT = (
        0x40000000
    )

OpCodes = {
    1 : Instruction.LD,
    2 : Instruction.HLT
}
