s=list(input())

check=False
temt=""
result=""
for i in s:
    if check==False:
        if i=="<":
            result+=temt[::-1]
            check=True
            temt=i
        elif i==" ":
            result+=temt[::-1]
            result+=" "
            temt=""
        else:
            temt+=i
    
    elif check:
        temt+=i
        if i==">":
            result+=temt
            temt=""
            check=False
        
            
print(result+temt[::-1])       