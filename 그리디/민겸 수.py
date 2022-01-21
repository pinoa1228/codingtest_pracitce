s=list(input())
result=[]
result_min=[]

start=0
def count(result):
    answer=""
    # print(result)
    for target in result:
        m_count=list(target).count("M")    
        if m_count==len(target):
            total=10**(m_count-1)
        else:
            total=10**m_count*5
            
        answer+=str(total)
        # print(answer,total)
    return answer

for i in range(len(s)):
    if s[i]=="K":
        result.append(s[start:i+1])
        if start!=i:
            result_min.append(s[start:i])
        result_min.append([s[i]])
        start=i+1
    elif i==len(s)-1:
        result.extend(s[start:])
        result_min.append(s[start:])
print(result)
        
        
# print(result_min)

answer_max=count(result)
answer_min=count(result_min)
print(answer_max,answer_min)