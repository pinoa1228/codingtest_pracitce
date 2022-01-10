from itertools import combinations

n,s=map(int,input().split())
numbers=list(map(int,input().split()))

cnt=0
for i in range(1,n+1):
    for number in list(combinations(numbers,i)):
        if sum(number)==s:
            cnt+=1
print(cnt)