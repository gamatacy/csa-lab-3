from emu.instruction import *

class HighLevelInstruction():

    def __init__(self, instruction: Instruction, op: int):
        self.instruction = instruction
        self.op = op

class HighLevelData():

    def __init__(self, value: str | int, addr: int):
        self.value = value
        self.addr = addr

class FUNction():

    def __init__(self, params: [str], addr: int):
        self.params = params 
        self.addr = addr

functions: {str : FUNction } = {}
instructions: [HighLevelInstruction] = []
data: {str : HighLevelData} = {}
_data_pointer = 0
_start_point = 0

def get_start_point() -> int:
    global _start_point
    return _start_point

def add_halt():
    instructions.append(
        HighLevelInstruction(
            Instruction.HLT,
            0
        )
    )

def generator(tokens: [str]):
    global _data_pointer
    global _start_point

    for i in range(len(tokens)):
        match tokens[i]:
            case '_start_':
                _start_point = len(instructions)
            case 'defun':
                fname = tokens[i+1] 
                params = tokens[i+2]
                body = tokens[i+3]

                _start_addr = len(instructions)

                for p in params:
                    data[p] = HighLevelData(0,_data_pointer)
                    _data_pointer += 1
            
                generator(body)
                functions[fname] = FUNction(params, _start_addr)
                
                i += 3
                break
            case 'call':
                for idx, p in enumerate(functions[tokens[i+1]].params):
                    instructions.append(
                        HighLevelInstruction(
                            Instruction.LD,
                            data[tokens[i+2][idx]].addr
                        )
                    )
                    instructions.append(
                        HighLevelInstruction(
                            Instruction.ST,
                            data[p].addr
                        )
                    )

                instructions.append(
                    HighLevelInstruction(
                        Instruction.CALL,
                        functions[tokens[i+1]].addr
                    )
                )
                i += 1
            case 'ret':
                instructions.append(
                    HighLevelInstruction(
                        Instruction.LD,
                        data[tokens[i+1]].addr
                    )
                )
                instructions.append(
                    HighLevelInstruction(
                        Instruction.RET,
                        0
                    )
                )
                i += 1
            case 'read':
                instructions.append(
                        HighLevelInstruction(
                            Instruction.LDBF,
                            tokens[i+2][0]
                        )
                    )
                instructions.append(
                        HighLevelInstruction(
                            Instruction.ST,
                            data[tokens[i+1]].addr
                        )
                    )
            case 'write':
                if isinstance(tokens[i+1][0], int):
                    instructions.append(
                        HighLevelInstruction(
                            Instruction.LDC,
                            tokens[i+1][0]
                        )
                    )
                elif tokens[i+1][0] in data:
                    instructions.append(
                        HighLevelInstruction(
                            Instruction.LD,
                            data[tokens[i+1][0]].addr
                        )
                    )
                else:
                    instructions.append(
                        HighLevelInstruction(
                            Instruction.LDC,
                            0
                        )
                    )
                instructions.append(
                        HighLevelInstruction(
                            Instruction.STBF,
                            data[tokens[i+2][0]].value if tokens[i+2][0] in data else tokens[i+2][0]
                        )
                    )
            case 'let':
                data[tokens[i+1]] = HighLevelData(tokens[i+2][0], _data_pointer)
                if isinstance(tokens[i+2], str):
                    _data_pointer += len(tokens[i+2])+1
                else:
                    _data_pointer += 1
                i += 1
            case 'alloc':
                data[tokens[i+1]] = HighLevelData(tokens[i+2][0], _data_pointer)
                _data_pointer += tokens[i+2][0]
                i += 1
            case 'save':
                if len(tokens[i+2]) == 1 and isinstance(tokens[i+2][0], int):
                    instructions.append(
                        HighLevelInstruction(
                            Instruction.LDC,
                            tokens[i+2][0]
                        )
                    )
                elif len(tokens[i+2]) == 1 and tokens[i+2][0] in data:
                    instructions.append(
                        HighLevelInstruction(
                            Instruction.LD,
                            data[tokens[i+2][0]].addr
                        )
                    )
                else: 
                    generator(tokens[i+2])

                instructions.append(
                    HighLevelInstruction(
                        Instruction.ST,
                        data[tokens[i+1]].addr
                    )
                )
                i += 2
                break
            case 'while':
                condition = tokens[i+1][0]
                variable = tokens[i+1][1]
                value = tokens[i+1][2]
                _start_addr = len(instructions)
                generator(tokens[i+3])

                instructions.append(
                    HighLevelInstruction(
                        Instruction.LDC,
                        value
                    )
                )

                _tmp_addr = _data_pointer+322 
                instructions.append(
                    HighLevelInstruction(
                        Instruction.ST,
                        _tmp_addr
                    )
                )

                instructions.append(
                    HighLevelInstruction(
                        Instruction.LD,
                        data[variable].addr
                    )
                )

                instructions.append(
                    HighLevelInstruction(
                        Instruction.SUB,
                        _tmp_addr
                    )
                )

                match condition:
                    case '=':
                
                        instructions.append(
                            HighLevelInstruction(
                                Instruction.JZ,
                                0
                            )
                        )

                        instructions.append(
                            HighLevelInstruction(
                                Instruction.JMP,
                                _start_addr
                            )
                        )

                    case '<':
                        instructions.append(
                            HighLevelInstruction(
                                Instruction.JN,
                                0
                            )
                        )

                        instructions.append(
                            HighLevelInstruction(
                                Instruction.JMP,
                                _start_addr
                            )
                        )
                i += 3
                break
            case 'if':
                condition = tokens[i+1][0]
                variable = tokens[i+1][1]
                value = tokens[i+1][2]
                
                instructions.append(
                    HighLevelInstruction(
                        Instruction.LDC,
                        value
                    )
                )

                _tmp_addr = _data_pointer+322 
                instructions.append(
                    HighLevelInstruction(
                        Instruction.ST,
                        _tmp_addr
                    )
                )

                instructions.append(
                    HighLevelInstruction(
                        Instruction.LD,
                        data[variable].addr
                    )
                )

                instructions.append(
                    HighLevelInstruction(
                        Instruction.SUB,
                        _tmp_addr
                    )
                )

            

                match condition:
                    case '=':
                
                        instructions.append(
                            HighLevelInstruction(
                                Instruction.JZ,
                                0
                            )
                        )

                        instructions.append(
                            HighLevelInstruction(
                                Instruction.JMP,
                                0
                            )
                        )

                    case '<':
                        instructions.append(
                            HighLevelInstruction(
                                Instruction.JN,
                                0
                            )
                        )

                        instructions.append(
                            Instruction.JMP,
                            0
                        )

                _jmp_addr = len(instructions)
                generator(tokens[i+2])
                instructions[ len(instructions) - (len(instructions) - _jmp_addr) - 1].op = len(instructions)
                i += 3
                break
            case _:
                match tokens[i]:
                    case "+":
                        if tokens[i+1] in data:
                            instructions.append(
                                HighLevelInstruction(
                                    Instruction.LD,
                                    data[tokens[i+1]].addr
                                )
                            )
                        else:
                            instructions.append(
                                HighLevelInstruction(
                                    Instruction.LDC,
                                    tokens[i+1]
                                )
                            )

                         
                        #2nd op must be in memory
                        instructions.append(
                            HighLevelInstruction(
                                Instruction.ADD,
                                data[tokens[i+2]].addr
                            )
                        )

                        i+=2
                    case "-":
                        if tokens[i+1] in data:
                            instructions.append(
                                HighLevelInstruction(
                                    Instruction.LD,
                                    data[tokens[i+1]].addr
                                )
                            )
                        else:
                            instructions.append(
                                HighLevelInstruction(
                                    Instruction.LDC,
                                    tokens[i+1]
                                )
                            )

                         
                        #2nd op must be in memory
                        instructions.append(
                            HighLevelInstruction(
                                Instruction.SUB,
                                data[tokens[i+2]].addr
                            )
                        )
                        i+=2
                    case "<<":
                        if tokens[i+1] in data:
                            instructions.append(
                                HighLevelInstruction(
                                    Instruction.LD,
                                    data[tokens[i+1]].addr
                                )
                            )
                        else:
                            instructions.append(
                                HighLevelInstruction(
                                    Instruction.LDC,
                                    tokens[i+1]
                                )
                            )
                        for _ in range(tokens[i+2]):
                            instructions.append(
                                HighLevelInstruction(
                                    Instruction.ROL,
                                    0
                                )
                            )
                        i+=2
                    case ">>":
                        if tokens[i+1] in data:
                            instructions.append(
                                HighLevelInstruction(
                                    Instruction.LD,
                                    data[tokens[i+1]]
                                )
                            )
                        else:
                            instructions.append(
                                HighLevelInstruction(
                                    Instruction.LDC,
                                    tokens[i+1]
                                )
                            )
                        for _ in range(tokens[i+2]):
                            instructions.append(
                                HighLevelInstruction(
                                    Instruction.ROL,
                                    0
                                )
                            )
                        i+=2
                    case _:
                        if isinstance(tokens[i], list):
                            generator(tokens[i])

                      

              
        

            

