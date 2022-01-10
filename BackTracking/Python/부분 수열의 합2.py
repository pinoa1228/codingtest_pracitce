n,s=map(int,input().split())
numbers=list(map(int,input().split()))

cnt=0

def sum(index,total):
    global cnt
    
    if index>=n:
        return
    
    total+=numbers[index]
    if total==s:
        cnt+=1
        
    # 해당 인덱스를 선택한 경우
    sum(index+1,total)
    # 해당 인덱스를 선택하지 않은 경우
    sum(index+1,total-numbers[index])
    
    