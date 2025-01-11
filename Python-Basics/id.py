
# id() fynctions
#
#    Id is a unique identifier of every object. In CPython, it gives memory address
#

# Example-1

print(id(5)) #4297288112
a = 10
print('id of a',id(a)) # id of a 4297288272
b = a
print('id of b',id(b)) # id of b 4297288272, 

# Note both values(of a and b) are same because both are pointing to same location 

# Example-2

a=10
b=10
print("id of a:", id(a))  # id of a: 4329171536
print("id of b:", id(b))  # id of b: 4329171536

# Note: Here also it returns same memory address because value is same for both variables 

# is operator in python

a = 10
b = 10
print(a is b)  # True

c = a
print(c is b)  # True

c = 20
print(c is b)  # False