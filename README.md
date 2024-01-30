# Ivan Voronin P33312 

## lisp | acc | harv | mc | tick | struct | stream | port | cstr | prob5 | 8bit

## Instruction set

| Byte | Description   |
|------|---------------|
| 0    | Operand       |
| 1    | Operand       |
| 2    | Operand       |
| 3    | Operand       |
| 4    | Operand         (Only 1 lower bit)  |
| 5    |               |
| 6    |               |
| 7    | OpCode        |


| Opcode | Instruction | Operand |
|--------|-------------|---------|
| 0x0    | NOP         |         |         
| 0x1    | LD          |   ADDR  |
| 0x2    | HLT         |         |
| 0x3    | PUSH        |         |
| 0x4    | POP         |         |
| 0x5    | ST          |   ADDR  |
| 0x6    | JMP         |   ADDR  |
| 0x7    | ROL         |         |
| 0x8    | ROR         |         |
| 0x9    | ADD         |   ADDR  |
| 0xA    | SUB         |   ADDR  |
| 0xB    | JZ          |         |
| 0xC    | JN          |         |
| 0xD    | JC          |         |
| 0xE    | LDBF        |   PORT  |
| 0xF    | STBF        |   PORT  |


## Microcode 

Микрокоманда - 32 бита 

Микрокоманды хранятся в памяти микрокоманд 

Разделены на операционные и управляющие. Операционные - для чтения/записи регистров и памяти, управляющие - для условных переходов.

Форматы команд: 

**Операционная микрокоманда**

```
|Bit | Description |
|----|-------------|
| 0  | DR -> RALU  |
| 1  | SP -> RALU  |
| 2  | PS -> RALU  |
| 3  |             |
| 4  | AC -> LALU  |
| 5  | BR -> LALU  |
| 6  | IAR -> LALU |
| 7  | IR -> LALU  |
| 8  | ~RALU       |
| 9  | ~LALU       |
| 10 | L + R       |
| 11 | AND         |
| 12 | SHLT        |
| 13 | SHRT        |
| 14 | INC         |
| 15 | 2LB         |
| 16 | ALU -> DR   |
| 17 | ALU -> SP   |
| 18 | ALU -> PS   |
| 19 | ALU -> AR   |
| 20 | ALU -> AC   |
| 21 | ALU -> BR   |
| 22 | ALU -> IAR  |
| 23 | MEM -> DR   |
| 24 | DR -> MEM   |
| 25 | IO -> DR    |
| 26 | DR -> IO    |
| 27 |             |
| 28 |             |
| 29 |             |
| 30 | HALT        |
| 31 | 0           |
```

**Управляющая микрокоманда**

```
|Bit | Description |
|----|-------------|
| 0  | DR -> RALU  |
| 1  | SP -> RALU  |
| 2  | PS -> RALU  |
| 3  |             |
| 4  | AC -> LALU  |
| 5  | BR -> LALU  |
| 6  | IAR -> LALU |
| 7  | IR -> LALU  |
| 8  | ~RALU       |
| 9  | ~LALU       |
| 10 | L + R       |
| 11 | AND         |
| 12 | SHLT        |
| 13 | SHRT        |
| 14 | INC         |
| 15 | 2LB         |
| 16 | CMP Z       |
| 17 | CMP N       |
| 18 | CMP C       |
| 19 | CMP V       |
| 20 |             |
| 21 |             |
| 22 |             |
| 23 |             |
| 24 |             |
| 25 |             |
| 26 |             |
| 27 |             |
| 28 |             |
| 29 |             |
| 30 |             |
| 31 | 1           |
```