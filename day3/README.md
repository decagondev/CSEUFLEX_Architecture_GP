# System STACK

```
FF: 00 
FE: 00
FD: 00
FC: 00
FB: 00
FA: 00
F9: 00
F8: 00
F7: 00
F6: 00 
F5: 00 
F4: 00 
F3: 12 
F2: 32 
F1: 00
F0: 00
EF: 00
.
.
.
05: 00
04: 00
03: XX
02: XX 
01: XX 
00: XX <-- PC <-- SP


R0: 12
R1: 32
R2: 00

R7: F3 (this is the SP)

PUSH R0 #
PUSH R1 #
POP R2 #
POP R2 #
POP R2 #
POP R2 #
POP R2 #
POP R2
POP R2
POP R2
POP R2
POP R2
POP R2
POP R2
POP R2
POP R2 <---- 11 pops



 1111 1111
+0000 0001
10000 0000
 0000 0000
11111 1111
```