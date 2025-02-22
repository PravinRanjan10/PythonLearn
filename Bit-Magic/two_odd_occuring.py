def oddappearing(arr) :
    xors = 0
    group1 = 0
    group2 = 0
    
    for num in arr :
        xors = xors ^ num   # Find xor of all element of array.
        
    print("xor=", xors)  # For above example, xor would be (5^6)=3
    sn = xors & ~(xors-1)  #  Find Rightmost set bit's of a number
                           # Now question is why we want to find Rightmost set bit.
                           # So finding RMS will tell that one of the no. has set bit at exactly same position and 
                           # other number doesn;t has the set bit at exactly same position.
    print("sn=", sn)       # 1
    
    for num in arr :    # Now devide whole array in two groups. group1: which will contains all number
                        # which Rightmost set bit is 1(1st position)
        if num & sn != 0 :
            group1 = group1 ^ num    # group1={3, 3, 5, 7, 7}. So this group has all the element which 
                                    # rightmost set bit position is 1
        else :
            group2 = group2 ^ num    # group2={4, 4, 4, 4, 6}. So this group has all the element which 
                                    # rightmost set bit position is NOT 1
            
    print(group1,group2)
            
            
if __name__ == "__main__" :
    arr = [3,4,3,4,5,4,4,6,7,7]
    oddappearing(arr)

# Reference: https://www.youtube.com/watch?v=oHDyVK43sGc