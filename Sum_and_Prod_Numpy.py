import numpy as np
l1=[]
n,m=map(int,input().split())
for i in range(n):
    ele=list(map(int,input().split()))
    l1.append(ele)

a=np.array(l1)                 #converting list into numpy array
print(np.prod(np.sum(a,axis=0)))                   #first do the sum along columns wise and then find the product

---------------------------------------------------------

Success
Input (stdin)

2 2
1 2
3 4
Expected Output

24
