1st way:
----------
import numpy
a=list(map(int,input().split()))
b=list(map(int,input().split()))
A=numpy.array(a)
B=numpy.array(b)
print(numpy.inner(A,B))
print(numpy.outer(A,B))



'''
2nd way
---------
import numpy
A=numpy.array(input().split(),dtype=int)
B=numpy.array(input().split(),dtype=int)
print(numpy.inner(A,B))
print(numpy.outer(A,B))

------------------------------------------------------

OUTPUT:
--------

Sample Input

0 1
2 3
Sample Output

3
[[0 0]
 [2 3]]
