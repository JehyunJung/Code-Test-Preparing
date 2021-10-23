import math
def exchange_money(n,money_types,target_money):
  d = [math.inf] * (target_money + 1)
  d[0]=0

  for i in range(money_types[0],target_money+1):
    for money_type in money_types:
      d[i]=min(d[i],d[i-money_type]+1)

  return d[target_money]

n,target_money=0,0
money_types=[]

with open("input.txt","r") as file:
  n,target_money=map(int,file.readline().split())
  for _ in range(n):
    money_types.append(int(file.readline()))

result=exchange_money(n,money_types,target_money)

if result == math.inf:
  print(-1)
else:
  print(result)
