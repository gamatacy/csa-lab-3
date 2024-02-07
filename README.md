# Ivan Voronin P33312 

## lisp | acc | harv | mc | tick | struct | stream | port | cstr | prob5 | 8bit

## How to

Compile code
```
python -m compiler <input.lsp> <output.yaml>
```

## Lisp syntax

```lisp
<program>               := <expressions> EOF

<expressions>           := | <expressions> <expression>

<expression>            := <open-bracket> <bracketed-expression> <varname> | <literal> | <close-bracket>

<bracketed-expression>  :=  <function-definition> 
                            | <function-call> 
                            | <if-condition> 
                            | <binary-operation> 
                            | <assignment> 
                            | <loop-expression>

<function-call>         := call <fname> <arguments>

<arguments>             := <var> | <expression>

<function-definition>   := defun <varname> <open-bracket> <parameters> <close-bracket> <expressions>

<parameters>            := | <parameters> <varname>

<assignment>            := let <varname> <expr>

<if-condition>          := if <condition-expression> <true-expression>

<loop-expression>       := loop <condition-expression> <expressions> 

<math-operator>         := < | = | << | >> | + | - 

<unary-operator>        := save

<condition-expression>  := <expression>

<literal>               := <number-literal> | <string-literal> 

<number-literal>        := [0-9]+

<string-literal>        := "\w*"

<varname>               := [a-zA-Z\.]\w*
```

## Instruction set

| Byte | Description   |
|------|---------------|
| 0    | Operand       |
| 1    | Operand       |
| 2    | Operand       |
| 3    | Operand       |
| 4    | Operand         (Only 1 lower bit)  |
| 5    |               |
| 6    | OpCode        |
| 7    | OpCode        |


| Opcode | Instruction | Operand | Description |
|--------|-------------|---------|-------------|
| 0x0    | NOP         |         |  Nothing    |
| 0x1    | LD          |   ADDR  |  MEM[ADDR] -> Acc|
| 0x2    | HLT         |         |  Stop clk|
| 0x3    | PUSH        |         |  Acc -> SP+1|
| 0x4    | POP         |         |  SP -> Acc, SP-1|
| 0x5    | ST          |   ADDR  |  Acc -> MEM[ADDR] |
| 0x6    | JMP         |   ADDR  |  ADDR -> IAR |
| 0x7    | ROL         |         |  Acc << 1|
| 0x8    | ROR         |         |  Acc >> 1|
| 0x9    | ADD         |   ADDR  |  Acc + MEM[ADDR]|
| 0xA    | SUB         |   ADDR  |  Acc - MEM[ADDR]|
| 0xB    | JZ          |         |  IF FLAG.Z, IAR+1|
| 0xC    | JN          |         |  IF FLAG.N, IAR+1|
| 0xD    | JC          |         |  IF FLAG.C, IAR+1|
| 0xE    | LDBF        |   PORT  |  IO[PORT] -> Acc |
| 0xF    | STBF        |   PORT  |  Acc -> IO[PORT] |
| 0x10   | CALL        |   ADDR  |  IAR -> SP, ADDR -> IAR |
| 0x20   | RET         |         |  SP -> IAR |


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