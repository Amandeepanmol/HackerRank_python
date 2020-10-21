import numpy as np
N,M,P=map(int,input().split())
l1=[]
l2=[]
for i in range(N):
    ele1=list(map(int,input().split()))
    l1.append(ele1)
for i in range(M):
    ele2=list(map(int,input().split()))
    l2.append(ele2)

a=np.array(l1)
b=np.array(l2)
c=np.concatenate((a,b),axis=0)
print(c)

---------------------------------------------------

OUTPUT:
--------

Compiler Message
Success
Input (stdin)

4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4
Expected Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]
