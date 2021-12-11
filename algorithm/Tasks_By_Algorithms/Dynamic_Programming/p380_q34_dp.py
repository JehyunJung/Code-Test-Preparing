num=0
datas=[]

with open("input34.txt","r") as file:
  num=int(file.readline())
  datas=list(map(int,file.readline().split()))

datas.reverse()

dp=[1]*num

for i in range(1,num):
  for j in range(i):
    if datas[i]>datas[j]:
      dp[i]=max(dp[i],dp[j]+1)

print(num-max(dp))      