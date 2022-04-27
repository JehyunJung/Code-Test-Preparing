def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (m+1) for _ in range(n+1)]
        
    for x,y in puddles:
        dp[y][x]=-1

    dp[1][1]=1
    
    for y in range(1,n+1):
        for x in range(1,m+1):
            if y==1 and x==1:
                continue

            if dp[y][x]==-1:
                dp[y][x]=0
                continue
                
            dp[y][x]=(dp[y-1][x]+dp[y][x-1])%1000000007
            
    answer=dp[n][m]
    
    return answer

if __name__ == "__main__":
    m,n,k,puddles=0,0,0,[]
    with open("level3_3.txt","r") as file:
        m,n,k=map(int,file.readline().split())
        puddles=[list(map(int,file.readline().split())) for _ in range(k)]
    print(solution(m,n,puddles))
        