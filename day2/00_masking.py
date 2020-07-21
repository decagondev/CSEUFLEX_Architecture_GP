# lets talk about bitshifting
# Example of shifting LDI right by 6 bits:
#
# 10000010
# 01000001
# 00100000
# 00010000
# 00001000
# 00000100
# 00000010
#
# The result is 0b10 or 2, the number of operands for LDI.
LDI = 0b10000010
ADD = 0b00000000
# 000000AA
bob = LDI >> 6
bob == 0b00000010 # => 2
add_to_pc = bob + 1

# FETCH
IR = 0b10000010

# DECODE
add_to_pc = (IR >> 6) + 1

if IR == LDI:
    # do the ldi thing
    pass
elif IR == ADD:
    # do the add thing
    pass

cpu.pc += add_to_pc