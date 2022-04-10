def solution():
  dp=[[0]*(max_weight+1) for _ in range(n+1)]

  for i in range(1,n+1):
    weight,prize=weights[i],prizes[i]
    for remaining_weight in range(max_weight+1):
      if weight <= remaining_weight:
        dp[i][remaining_weight]=max(dp[i-1][remaining_weight],dp[i-1][remaining_weight-weight]+prize)
      else:
        dp[i][remaining_weight]=dp[i-1][remaining_weight]

  print(dp[n][max_weight])


if __name__ == "__main__":
  n,max_weight=0,0
  weights=[0]
  prizes=[0]
  with open("input12865.txt","r") as file:
    n,max_weight=map(int,file.readline().split())
    for _ in range(n):
      weight,prize=map(int,file.readline().split())
      weights.append(weight)
      prizes.append(prize)
  
  solution()