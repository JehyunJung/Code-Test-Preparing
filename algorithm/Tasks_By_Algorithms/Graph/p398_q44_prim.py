from heapq import heappush,heappop
from math import inf

def distance(A,B):
  min_distance=inf
  for i in range(3):
    min_distance=min(min_distance,abs(A[i]-B[i]))

  return min_distance

num=0
graph=[0]

with open("input44.txt","r") as file:
  num=int(file.readline())
  for _ in range(num):
    graph.append(list(map(int,file.readline().split())))

visited=[False for _ in range(num+1)]
result=0

heap=[]
mst=[]
edge_count=0
visited[1]=True

for i in range(2,num+1):
  heappush(heap,(distance(graph[1],graph[i]),i))

while edge_count < num-1:
  cost,vertex=heappop(heap)
  if visited[vertex]:
      continue

  visited[vertex]=True
  result+=cost
  edge_count+=1

  for i in range(1,num+1):
    if i==vertex or visited[i]:
      continue
    heappush(heap,(distance(graph[vertex],graph[i]),i))

print(result)

    
    
