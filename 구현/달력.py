
n=int(input())
graph=[0]*366

for _ in range(n):
    s,e=map(int,input().split())

    for i in range(s,e+1):
        graph[i]+=1    
    
max_v=0
cnt=0
result=0
for g in range(1,366):
    if graph[g]!=0:
        max_v=max(graph[g],max_v)
        cnt+=1
    elif cnt>0:
        # print(cnt,max_v)
        result+=max_v*cnt
        cnt=0
        max_v=0
result+=max_v*cnt
print(result)