def solution():
    dp=[[0]*(num+1) for _ in range(4)]

    for i in range(1,4):
        for j in range(i*max_carry,num+1):
            dp[i][j]=max(dp[i][j-1],dp[i-1][j-max_carry]+cum_passengers[j]-cum_passengers[j-max_carry])
        print(dp[i])
  
    return max(dp[3])   

    
if __name__ == "__main__":
    num=0
    passengers=[]
    max_carry=0
    with open("input2616.txt","r") as file:
        num=int(file.readline())
        passengers=list(map(int,file.readline().split()))
        max_carry=int(file.readline())
    cum_passengers=[0]*(num+1)
    for i in range(1,num+1):
        cum_passengers[i]=cum_passengers[i-1]+passengers[i-1]
      
    answer=solution()
    print(answer)