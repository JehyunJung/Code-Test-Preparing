def solution():
    dp=[0] * (N+1)
    dp[0]=1
    types=[2**num for num in range(0,20) if 2**num <1000000]

    for type in types:
        for i in range(1,N+1):
            if i-type >=0:
                dp[i]+=dp[i-type]
            dp[i]%=1000000000
    return dp[N]

if __name__ == "__main__":
    N=0

    with open("input2410.txt","r") as file:
        N=int(file.readline())
    
    print(solution())