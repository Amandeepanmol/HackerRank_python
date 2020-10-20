import numpy
n,m=map(int,input().split())
s=str(numpy.eye(n,m))
print(s.replace("1"," 1").replace("0"," 0"))


---------------------------------------------------------

OUTPUT:
--------
Input (stdin)
3 3
Your Output (stdout)
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
Expected Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
