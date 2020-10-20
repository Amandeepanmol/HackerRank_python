import numpy
N,M=map(int,input().split())
l1=[]
for i in range(N):
    ele=list(map(int,input().split()))
    l1.append(ele)
a=numpy.array(l1)                         #converts lists in array
b=numpy.transpose(a)               #finds transpose
print(b)
c=a.flatten()                    #finds flatten
print(c)

------------------------------------------

OUTPUT:
------------


nput (stdin)

2 2
1 2
3 4
Expected Output

[[1 3]
 [2 4]]
[1 2 3 4]
