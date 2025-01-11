# type() function
# It's a build-in function in python, which tells data type a varabile

# Example-1
a = 10
print(type(a))  # <class 'int'>

b = 10.5
print(type(b))  # <class 'float'>

c = 2 + 4j
print(type(c))  # <class 'complex'>

a = True
print(type(a))  # <class 'bool'>

b = None
print(type(b))  # <class 'NoneType'>




# Example-2 
# sequence type

str = "gfg"
print(type(str)) # <class 'str'>

l = [10, 20, 30]
print(type(l))   # <class 'list'>

t = (10, 20, 30)
print(type(t))  # <class 'tuple'>

s = {10, 20, 30}
print(type(s))  # <class 'set'>

d = {10: "gfg", 20: "ide"}
print(type(d))  # <class 'dict'>