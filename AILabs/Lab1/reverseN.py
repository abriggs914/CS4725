#code

def reverseN(lst, n) :
    a = lst[:n]
    b = lst[n:]
    a.reverse()
    return a + b
    
def reverseNArr(lst, arr) :
    for r_val in arr:
        lst = reverseN(lst, r_val)
    return lst
    
lst = [8,7,1,5,4,3,6,2]
print(reverseNArr(lst, [8,5,3,4,6]))