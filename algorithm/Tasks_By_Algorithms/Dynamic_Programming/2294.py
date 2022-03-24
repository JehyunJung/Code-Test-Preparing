from math import inf
def solution():
    dp=[-1] * (k+1)
    dp[0]=0
    
    if k < min(money_types):
        print(-1)
        exit(0)
        
    for i in range(1,k+1):
        temp=inf
        for money_type in money_types:
            prev_step=i-money_type
            if prev_step>=0:
                temp=min(temp,dp[prev_step])
        dp[i]=temp+1
    if dp[i]==inf:
      print(-1)
    else:
      print(dp[k])    

    
if __name__ =="__main__":
  n,k=0,0
  money_types=[]
  with open("input2294.txt","r") as file:
    n,k=map(int,file.readline().split())
    for _ in range(n):
      money_types.append(int(file.readline().strip()))
  solution()