# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
eng=set(map(int,input().strip().split()))

m=int(input())
fre=set(map(int,input().strip().split()))

set1=eng.union(fre)
print(len(set1))
