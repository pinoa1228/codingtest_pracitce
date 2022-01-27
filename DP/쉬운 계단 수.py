n=int(input())

number=[[1]*10 for _ in range(n-1)]

if n==1:
    print(9)
    exit()
for i in range(2,9):
    number[0][i]=2

# 피보나치 수열 떠올림
for i in range(1,n-1):
    for j in range(10):
        # print(j)
        if j==0:
            number[i][j]=number[i-1][1]
        elif j==9:
            number[i][j]=number[i-1][j-1]
        else:
            number[i][j]=number[i-1][j-1]+number[i-1][j+1]        
print(sum(number[-1])%1000000000)
    