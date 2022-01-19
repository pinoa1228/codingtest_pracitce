from itertools import combinations
import copy
n,m=map(int,input().split())
graph=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

zero_list=[]
two_list=[]
len_one=0
for _ in range(n):
    arr=list(map(int,input().split()))
    for k in range(m):
        if arr[k]==0:
            zero_list.append((_,k))
        elif arr[k]==1:
            len_one+=1
        else:
            two_list.append((_,k))
    graph.append(arr)
   
def dfs(x,y,temt):
    global cnt,visited
    temt[x][y]=2
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m or temt[nx][ny]==1 or visited[nx][ny]==1:
            continue
        cnt+=1
        dfs(nx,ny,temt)

answer=0
for k in list(combinations(zero_list,3)):
    # 2차원 배열 복사
    temt=copy.deepcopy(graph)
    for t in range(3):
        temt[k[t][0]][k[t][1]]=1
    total=0
    visited=[[0]*m for _ in range(n)]
    for i,j in two_list:
        cnt=1
        if visited[i][j]==0:
            dfs(i,j,temt)
            total+=cnt
    result=(n*m)-(total+len_one+3)
    answer=max(answer,result)

print(answer)
            