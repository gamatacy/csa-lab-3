# Ivan Voronin P33312 

## lisp | acc | harv | mc | tick | struct | stream | port | cstr | prob5 | 8bit



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
| 15 |             |
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
| 15 |             |
| 16 | CMP Z       |
| 17 | CMP N       |
| 18 | CMP C       |
| 19 | CMP V       |
| 20 |jmp addr bgn |
| 21 | *           |
| 22 | *           |
| 23 | *           |
| 24 | *           |
| 25 | *           |
| 26 | *           |
| 27 |jmp addr end |
| 28 |             |
| 29 |             |
| 30 |             |
| 31 | 1           |
```