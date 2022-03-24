def solution():
  dp=[0] * (k+1)
  dp[0]=1
  for money_type in money_types:
    for i in range(1,k+1):
      prev_step=i-money_type
      if prev_step >=0:
        dp[i]+=(dp[prev_step])

  print(dp[k])    
    
if __name__ =="__main__":
  n,k=0,0
  money_types=[]
  with open("input2293.txt","r") as file:
    n,k=map(int,file.readline().split())
    for _ in range(n):
      money_types.append(int(file.readline().strip()))
  solution()