def solution():
  dp=[0 for _ in range(n+1)]
  max_prize=0
  for i in range(n-1,-1,-1):
    time,prize=schedules[i][0],schedules[i][1]
    if i+time <=n:
      dp[i]=max(max_prize,dp[i+time]+prize)
      max_prize=dp[i]
      
    else:
      dp[i]=max_prize
  print(max_prize)

if __name__ == "__main__":
  n=0
  schedules=[]
  with open("input15486.txt","r") as file:
    n=int(file.readline())
    schedules=[list(map(int,file.readline().split())) for _ in range(n)]
  solution()