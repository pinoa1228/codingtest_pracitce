from collections import defaultdict

import sys
input=sys.stdin.readline

dict=defaultdict(int)
total=0
while True:
    log=input().rstrip()
    if not log:
        break
   
    total+=1
    dict[log]+=1

# 처음에는 그냥 dictionary에 있는거 다 계산해서 다시 박고 그담에 다시 출력하는 포문 돌릴려함-> 시간복잡도가 N 증가함
# dict key값 기준으로 정렬하기-> 아니면 키 값만 list로 만들어서 정렬시키기
dict=sorted(dict.items())     

for d in dict:
    # 반올림 넷째자리까지-> round쓰면 틀림 왜일까..?
    print('%s %.4f' %(d[0],d[1]*100/total))

    