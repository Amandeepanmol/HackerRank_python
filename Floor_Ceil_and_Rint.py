import numpy
n=list(map(float,input().split()))
a=numpy.array(n)
numpy.set_printoptions(sign=" ")
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
------------------------------------------

OUTPUT:
-----------

Compiler Message
Success
Input (stdin)

1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Expected Output

[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
