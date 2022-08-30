from math import inf

def dfs(n,m):
    global dp
    if m==0:
        return 0

    if n<=0 :
        return -inf

    if dp[n][m] == -inf:

        dp[n][m]=dfs(n-1,m)

        if m==1:
            dp[n][m]=max(dp[n][m],prefix_sum[n])

        for k in range(n,-1,-1):
            if k-1 <0:
                break
            dp[n][m]=max(dp[n][m], dfs(k-2,m-1) + prefix_sum[n]-prefix_sum[k-1])

    return dp[n][m]

if __name__ == "__main__":
    N,M=0,0
    prefix_sum=[]
    dp=[]
    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Dynamic_Programming\\input2228.txt","r") as file:
        N,M=map(int,file.readline().split())
        prefix_sum.append(int(file.readline()))

        dp=[[-inf]*(M+1) for _ in range(N)]
        for _ in range(N-1):
            prefix_sum.append(prefix_sum[-1]+int(file.readline()))
    print(prefix_sum)
    print(dfs(N-1,M))