import heapq
from math import inf

def dijkstra(n,graph):
  distances=[[inf]*(n) for _ in range(n)]
  queue=[]
  dy=[-1,0,1,0]
  dx=[0,1,0,-1]

  distances[0][0]=graph[0][0]
  heapq.heappush(queue,(distances[0][0],0,0))

  while queue:
    cost,y,x=heapq.heappop(queue)

    for i in range(4):
      new_y=y+dy[i]
      new_x=x+dx[i]

      if new_x <0 or new_x >=n or new_y <0 or new_y >=n:
        continue
        
      temp=cost+graph[new_y][new_x]
      if temp < distances[new_y][new_x]:
        distances[new_y][new_x]=temp
        heapq.heappush(queue,(temp,new_y,new_x))
  return distances

test_cases=0
n=0

with open("input39.txt","r") as file:
  test_cases=int(file.readline())
  for _ in range(test_cases):
    graph=[]
    n=int(file.readline())
    
    for _ in range(n):
      graph.append(list(map(int,file.readline().split())))
    
    distances=dijkstra(n,graph)
    print(distances[n-1][n-1])


