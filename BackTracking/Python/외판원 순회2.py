n=int(input())
w=[]


for _ in range(n):
    w.append(list(map(int,input().split())))

def dfs(start,next,value,visited):
    global min_value
    
    if len(visited)==n:
        min_value=min(min_value,value+w[next][start])
        return
    
    for i in range(n):
        if w[next][i]!=0 and i!=start and i not in visited:
            #스택에 방문한 도시 넣고 다 돌면 빼기
            visited.append(i)
            dfs(start,i,value+w[next][i],visited)
            visited.pop()
            

min_value=1e9
for i in range(n):
    dfs(i,i,0,[i])
print(min_value)