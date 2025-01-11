# Types of conversion in python
# 1. Implicit Type conversion
# 2. Explicit Type conversion

# ********** Implicit type conversion **********

a = 10
b = 1.5
c = a + b  # a convert to float
print(c) # 11.5

d = True
e = a + d  # bool convert to 1 or 0
print(e)   # 11, the Reason is, a = 10 and d = True (which is 1 in integer)

f = False
g = a + False
print(g) # 10, bcz 10+0(for false)


# ********** Explicit type conversion **********
# explicit means, default conversion will not happen. For example, here string needs to be converted in int or float

# Example-1
s = '135'

i = 10 + int(s)  # str to int conversion, so it will become s = 135

f = float(s)  # str to float conversion, so it will become f = 135.0

print(i)  # 145
print(f) # 135.0

# Example-2

# explicit conversion

s = 'pravin'

print('str to list', list(s))  # ['p', 'r', 'a', 'v', 'i', 'n']

print('str to tuple', tuple(s)) # ('p', 'r', 'a', 'v', 'i', 'n')

print('', set(s))  # {'p', 'r', 'a', 'v', 'i', 'n'}


# Example-3

l = ['a', 'b', 'c']

print('list to str', str(l)) # ['a', 'b', 'c'] convert all item to string

a = 10

b = 11

print('int to str,', str(a) + str(b))  # 1010, it will a string

c = 12.5

print('float to str', str(c))  # "12.5"

# Example-4

t = (10, 20, 30)

print('tuple to list', list(t))  # [10, 20, 30]

s = {10, 20, 30}

print('set to list', list(s))  # [10, 20, 30]

# Example-4

# int to binary

a = 20

print('int to binary 20-->', bin(a), len(bin(a)))  # 0b10100, 7 ==> 0b for binary, 0o for octa and 0x for hexa prefix will be added

print('int to octa 20-->', oct(a))    # 0o24   ==> we group with three bits of it's binary and convert to integer

print('int to hexa 20-->', hex(a))    # 0x14   ==> we group 4 bits of it's binary and convert to integer

# Example -5

# int to binary

a = "1001"

print('binary to int', int(a, 2))  # base is 2 # output: 9

b = "12"

print('oct to int', int(b, 8))  # base is 8    # output: 10, 1*8^1 + 2*8^0
 
c = "A1"

print('hexa to int', int(c, 16))    # base is 16 # output: 161, A=10(in hexa form) so 10*16^1 + 1*16^0 = 160+1


# Example -6 
s = "135" # This string can be converted to 135 integer
s = "abc" # This is a sting literal and can not be converted to integer

