N=0
times=[0]
prizes=[0]

with open("input33.txt","r") as file:
  N=int(file.readline())
  for _ in range(N):
    t,p=map(int,file.readline().split())
    times.append(t)
    prizes.append(p)

dp=[0] *(N+1)

for i in range(1,N+1):

  check=False
  for j in range(5):
    target=i-j
    if target == 0:
      break
    if target+times[target]==i+1:
      dp[i]=max(dp[i],dp[i-times[target]]+prizes[target])
      check=True
  if not check:
    dp[i]=dp[i-1]
     

print(dp[N]) 


