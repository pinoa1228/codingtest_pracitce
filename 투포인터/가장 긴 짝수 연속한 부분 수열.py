
n,k=map(int,input().split())
s=list(map(int,input().split()))

start=0
end=0
cnt=0
result=0
# check=True
while start<=end:
    if s[end]%2==1:
        if cnt<k:
            # check=True
            cnt+=1
            end+=1
        else:
            # check=False
            if s[start]%2==1:
                cnt-=1
            start+=1
    else:
        # check=True
        end+=1
    if cnt<=k:
        result=max(result,end-start)
    if end>=n:
        break

print(result-cnt)