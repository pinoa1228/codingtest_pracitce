from collections import deque
n,m=map(int,input().split())
q=deque()
train=[[0]*20 for _ in range(n)]

for _ in range(m):
    arr=list(map(int,input().split()))
    if len(arr)==3:
        num,i,x=arr[0],arr[1],arr[2]
        if num==1:
            train[i-1][x-1]=1
        else:
            train[i-1][x-1]=0
    else:
        num,i=arr[0],arr[1]
        if num==3:
            q=deque(train[i-1])
            q.appendleft(0)
            train[i-1]=list(q)[:20]
        else:
            q=deque(train[i-1])
            q.popleft()
            q.append(0)
            train[i-1]=list(q)

be=[]
be.append(train[0])     
temp=0      
for i in train:
    if i not in be:
        be.append(i)

print(len(be))
            