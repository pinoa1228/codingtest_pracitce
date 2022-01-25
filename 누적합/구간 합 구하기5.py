n,m=map(int,input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(1,n):
        graph[i][j]+=graph[i][j-1]
        
for i in range(1,n):
    for j in range(n):
        graph[i][j]+=graph[i-1][j]

print(graph)
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    if x1==1 and y1==1:
        print(graph[x2-1][y2-1])
        continue
    if x1==1:
        print(graph[x2-1][y2-1]-graph[x2-1][y1-2])
    elif y1==1:
        print(graph[x2-1][y2-1]-graph[x1-2][y2-1])
    else:
        print(graph[x2-1][y2-1]-graph[x1-2][y2-1]-graph[x2-1][y1-2]+graph[x1-2][y1-2])
