from math import inf
def solution():
  dp=[inf] * (num)
  dp[0]=0
  for i in range(num):
    previous_block=blocks[i]
    for j in range(i+1,num):
      if previous_block=='B' and blocks[j]=='O' or previous_block=='O' and blocks[j]=='J' or previous_block=='J' and blocks[j]=='B':
        dp[j]=min(dp[i]+(j-i)**2,dp[j])

  if dp[num-1]==inf:
    print(-1)
  else:
    print(dp[num-1])
    
if __name__ == "__main__":
  num=0
  blocks=[]

  with open("input12026.txt","r") as file:
    num=int(file.readline())
    blocks=list(file.readline())
  solution()