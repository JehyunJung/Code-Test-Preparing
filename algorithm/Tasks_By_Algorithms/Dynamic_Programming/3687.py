from math import inf

def setMinNum():
    dp[2]=1
    dp[3]=7
    dp[4]=4
    dp[5]=2
    dp[6]=6
    dp[7]=8
    
    for i in range(8,101):
        for j in range(2,8):
            if j!=6:
                temp=dp[i-j]*10+dp[j]
            else:
                temp=dp[i-j]*10
            dp[i]=min(dp[i],temp)
    return dp

def solution(n):
    max_num=0
    if n %2==0:
        max_num=int("1"*(n//2))
    else:
        max_num=int("7"+"1"*(n//2 -1))
    
    print(dp[n],max_num)

if __name__ == "__main__":

    testcases=0
    dp=[inf]*101
    dp=setMinNum()

    with open("input3687.txt","r") as file:
        testcases=int(file.readline())
        for _ in range(testcases):
            n=int(file.readline())
            solution(n)



        