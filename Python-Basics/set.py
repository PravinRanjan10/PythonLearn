# set in python
# it's a similar to list like contains any data type 

# some differences are:
# 1. Distinct elements
# 2. Unordered
# 3. No indexing
# 4. Union, Intersection, difference etc. supported
# 5. Uses hashing internally. Thus faster than list

# **********************

s1 = {10, 20, 30}

print(s1) # {10, 20, 30}

s2 = set([20, 30, 40])  # convert list to set

print(s2) # {10, 20, 30}

s3 = {}  # It will not create set but disctonary

print('expected type set',type(s3))  # <class 'dict'>

s4 = set()  # Anotherway to create set

print(type(s4))  # <class 'set'>

print(s4) # set()


# ************* Insertion **********
s = {10, 20}

s.add(30) 

print(s)  # {10, 20, 30}

s.add(30)  # adding duplicate items but won;t be added
print(s)  # {10, 20, 30}

s.update([40, 50])  # update should only usable for iterables like list, dict etc.

print(s) # # {10, 20, 30, 40, 50}, it can be printed in ordere

s.update([60, 70], [80, 90])  # inserting multiple list

print(s)   # {10, 20, 30, 40, 50, 80, 90, 60, 70}

# s.update(100) # it will throw error because 100 is int and not iterables.  
# but s.update({100}) will work because it's  a dict here.


# ********* Removal *********
s = {10, 30, 20, 40}

s.discard(30) 

print("after discard:", s) # {10, 20, 40}

s.remove(20) 

print(s) # {10, 40}

s.clear()  # It will clear all set but empty set will be there

print(s) # set()

s.add(50)

print(s)  # {50}

del s # It will delete set 

# print(s) # It will throw error, s is not defined


# ******** Operations on set-1 **************

s1 = {2, 4, 6, 8}
s2 = {3, 6, 9}

print('union ', s1 | s2)  # {2, 4, 6, 8, 3, 9}
print(s1.union(s2))       # {2, 4, 6, 8, 3, 9}

print('intersecton', s1 & s2)  # {6}
print(s1.intersection(s2))   # {6}

print('present in s1, but not present in s2', s1 - s2)  # {2, 4, 8}
print(s1.difference(s2))

print('symmetric differences, not present in both', s1 ^ s2)  # {2, 3, 4, 8, 9}


# ************* Operations on set-2 ***********

s1 = {2, 4, 6, 8}
s2 = {4, 8}

print('disjoint sets:', s1.isdisjoint(s2)) # False

print('isSubset:', s1 <= s2)  # False
print(s1.issubset(s2))   #  False

print('proper set:', s1 < s2)  # False

print('s1 is superset of s2:', s1 >= s2)   # True
print(s1.issuperset(s2))   # True
 
print('s1 is proper superset of s2:', s1 > s2)   # True