from math import inf
from copy import deepcopy
def solution():
  dp=[[inf] * 3 for _ in range(houses)]
  min_cost=inf

  # 첫번째 집 R
  dp[0]=deepcopy(paint_costs[0])
  dp[0][1]=inf
  dp[0][2]=inf

  for i in range(1,houses):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2]) + paint_costs[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2]) + paint_costs[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1]) + paint_costs[i][2]

  print(dp)
  min_cost=min(min_cost,dp[houses-1][1],dp[houses-1][2])

  # 첫번째 집 G
  dp[0]=deepcopy(paint_costs[0])
  dp[0][0]=inf
  dp[0][2]=inf

  for i in range(1,houses):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2]) + paint_costs[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2]) + paint_costs[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1]) + paint_costs[i][2]

  print(dp)
  min_cost=min(min_cost,dp[houses-1][0],dp[houses-1][2])

  # 첫번째 집 B
  dp[0]=deepcopy(paint_costs[0])
  dp[0][0]=inf
  dp[0][1]=inf

  for i in range(1,houses):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2]) + paint_costs[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2]) + paint_costs[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1]) + paint_costs[i][2]
  
  print(dp)
  min_cost=min(min_cost, dp[houses-1][0],dp[houses-1][1])

  return min_cost

if __name__ == "__main__":
  houses=0
  paint_costs=[]

  with open("input1149.txt","r") as file:
    houses=int(file.readline())
    for _ in range(houses):
      paint_costs.append(list(map(int,file.readline().split())))
  print(solution())