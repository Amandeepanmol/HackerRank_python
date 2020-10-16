import numpy                                 #importing numpy module

def arrays(arr):
    # complete this function
    # use numpy.array
    a=numpy.array(arr,dtype=float)           #using dtype to convert value in float
    return a[::-1]                       #reversing array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


-----------------------------------------------------------

OUTPUT
------------
Compiler Message
Success
Input (stdin)
1 2 3 4 -8 -10
Expected Output
[-10.  -8.   4.   3.   2.   1.]
