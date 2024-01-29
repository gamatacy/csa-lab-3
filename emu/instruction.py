from enum import Enum
# inc iar
# 0x00404440

AC_TO_MEM = 0x01010410
AC_TO_DR = 0x00010410
DR_TO_AC = 0x00100401
ADDR_TO_AR = 0x00088480
SP_TO_AR = 0x00080402
MEM_TO_DR = 0x00800000
INC_IAR = 0x00404440

class Instruction(Enum):

    PUSH = (
        0x00020602,
        SP_TO_AR,
        AC_TO_MEM,
        INC_IAR
    )

    POP = (
        SP_TO_AR,
        MEM_TO_DR,
        DR_TO_AC,
        0x00024402,
        INC_IAR
    )

    LD = (
        ADDR_TO_AR,
        MEM_TO_DR,
        DR_TO_AC,
        INC_IAR
    )

    ST = (
        ADDR_TO_AR,
        AC_TO_MEM,
        INC_IAR
    )

    JMP = (
        ADDR_TO_AR,
        MEM_TO_DR,
        0x00400401,
        INC_IAR 
    )

    ROL = (
        0x00101410,
        INC_IAR
    )

    ROR = (
        0x00102410,
        INC_IAR
    )

    ADD = (
        ADDR_TO_AR,
        MEM_TO_DR,
        0x00100411,
        INC_IAR
    )

    SUB = (
        ADDR_TO_AR,
        MEM_TO_DR,
        0x00104511,
        INC_IAR
    )

    JZ = (
        0x80010000,
        INC_IAR
    )

    JN = (
        0x80020000,
        INC_IAR
    )

    JC = (
        0x80040000,
        INC_IAR
    )

    LDBF = (
        ADDR_TO_AR,
        0x02000000,
        DR_TO_AC,
        INC_IAR
    )

    STBF = (
        ADDR_TO_AR,
        AC_TO_DR,
        0x04000000,
        INC_IAR
    )

    NOP = (
        0x00000000
    )

    HLT = (
        0x40000000
    )

OpCodes = {
    0x0 : Instruction.NOP,
    0x1 : Instruction.LD,
    0x2 : Instruction.HLT,
    0x3 : Instruction.PUSH,
    0x4 : Instruction.POP,
    0x5 : Instruction.ST,
    0x6 : Instruction.JMP,
    0x7 : Instruction.ROL,
    0x8 : Instruction.ROR,
    0x9 : Instruction.ADD,
    0xA : Instruction.SUB,
    0xB : Instruction.JZ,
    0xC : Instruction.JN,
    0xD : Instruction.JC,
    0xE : Instruction.LDBF,
    0xF : Instruction.STBF
}