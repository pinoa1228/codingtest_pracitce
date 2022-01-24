import heapq
import sys
input = sys.stdin.readline
n=int(input())

time=[]
heap=[]
for _ in range(n):
    a,b=map(int,input().split())
    time.append((a,b))

time.sort()


for a,b in time:
    if not heap:
        heapq.heappush(heap,b)
        continue
    if heap[0]<=a:
        heapq.heappop(heap)
        heapq.heappush(heap,b)
    else:
        heapq.heappush(heap,b)
print(len(heap))