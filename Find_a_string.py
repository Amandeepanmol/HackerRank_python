def count_substring(string, sub_string):
    start=0
    c=0
    while(start<len(string)):
        x=string.find(sub_string,start)
        if x!=-1:
            start=x+1
            c+=1
        else:
            break
    return c  

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
