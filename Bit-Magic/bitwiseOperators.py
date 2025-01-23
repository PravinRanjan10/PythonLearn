print(bin(18))  # 0b10010
print(bin(12))  # 0b1100

print(int("0b10010", 2))  # binary to int  # 18

print(int("0b1100", 2))   # binary to int  # 12

# *********************

x = 3
y = 6
# bitwise And : &

print("bitwise and: 3 & 6:", 3 & 6)

# bitwise or : |

print("bitwise or: 3 | 6:", 3 | 6)

# bitwise xor : ^

print("bitwise xor: 3 ^ 6:", 3 ^ 6)


# ********** Left Shift *********** # Multiplication 
x = 5

print("left shift: 5 by 1", x << 1)

print("left shift: 5 by 2", x << 2)

print("left shift:, 5 by 3", x << 3)


# ************* Right Shift ********* # Division

x = 5

print("right shift: 5 by 1:", x >> 1)

print("right shift: 5 by 2:", x >> 2)

print("right shift:, 5 by 3:", x >> 3)

# ************** Bitwise not **********

x = 5
print("bitwise not : ~5:", ~x)  # bitwise not


# Binary representation of -ve number:
"""
    There are three approach to represent binary number
    1. 2's complement
            a) Invert all bits
            b) add 1

            Ex: 
                x = 3 ( binary is 00..011)
                    a) invert it ==> 11 ... 1100
                    b) add 1 ==>     11 ... 1101

    2. sign bit

    3. 1's complement
"""