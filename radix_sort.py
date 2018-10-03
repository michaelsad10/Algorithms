import math 

def counting_sort(A,x):
    count = [0] * 10
    result = [0] * len(A)
    exp = pow(10,x) 
    for j in range(0,len(A)):
        count[int((A[j]/exp))%10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    for j in range(len(A)-1,-1,-1):
        key = int((A[j]/exp))%10
        index = count[key]
        result[index-1] = A[j]
        count[key] -= 1
    return result

def radix_sort(A,n):
    for i in range(0,n):
       A = counting_sort(A,i)
    return(A) 
A = [123,144,123,145,168,123,121,129]
x = radix_sort(A,4)
print(x)




