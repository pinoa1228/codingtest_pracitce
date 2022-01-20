import heapq

#최소힙
heap=[]
t=int(input())
result=[]
for _ in range(t):
    k=int(input())
    for _ in range(k):
        oper,n=input().split()
        if oper=="I":
            heapq.heappush(heap,int(n))
        else:
            if not heap:
                continue
            if int(n)<0:
                heapq.heappop(heap)
            else:
                heap.pop(heap.index(max(heap)))

    if heap:
        # 마지막 꺼가 제일 큰 값이라는 것을 보장 못함
        print(max(heap),heap[0])
    else:
        print("EMPTY")