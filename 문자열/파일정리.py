from collections import defaultdict
n=int(input())
dict=defaultdict(int)
for _ in range(n):
    a,b=input().split(".")
    dict[b]+=1
dict2=sorted(dict.items())

for a,b in dict2:
    print(a,b)
