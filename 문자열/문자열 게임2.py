import sys
from collections import defaultdict

def game(s,k):

    alpha = defaultdict(list)
    max_str=0
    min_str=1e9

    for i in range(len(s)):
        if s.count(s[i])>=k:
            alpha[s[i]].append(i)
    
    if not alpha:
        print(-1)
        return
            
    for v_list in alpha.values():
        for j in range(len(v_list)-k+1):
            temt=v_list[j+k-1]-v_list[j]+1
            #시간초과남 내장함수 쓰면
            if temt < min_str: min_str = temt 
            if temt > max_str: max_str = temt


    print(min_str,max_str)
            
        
    
T = int(sys.stdin.readline()) 
for t in range(1, T+1): 
    string = sys.stdin.readline().strip() 
    K = int(sys.stdin.readline()) 
    game(string,K)

