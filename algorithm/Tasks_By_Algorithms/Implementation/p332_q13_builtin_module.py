from math import inf
from itertools import combinations

n,m=0,0
homes=[]
stores=[]
result=inf

with open("input13.txt","r") as file:
  n,m=map(int,file.readline().split())
  for i in range(n):
    temp=list(map(int,file.readline().split()))
    for j in range(n):
      if temp[j] == 1:
        homes.append((i+1,j+1))
      elif temp[j] == 2:
        stores.append((i+1,j+1))


for combination in combinations(stores,m):
  sumOfDistances=0
  for home in homes:
    min_distance=inf
    for store in combination:
      min_distance=min(min_distance,abs(home[0]-store[0])+abs(home[1]-store[1]))
    sumOfDistances+=min_distance
  
  result=min(result,sumOfDistances)
print(result)