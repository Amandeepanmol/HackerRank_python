import numpy
n,m=map(int,input().split())
a=numpy.array([input().split() for i in range(n)],dtype=int)
b=numpy.array([input().split() for i in range(n)],dtype=int)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))
----------------------------------------------------------------

OUTPUT:
---------

Compiler Message
Success
Input (stdin)

1 4
1 2 3 4
5 6 7 8
Expected Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]
