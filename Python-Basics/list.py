# List is a collection of items of any data types


"""
List Methods
*****************
Let’s look at different list methods in Python:

    append(): Adds an element to the end of the list.

    copy(): Returns a shallow copy of the list.

    clear(): Removes all elements from the list.

    count(): Returns the number of times a specified element appears in the list.

    extend(): Adds elements from another list to the end of the current list.

    index(): Returns the index of the first occurrence of a specified element.

    insert(): Inserts an element at a specified position.

    pop(): Removes and returns the element at the specified position (or the last element if no index is specified).

    remove(): Removes the first occurrence of a specified element.

    reverse(): Reverses the order of the elements in the list.

    sort(): Sorts the list in ascending order (by default).
"""
# List item access

l = [10,20,30,40,50]

print(l)  # [10,20,30,40,50]
print(l[3])   # 40
print(l[-1])  # 50
print(l[-2])  # 40

# *****************
# List insert and search

l = [10, 20, 30, 40, 50]

l.append(30)     # appending 30 at last
print(l)         # [10, 20, 30, 40, 50, 30]
l.insert(1, 15)  # inserting value at index 1 
print(l)         # [10, 15, 20, 30, 40, 50, 30]

print(15 in l)      # checking for 15 in l    # True
print(l.count(30))  # counting occurence of 30   # 2
print(l.index(30))  # checking index of first occurence of 30  # 3

# *****************
# List : removal of item

l = [10, 20, 30, 40, 50, 60, 70, 80]

print(l)    # [10, 20, 30, 40, 50, 60, 70, 80]


l.remove(20)   # It return None. It only removes 1st occurance of item.
print('after removing 20',l)  # [10, 30, 40, 50, 60, 70, 80]

print('removing and returning last item',l.pop())  #80
print('after removing last item',l)   # [10, 30, 40, 50, 60, 70]

print('removing and returning item at index 2',l.pop(2))  # 40

print('after removing item at index 2',l)  # [10, 30, 50, 60, 70]

del l[1]   # It doesn't return anything, will throw error if want to print

print('after removing item at index 1, using del',l)  # [10, 50, 60, 70]

del l[0:2]  # It doesn't return anything

print('after removing items from  index 0 to 2-1, using del',l) # [60, 70]


# *******************
# general purpose functions

l = [10, 40, 20, 50]

print(l)

print('max', max(l))  # 50

print('min', min(l))  # 10

print('sum', sum(l))  # 120

l.reverse()  

print('after reverse', l) # [50, 20, 40, 10]

l.sort()  # can be explored more. l.sort(reverse=True | key=somefunctions)

print('after sorting', l) # [10, 20, 40, 50]

# few more operations
new_list = l.sorted()
l3 = l1+l2  # It will add all the elementes from both list

println(l1*2)  # It's a similar l1+l1. Ex: l1 = [1, 2, 3] so l1*2 would be [1, 2, 3, 1, 2, 3]



