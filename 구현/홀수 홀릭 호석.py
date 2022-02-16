n=input()

total=0

def isOdd(n):
    cnt=0
    # print(n)
    new=str(n)
    for i in range(len(new)):
        if int(new[i])%2==1:
            cnt+=1
    return cnt
    
    
def go(n,total):
    
    n=str(n)
    global min_v,max_v
    if len(n)==1:
        if int(n)%2==1:
            total+=1
        return total
    if len(n)==2:
        n=int(n[0])+int(n[1])
        go(n,total+isOdd(n))

            
    target=0
    # print(n)
    for i in range(1,len(n)):
        target=int(n[:i])
        for j in range(i+1,len(n)):
            target+=int(n[i:j])
            target+=int(n[j:])
            # print(target)
            result=go(target,total+isOdd(target))
            print(result)
            min_v=min(result,min_v)
            max_v=max(result,max_v)

min_v=1e9
max_v=0           
    
go(n,isOdd(n))

print(min_v,max_v)