def solution(n):
  dp=[False]*m
  index=0
  for i in range(1,6):
    dp[i]=True
    index+=1
    if index==n:
      return i


  for i in range(6,m):
    if i % 5==0 and dp[i//5]:
      dp[i]=True
    elif i % 3==0 and dp[i//3]:
      dp[i]=True
    elif i % 2==0 and dp[i//2]:
      dp[i]=True

    if dp[i]:
      index+=1
      if index==n:
        return i

n=0
m=1000
with open("input35.txt","r") as file:
  n=int(file.readline())

print(solution(n))
