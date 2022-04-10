def solution():
  dp=[i for i in range(num+1)]

  for i in range(7,num+1):
    dp[i]=max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)
  print(dp)
  return dp[num]
if __name__ == "__main__":
  num=0
  with open("input11058.txt","r") as file:
    num=int(file.readline())
  print(solution())