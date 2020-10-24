import numpy
n=int(input())
A=numpy.array([input().split() for _ in range(n)],dtype=int)
B=numpy.array([input().split() for _ in range(n)],dtype=int)
print(numpy.dot(A,B))
----------------------------------------------------------------------------

OUTPUT
---------

Compiler Message
Success
Input (stdin)

2
1 2
3 4
1 2
3 4
Expected Output

[[ 7 10]
 [15 22]]
