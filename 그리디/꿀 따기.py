n=int(input())

bee=list(map(int,input().split()))
s=bee.copy()
honey=0
for i in range(1,n):
    s[i]+=s[i-1]
print(s)
result=0

#오른쪽
for i in range(1,n-1):
    result=max(result,2*s[-1]-bee[i]-s[i]-bee[0])  
#왼쪽
for i in range(1,n-1):
    result=max(result,s[-1]-bee[-1]+s[i-1]-bee[i])
   
for i in range(1,n-1):
    result=max(result,s[i]-bee[0]+s[-1]-s[i-1]-bee[-1])
    
print(result)
