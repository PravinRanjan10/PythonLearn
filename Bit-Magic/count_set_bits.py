# count all set bit's of a number
"""
 Method-1:   ==== > O(n)
    while n>0:
        if n%2 == 1:
            count++
        n = n//2 

 Method-2:  =====> O(n)
    while n > 0:
        if 1&n == 1:
            count +=1
        n>>=1

 Method-3:    ====> O(no. of set bits)
    Brian Kernigam's Algorithm   
    
    In this algo, just unset the last bit by using this property.
    n = n&(n-1). If And operation done on n-1 then it unset last bit.
    so overall, it keep unseting as many set bits are present in number.


"""
def countSetBits(n):
    count = 0

    while n > 0:  # while n:
        count+=1
        n = n&(n-1)
    
    print(count)

if __name__=='__main__':
    n=12
    countSetBits(n)