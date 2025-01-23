# Set K'th bit is set or not
# Method-1: using left shift
# Method-2: using right shift

def M1_isKthBitSet(n, k):
    if n&(1<<(k-1)):   # k is counted from 1
        print("SET")
    else:
        print("NOT SET")

def M2_isKthBitSet(n, k):
    if 1&(n>>(k-1)):   # k is counted from 1
        print("SET")
    else:
        print("NOT SET")

if __name__=='__main__':
    n=5
    k=3
    M1_isKthBitSet(n, k)
    M2_isKthBitSet(n, k)


