from math import inf
def solution():
    dp=[[0] * (num+1) for _ in range(num+1)]
    for diagonal in range(1,num+1):
        for i in range(0,num-diagonal):
            j=i+diagonal
            if diagonal==1:
                dp[i][j]=matrices[i][0]*matrices[i][1]*matrices[j][1]
                continue
            dp[i][j]=inf
            
            for k in range(i,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+matrices[i][0]*matrices[k][1]*matrices[j][1])
    print(dp[0][num-1])
  
if __name__ == "__main__":
    num=0
    matrices=[]
    with open("input11049.txt","r") as file:
        num=int(file.readline())
        matrices=[list(map(int,file.readline().split())) for _ in range(num)]
    solution()