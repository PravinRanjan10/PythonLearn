# Find two numbers which comes odd number of times


def oddappearing(arr) :
    xors = 0
    res1 = 0
    res2 = 0
    
    for i in arr :
        xors = xors ^ i
        
    print("xor=", xors)
    sn = xors & -(xors-1)
    print("sn=", sn)
    
    for i in arr :
        if i & sn != 0 :
            res1 = res1 ^ i
        
        else :
            res2 = res2 ^ i 
            
    print(res1,res2)
            
            
if __name__ == "__main__" :
    arr = [3,4,3,4,5,4,4,6,7,7]
    oddappearing(arr)