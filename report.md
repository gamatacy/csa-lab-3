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
| 0  | DR -> LALU  |
| 1  | SP -> LALU  |
| 2  | PS -> LALU  |
| 3  |             |
| 4  | AC -> RALU  |
| 5  | BR -> RALU  |
| 6  | IAR -> RALU |
| 7  | IR -> RALU  |
| 8  | ~RALU       |
| 9  | ~LALU       |
| 10 | R + L       |
| 11 | AND         |
| 12 | SHLT        |
| 13 | SHRT        |
| 14 |             |
| 15 |             |
| 16 | ALU -> DR   |
| 17 | ALU -> SP   |
| 18 | ALU -> PS   |
| 19 | ALU -> AR   |
| 20 | ALU -> AC   |
| 21 | ALU -> BR   |
| 22 | ALU -> IAR  |
| 23 |             |
| 24 |             |
| 25 |             |
| 26 |             |
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
| 0  | DR -> LALU  |
| 1  | SP -> LALU  |
| 2  | PS -> LALU  |
| 3  |             |
| 4  | AC -> RALU  |
| 5  | BR -> RALU  |
| 6  | IAR -> RALU |
| 7  | IR -> RALU  |
| 8  | ~RALU       |
| 9  | ~LALU       |
| 10 | R + L       |
| 11 | AND         |
| 12 | SHLT        |
| 13 | SHRT        |
| 14 |             |
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