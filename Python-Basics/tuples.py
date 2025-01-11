# tuples:
# Tuples are similar to list, they are ordered, they are indexed
# Tuples are immutable (once created, you can not change the values)
# Tules are faster that list

# tuple 

t = (10, 20, "geek")

print(t)  # (10, 20, "geek")

t = ()  # Create a empty tuple

print(type(t)) # <class 'tuple'>

print(t) # ()

t = 10 

print('expected type tuple, but its int', type(t)) # <class 'int'>

t = (10,)  # we need to give comma at end to create empty tuple
# point to note, if t=(10) it will not create tuple, but create int value. similare t=("10") will create string
print(t) # (10,)

print('created single item tuple ', type(t)) # <'class', 'tuple'>


# accessing tuples
t = (10,20,30,40,10) # t= 10, 20, 30, 40, 10 ==>> this will also work

print(t[2])  # 30

print(t[-1])  # 10

print(t[1:3])  # (20, 30)

print(len(t))  # 5

print(t.count(10)) # 2

print(t.index(10)) # 0