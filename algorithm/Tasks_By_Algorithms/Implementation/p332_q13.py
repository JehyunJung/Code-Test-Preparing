from math import inf
def solution(temp_stores,count):
  global result
  for i in range(len(stores)):
    if count==m:
      sumOfDistances=0
      for home in homes:
        min_distance=inf
        for store_index in temp_stores:
          min_distance=min(min_distance,abs(home[0]-stores[store_index][0])+abs(home[1]-stores[store_index][1]))
        sumOfDistances+=min_distance
      
      result=min(result,sumOfDistances)
      print(temp_stores,sumOfDistances)
      return

    if (i in temp_stores) or (len(temp_stores)>0 and i < temp_stores[-1]):
      continue  
    solution(temp_stores+[i],count+1)

  return result

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
print(solution([],0))