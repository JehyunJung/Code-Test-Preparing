N=0
times=[]
prizes=[]

with open("input33.txt","r") as file:
  N=int(file.readline())
  for _ in range(N):
    t,p=map(int,file.readline().split())
    times.append(t)
    prizes.append(p)

dp=[0] *(N+1)

for i in range(1,N+1):
  if dp[i]==0:
    dp[i]=dp[i-1]
  time=i+times[i-1]-1
  if time<=N:
    dp[time]=max(dp[time],dp[i-1]+prizes[i-1])
print(dp[N])


