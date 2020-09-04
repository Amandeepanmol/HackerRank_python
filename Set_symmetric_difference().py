n=int(input())
eng=set(map(int,input().strip().split()))

b=int(input())
fre=set(map(int,input().strip().split()))

res=eng.symmetric_difference(fre)
print(len(res))
