from collections import defaultdict
import sys
input = sys.stdin.readline

dict=defaultdict(list)
def change(time):
    h,m=time.split(":")
    return int(h)*60+int(m)
times = list(input().split())
S = int(times[0][:2]+times[0][3:])
E = int(times[1][:2]+times[1][3:])
Q = int(times[2][:2]+times[2][3:])
cnt=0
arr=[]
while True:
    # print(log)
    try:
        time,name=input().split()
        # print(time,name)
        time = int(time[:2]+time[3:])
        # print(change_result)
        if time<=S:
            dict[name]=1
        elif E<=time<=Q and dict[name]==1:
            cnt+=1
            #이거 생각 못함
            dict[name]=0
    except:
        break
        
print(cnt)
        
    