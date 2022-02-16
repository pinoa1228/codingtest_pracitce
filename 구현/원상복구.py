n,k=map(int,input().split())
s=list(map(int,input().split()))
d=list(map(int,input().split()))


for _ in range(k):
    p=[0]*n
    for i in range(n):
        p_index=d[i]-1
        p[p_index]=s[i]
    s=p

print(*p)
# for i in range(n):
#     print(p[i],end=" ")

