# Find only odd of a list.
# Perform xor operation with all nums. Odd number will be found

x = [10, 20, 20]
res = 0
for num in x:
    res = res ^ num
print(res) # 10
    