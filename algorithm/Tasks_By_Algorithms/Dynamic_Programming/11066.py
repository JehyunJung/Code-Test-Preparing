from math import inf
def solution():
    dp=[[0] * (num) for _ in range(num)]
    accu_list=[0]*(num+1)
    for i in range(1,num+1):
        accu_list[i]=accu_list[i-1]+files[i-1]

    for diagonal in range(1,num):
        for i in range(num-diagonal):
            j=i+diagonal
            
            if diagonal==1:
                dp[i][j]=accu_list[j+1]-accu_list[i]
                continue

            dp[i][j]=inf

            for k in range(i,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+accu_list[j+1]-accu_list[i])
    print(dp[0][-1])

if __name__ == "__main__":
    testcases=0
    num=0
    files=[]
    with open("input11066.txt","r") as file:
        test_cases=int(file.readline().strip())
        for _ in range(test_cases):
            num=int(file.readline().strip())
            files=list(map(int,file.readline().split()))
            solution()
  