if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        x=input().split(" ")
        operation=x[0]
        if(operation=="insert"):
            l.insert(int(x[1]),int(x[2]))
        if(operation=="remove"):
            l.remove(int(x[1]))
        if(operation=="append"):
            l.append(int(x[1]))
        if(operation=="sort"):
            l.sort()
        if(operation=="pop"):
            if(len(l)!=0):
                l.pop()
        if(operation=="reverse"):
            l.reverse()
        if(operation=="print"):
            print(l)    

-------------------------------------------------

OUTPUT:
--------

Compiler Message
Success
Input (stdin)

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Expected Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
