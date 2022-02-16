import sys
input = sys.stdin.readline
n,k=map(int,input().split())

trip=[]
dp=[[0]*(k+1) for _ in range(n+1)]
for _ in range(n):
    w,v=map(int,input().split())
    trip.append((w,v))




for i in range(1,n+1):
    for j in range(1,k+1):
        w=trip[i-1][0]
        v=trip[i-1][1]
        if i<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j]+v)

        

print(dp[n][k])