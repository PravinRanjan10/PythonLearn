# Check if a given number is power of 2
""" 
Method-1: 
keep deviding by 2 until number become zero. 
If reminder is not zero at any point =, means it's not power of two

def isPowerOfTwo(n):
	if (n == 0):
		return False
	while (n != 1):
		if (n % 2 != 0):
			return False
		n = n // 2

	return True

"""

# Method-2   ==> if n&(n-1) == 0, power of two else not
def isPowerOfTwo(n):
    if n == 0:
        print(False)

    if n&(n-1) == 0:
        print (True)
    else:
        print(False)

if __name__== '__main__':
    isPowerOfTwo(8)