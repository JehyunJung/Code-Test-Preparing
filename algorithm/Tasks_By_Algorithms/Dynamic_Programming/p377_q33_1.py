times=[]
prizes=[]
N=0
with open("input33.txt","r") as file:
  N=int(file.readline())
  for _ in range(N):
    t,p=map(int,file.readline().split())
    times.append(t)
    prizes.append(p)

dp=[0] *(N+1)
max_value=0

for i in range(N-1,-1,-1):
    time=times[i]+i
    if time <= N:
        dp[i]=max(prizes[i]+dp[time],max_value)
        max_value=dp[i]
    else:
        dp[i]=max_value
print(dp)
        
print(max_value) 


