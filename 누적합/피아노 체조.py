import sys
input = sys.stdin.readline
n=int(input())
music=list(map(int,input().split()))
arr=[0]*(n)

cnt=0
for i in range(1,n):
    if music[i]-music[i-1]<0:
        cnt+=1
    arr[i-1]=cnt
 
q=int(input())
graph=[]
for _ in range(q):
    x,y=map(int,input().split())
    nx,ny=x-1,y-1
    # 첫번째가 틀릴 수 있는데 첫번째만 연주하면 0이 되어야한다
    if nx==0:
        if ny==0:
            print(0)
        else:
            print(arr[ny-1])
    else:
        print(arr[ny-1]-arr[nx-1])  

