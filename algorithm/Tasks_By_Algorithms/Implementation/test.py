def solution():
    dp=[0]*51
    dp[2]=1
    dp[3]=1
    dp[4]=1
    dp[5]=3
    dp[6]=3
    dp[7]=1
    k=11
    for i in range(k+1):
        #1
        if i-2>=2:
            dp[i]+=dp[i-2]
        #7
        if i-3>=2:
            dp[i]+=dp[i-3]
        #4
        if i-4>=2:
            dp[i]+=dp[i-4]
        #2,3,5  
        if i-5>=2:
            dp[i]+=dp[i-5]*3
        #0,6,9
        if i-6>=2:
            dp[i]+=dp[i-6]*2
        #8

        if i-7>=2:
            dp[i]+=dp[i-7]
        #10
        if i-8>=2:
            dp[i]+=dp[i-8]
    print(dp)
    return dp[k]


if __name__ == "__main__":
    print(solution())

