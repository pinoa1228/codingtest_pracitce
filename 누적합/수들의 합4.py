from collections import defaultdict
import sys
# import math
# import time

input = sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))

dict=defaultdict(int)
cnt=0

for i in range(n):
    if i==0:
        if a[0]==k:
            cnt+=1
        dict[a[0]]=1
        continue
    a[i]+=a[i-1]
    if a[i]==k:
        cnt+=1
    if a[i]-k in dict.keys():
        cnt+=dict[a[i]-k] 
    dict[a[i]]+=1

print(cnt) 

