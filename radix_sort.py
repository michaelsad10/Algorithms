import math 

def counting_sort(A,x):
    count = [0] * 9
    result = [0] * len(A)
    for j in range(0,len(A)):
        count[int((A[j]/x))%10] += 1
    for i in range(1,9):
        count[i] += count[i-1]
    for j in range(len(A)-1,-1,-1):
        key = int((A[j]/x))%10
        index = count[key]
        result[index-1] = A[j]
        count[key] -= 1
    return result

def radix_sort(A,n):
    for i in range(0,n):
       A = counting_sort(A,(pow(10,i)))
    return(A) 
A = [123,144,123,145,168,123,121]
x = radix_sort(A,4)
print(x)




