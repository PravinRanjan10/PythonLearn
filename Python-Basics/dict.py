# dictonary is collection of key value pairs

d = {110: 'abc', 101: 'xyz', 105: 'pqr'}

print(d)  # {110: 'abc', 101: 'xyz', 105: 'pqr'}

d = {}  # It create empty dictonary
d['laptop'] = 40000   # {'laptop': 40000}
d['mobile'] = 15000   # {'laptop': 40000, 'mobile': 15000}
d['earphone'] = 1000   # {'laptop': 40000, 'mobile': 15000, 'earphone': 1000}

print(d)  # {'laptop': 40000, 'mobile': 15000, 'earphone': 1000}

print(d['mobile'])  # 15000


# ******** Accessing: Operations on dict-1 ************

d = {110: 'abc', 101: 'xyz', 105: 'pqr'}

print(d.get(101))  # xyz
 
print(d.get(125))  # None, It won't throw any error if key not exists

print(d.get(125, "NA"))  # If key 125 not found then return ""NA

if 125 in d:    # Insted of line 27-30, better to use line 25
    print(d[125]) 
else:
    print("NA")  


# ******** Removal: Operations on dict-2 ************

d = {110: 'abc', 101: 'xyz', 105: 'pqr', 106: 'bcd'}

d[101] = 'wxy'

print(len(d)) # 4

print(d)  # {110: 'abc', 101: 'wxy', 105: 'pqr', 106: 'bcd'}

print('returning and removing 105', d.pop(105))  # 105 pqr

print('after removing 105', d) # {110: 'abc', 101: 'wxy', 106: 'bcd'}

del d[106] # if key doesn't exists it will throw keyError 

print(d) # {110: 'abc', 101: 'wxy'}

d[108] = 'cde' # {110: 'abc', 101: 'wxy', 108: 'cde'}

print('returning and removing last inserted', d.popitem()) # (108, 'cde') it retruns both key and value in tuple