import sys
import heapq
input = sys.stdin.readline

n,k=map(int,input().split())

child=list(map(int,input().split()))

total=0
heap=[]
for i in range(1,n):

    temt=child[i]-child[i-1]
    #엣지 케이스 예외처리!!!!!!!
    if k==1:
        total+=temt
        continue
    
    if not heap or len(heap)<k-1:
        heapq.heappush(heap,temt)
    elif heap[0]<temt:
        total+=heap[0]
        heapq.heappop(heap)
        heapq.heappush(heap,temt)
    else:
        total+=temt

    

print(total)  
