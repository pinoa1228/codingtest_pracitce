from collections import defaultdict
import sys
input = sys.stdin.readline

s,e,q=input().split()

dict=defaultdict(list)
def change(time):
    h,m=time.split(":")
    return int(h)*60+int(m)

s_time=change(s)
e_time=change(e)
q_time=change(q)

while True:
    try:
        time,name=input().split()
        change_result=change(time)
        if change_result<=s_time:
            if "i" in dict[name]:
                continue
            dict[name].append("i")
        elif e_time<=change_result<=q_time:
            if "o" in dict[name]:
                continue
            dict[name].append("o")
    except :
        break
        
# print(dict)
cnt=0
for d in dict.values():
    if d==["i","o"]:
        cnt+=1
print(cnt)
        
    