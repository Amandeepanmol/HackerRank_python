cube = lambda x:x*x*x 

def fibonacci(n):
    f=0
    s=1
    l1=[]
    if n<=0:
        return []
    elif n==1:
        l1.append(f)
    else:
        l1.append(f)
        l1.append(s)
        for i in range(2,n):
            t=f+s
            f=s
            s=t
            l1.append(t)
    return l1

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
