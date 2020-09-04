# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
eng=set(map(int,input().strip().split()))

b=int(input())
fre=set(map(int,input().strip().split()))

res=eng.difference(fre)
print(len(res))
