n=int(input())
energe=[]
for _ in range(n-1):
    x,y=map(int,input().split())
    energe.append((x,y))
k=int(input())



def go(start,end,dp):
    for i in range(start,end):
        if i==n-2:
            dp[i+1]=min(dp[i+1],dp[i]+energe[i][0])
        else:
            dp[i+1]=min(dp[i+1],dp[i]+energe[i][0])
            dp[i+2]=min(dp[i+2],dp[i]+energe[i][1])
    return dp[-1]
            
answer=1e9
for i in range(n-3):
    dp=[1e9]*n
    dp[0]=0
    if i>=1:
        go(0,i,dp)
    dp[i+3]=min(dp[i]+k,dp[i+3])
    result=go(i,n-1,dp)
    answer=min(answer,result)
dp=[1e9]*n
dp[0]=0
print(min(answer,go(0,n-1,dp)))

