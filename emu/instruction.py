from enum import Enum
# inc iar
# 0x00404440

AC_TO_MEM = 0x01010410
ADDR_TO_AR = 0x00088480
MEM_TO_DR = 0x00800000

class Instruction(Enum):

    PUSH = (
        0x00024502,
        0x000A0502,
        AC_TO_MEM,
        0x00404440
    )

    POP = ()

    LD = (
        ADDR_TO_AR,
        MEM_TO_DR,
        0x00100401,
        0x00404440
    )

    ST = (
        ADDR_TO_AR,
        AC_TO_MEM,
        0x00404440
    )

    JMP = (
        ADDR_TO_AR,
        MEM_TO_DR,
        0x00400401,
        0x00404440 
    )

    # CALL = (
        # 0x00024502,
        # 0x000A0502,
    #     0x01010440,
    #     *JMP
    # )

    HLT = (
        0x40000000
    )

OpCodes = {
    1 : Instruction.LD,
    2 : Instruction.HLT
}

print(Instruction.JMP.value)
print(Instruction.CALL.value)