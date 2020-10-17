import numpy                               #importing numpy module
t=tuple(map(int,input().split()))       
a=numpy.zeros(t,dtype=int)                 #creates array filled with Zeros
b=numpy.ones(t,dtype=int)                  #creates array filled with Ones
print(a)
print(b)


----------------------------------------------------------
Output:
-----------
Compiler Message
Success
Input (stdin)
3 3 3
Expected Output
[[[0 0 0]
  [0 0 0]
  [0 0 0]]
 [[0 0 0]
  [0 0 0]
  [0 0 0]]
 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]
 [[1 1 1]
  [1 1 1]
  [1 1 1]]
 [[1 1 1]{-truncated-}
