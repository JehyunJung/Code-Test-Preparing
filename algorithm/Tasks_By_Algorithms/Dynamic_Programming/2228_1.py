from math import inf

def solution():
    dp=[[-inf]*(M+1) for _ in range(N)]

    for i in range(N):
        for j in range(M+1):
            if j==0:
                dp[i][j]=0
                continue

            dp[i][j]=dp[i-1][j]

            if j==1:
                dp[i][j]=max(dp[i][j],prefix_sum[i])
                continue
            
            for k in range(i,-1,-1):
                if k-2 <0:
                    continue
                dp[i][j]=max(dp[i][j],dp[k-2][j-1]+prefix_sum[i]-prefix_sum[k-1])
    
    print(dp)
    return dp[N-1][M]


if __name__ == "__main__":
    N,M=0,0
    prefix_sum=[]
    with open("input2228.txt","r") as file:
        N,M=map(int,file.readline().split())
        prefix_sum.append(int(file.readline()))

        for _ in range(N-1):
            prefix_sum.append(prefix_sum[-1]+int(file.readline()))

    print(solution())