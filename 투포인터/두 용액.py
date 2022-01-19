n=int(input())
liq=list(map(int,input().split()))

min_value=1e9
one=0
two=n-1
result=[]

liq.sort()

# print(liq)
if liq[0]>0:
    result.extend(liq[:2])
elif liq[-1]<0:
    result.extend(liq[-2:])
else:
    start=0
    end=n-1
    # 이건 start랑 end가 같아지기 전에 나와야한다.
    while start<end:
        if min_value==0:
            break
        # print(start,end)
        if abs(liq[start]+liq[end])<min_value:
            min_value=abs(liq[start]+liq[end])
            one=start
            two=end
            
        if abs(liq[start])>=abs(liq[end]):
            start+=1
        else:
            end-=1
    result.extend([liq[one],liq[two]])
    
print(result[0],result[1])
