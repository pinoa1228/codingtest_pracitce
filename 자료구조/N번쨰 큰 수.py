import heapq
n=int(input())

heap=list(map(int,input().split()))
heapq.heapify(heap)

for _ in range(1,n):
    graph=list(map(int,input().split()))
    for j in range(n):
        if graph[j]>heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,graph[j])

print(heap[0])