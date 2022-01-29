from math import inf
def solution():
  dp=[[inf] * 3 for _ in range(houses)]
  dp[0]=paint_costs[0]
  for i in range(1,houses):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2]) + paint_costs[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2]) + paint_costs[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1]) + paint_costs[i][2]

  return min(dp[houses-1])

if __name__ == "__main__":
  houses=0
  paint_costs=[]

  with open("input1149.txt","r") as file:
    houses=int(file.readline())
    for _ in range(houses):
      paint_costs.append(list(map(int,file.readline().split())))
  print(solution())