def solution(money):
    answer = 0
    length=len(money)
    dp=[0 for _ in range(length)]
    
    dp[0]=money[0]
    dp[1]=money[0]
    
    for i in range(2,length-1):
        dp[i]=max(dp[i-1],dp[i-2]+money[i])
    answer=max(dp)
    
    dp=[0 for _ in range(length)]
    dp[1]=money[1]
    
    for i in range(2,length):
        dp[i]=max(dp[i-1],dp[i-2]+money[i])

    answer=max(answer,max(dp))
    return answer

if __name__ == "__main__":
    money=[]
    with open("level3_4.txt","r") as file:
      money=list(map(int,file.readline().split()))
    print(solution(money))