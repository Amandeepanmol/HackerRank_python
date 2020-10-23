import numpy
l1=[]
n,m=map(int,input().split())
for i in range(n):
    ele=list(map(int,input().split()))
    l1.append(ele)

a=numpy.array(l1)
print(numpy.max(numpy.min(a,axis=1)))

----------------------------------------------------

Compiler Message
Success
Input (stdin)

4 2
2 5
3 7
1 3
4 0
Expected Output

3
