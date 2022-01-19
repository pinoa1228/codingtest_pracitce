from collections import defaultdict
n,k=map(int,input().split())
an=list(map(int,input().split()))

dict=defaultdict(int)

start=0
end=0

max_len=0
while start<=end:
   
    if dict[an[end]]==k:
        # print(an[start])
        dict[an[start]]-=1
        max_len=max(max_len,end-start)
        start+=1
        # print(end-start)
    else:
        dict[an[end]]+=1
        end+=1
    if end>=n:
        # 마지막에 else문에 걸리는 경우도 있으니까 현재 있는 포인터로 최대값인지 한번더 확인 해줘야한다
        max_len=max(max_len,end-start)
        break

print(max_len)  
        
