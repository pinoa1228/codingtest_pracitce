import sys

T = int(sys.stdin.readline())

# print(s)
def second(start,end,s):
    while start<end:
        if s[start]==s[end]:
            start+=1
            end-=1
        else:
            return False
    return True
def is_palindrome(s):
    start=0
    end=len(s)-1
    while start<end:
        if s[start]==s[end]:
            start+=1
            end-=1
        else:
            check1=second(start+1,end,s)
            check2=second(start,end-1,s)
            
            if check1 or check2:
                return 1
            else:
                return 2
    return 0


for _ in range(T):
    print(is_palindrome(sys.stdin.readline().rstrip()))
    

        