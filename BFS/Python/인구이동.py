n,l,r=map(int,input().split())

cnt=0
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    global visited
    visited[x][y]=1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n or visited[nx][ny]>-1:
            continue

        if l<=abs(graph[x][y]-graph[nx][ny])<=r:
            union_arr.append((nx,ny))
            dfs(nx,ny)

result=0            
while True: 
    visited=[[-1]*n for _ in range(n)]  
    # union_sum=[0]*2500
    # cnt=[0]*2500
    
    union=0
    for i in range(n):
        for j in range(n):
            cnt=0
            union_sum=0
            union_arr=[]
            if visited[i][j]==-1:
                union_arr.append((i,j))
                dfs(i,j)
                
                #어차피 방문처리 되있어서 가지 않으므로 연합한개 탐색 끝나면 그자리에서 다 바꾸기
                if len(union_arr)>1:
                    avg=sum([graph[x][y] for x,y in union_arr])//len(union_arr)
                    for x,y in union_arr:
                        graph[x][y]=avg
                union+=1

    if union==n*n:
        break
    result+=1
    # print(graph)
print(result)