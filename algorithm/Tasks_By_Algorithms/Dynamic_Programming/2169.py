import sys
def solution():
    dp=[[0] * m for _ in range(n)]

    dp[0][0]=values[0][0]

    #첫줄 처리
    for col in range(1,m):
        dp[0][col]=dp[0][col-1]+values[0][col]
    

    for row in range(1,n):
        left2right=[0]*m
        left2right[0]=dp[row-1][0]+values[row][0]

        for col in range(1,m):
            left2right[col]=max(dp[row-1][col],left2right[col-1])+values[row][col]
        
        right2left=[0]*m
        right2left[m-1]=dp[row-1][m-1]+values[row][m-1]

        for col in range(m-2,-1,-1):
            right2left[col]=max(dp[row-1][col],right2left[col+1])+values[row][col]
    

        for col in range(m):
            dp[row][col]=max(left2right[col],right2left[col])

    print(dp[-1][-1])

if __name__ == "__main__":
    sys.stdin=open("input2169.txT","r")
    n,m=map(int,input().split())
    values=[list(map(int,input().split())) for _ in range(n)]

    solution()