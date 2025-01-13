x = input() # It will take input from console. Bydefault it will always return string. So x would be string here

print(x) # User given input will be printed.

y = int(input()) # It will convert to integer

# ******* Print **********

print("x") # x, Default new line is added. It's equivalent to print("x\n")

print("x", end="") # x, It doesn't add new line. 

print() # quivalent to print(\n)

print("x", "y", sep="-") # x-y # with new line

print("a", "b", sep="*", end="") # a*b # without new line

print() # quivalent to print(\n)

print("a" + "b") # ab
