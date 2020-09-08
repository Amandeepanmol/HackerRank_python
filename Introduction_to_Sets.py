def average(array):
    l1=set(array)
    return sum(l1)/len(l1)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
