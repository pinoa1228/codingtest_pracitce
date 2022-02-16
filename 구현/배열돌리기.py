n,m,r=map(int,input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))
# visited=[[0]*m for _ in range(n)]
def rotate(n,m):
    global graph
    
    start=0
    end_m=m-1
    end_n=n-1

    for i in range((n+1)//2):
        # print(i)
        temt=graph[start][start]
        print(temt,start,i)
        for j in range(end_m):
            graph[start][j]=graph[start][j+1]
        
        temt2=graph[end_n][start]
        print(temt2)
        for j in range(start+2,end_n+1,-1):
            # print(graph[j-1][start])
            graph[j][start]=graph[j-1][start]
            
        graph[start+1][start]=temt
        
        temt3=graph[end_n][end_m]
        for j in range(1,end_m+1,-1):
            graph[end_n][j]=graph[end_n][j-1]
        graph[end_n][start-1]=temt2
        
        temt4=graph[start][end_m]
        for j in range(end_n):
            graph[j][end_m]=graph[j+1][end_m]
    
        graph[end_n-1][end_m]=temt3
        graph[start][end_m-1]=temt4
        
        start+=1
        end_m-=1
        end_n-=1
    return graph
        
for _ in range(r):
    rotate(n,m)  
    print(graph)    
  