n,k=map(int,input().split())

dp=[0]*(k+1)
# 동전 한개만 쓸때
dp[0]=1
number=[]
for _ in range(n):
    number.append(int(input()))

#k까지 더하는 경우의 수를 구해 간다.
for i in number:
    for j in range(i,k+1):
        if j>=i:
            dp[j]+=dp[j-i]
    