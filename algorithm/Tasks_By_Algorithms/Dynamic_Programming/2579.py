def solution():
    dp=[0] * (num+1) 
    dp[1]=stairs[1]
    
    if num==1:
        return dp[1]
    
    dp[2]=stairs[1]+stairs[2]
    
    if num==2:
        return dp[2]

    for i in range(3,num+1):
        dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])
        
    return dp[-1]

if __name__ =="__main__":
    num=0
    stairs=[]
    with open("input2579.txt","r") as file:
        num=int(file.readline())

        stairs=[int(file.readline()) for _ in range(num)]
    stairs.insert(0,0)
    solution()