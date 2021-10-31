def money_exchanger(target_money):
  for money in money_list:
    if money<=target_money:
      target_money-=money
    
  if target_money==0:
    return True

  return False

N=0
money_list=[]

with open("input4.txt","r") as file:
  N=int(file.readline())
  money_list=list(map(int,file.readline().split()))

money_list.sort()

target=1
for money in money_list:
  if target<money:
    break
  target+=money

print(target)