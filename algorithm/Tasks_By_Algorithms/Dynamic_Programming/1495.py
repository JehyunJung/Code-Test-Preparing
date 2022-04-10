def solution():
  dp=[[-1] * (max_volume+1) for _ in range(n+1)]
  dp[0][start]=0

  for i in range(n):
    check=False
    for volume in range(max_volume+1):
      if dp[i][volume]==-1:
        continue
      check=True
      if (volume + volumes[i]) <= max_volume:
          dp[i+1][volume+volumes[i]]=0
      if (volume - volumes[i]) >=0:
          dp[i+1][volume-volumes[i]]=0
    if not check:
      break
  
  answer=-1
  for volume in range(max_volume+1):
    if dp[n][volume] !=-1:
      answer=volume
  return answer
  
if __name__ == "__main__":
  n,start,max_volume=0,0,0
  volumes=[]
  with open("input1495.txt","r") as file:
    n,start,max_volume=map(int,file.readline().split())
    volumes=list(map(int,file.readline().split()))
  print(solution())