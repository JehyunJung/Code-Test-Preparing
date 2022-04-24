def solution(n,A,B,C):
    global dp
    if A<0 or B<0 or C<0:
        return 0
      
    if n==0:
        if A==0 and B==0 and C==0:
            return 1
        return 0

    if dp[n][A][B][C] !=-1:
        return dp[n][A][B][C]

    dp[n][A][B][C]=0

    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i+j+k==0:
                    continue
                dp[n][A][B][C]+=solution(n-1,A-i,B-j,C-k)
    
    dp[n][A][B][C] %= 1000000007
    return dp[n][A][B][C]
if __name__ == "__main__":
    inputs=[]
    with open("input12996.txt","r") as file:
        inputs=list(map(int,file.readline().split()))
    num=inputs[0]
    dp=[[[[-1]*51for _ in range(51)]for _ in range(51)]for _ in range(51)]
    solution(num,inputs[1],inputs[2],inputs[3])
    print(dp[num][inputs[1]][inputs[2]][inputs[3]])