from itertools import permutations
from math import inf
n=0
operands=[]
operators=[]
temp=[]
with open("input19.txt","r") as file:
  n=int(file.readline())
  operands=list(map(int,file.readline().split()))
  temp=list(map(int,file.readline().split()))

for idx in range(len(temp)):
  for j in range(temp[idx]):
    operators.append(idx)

min_sum=inf
max_sum=0

operators_permutations=list(set(permutations(operators,len(operators))))

for operator_list in operators_permutations:
  result,now=operands[0],0
  for index in range(len(operator_list)):
    now=operands[index+1]

    if operator_list[index]==0:
      result+=now
    elif operator_list[index]==1:
      result-=now
    elif operator_list[index]==2:
      result*=now
    elif operator_list[index]==3:
      result=int(result/now)

  min_sum=min(min_sum,result)
  max_sum=max(max_sum,result)

print(max_sum,min_sum,sep="\n")

