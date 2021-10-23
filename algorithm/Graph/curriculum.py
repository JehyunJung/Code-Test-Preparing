from collections import deque
import copy 

def topological_sort(v,graph,indegrees,weight):
  distance=copy.deepcopy(weight)
  queue=deque()
  for i in range(1,v+1):
    if indegrees[i] ==0:
      queue.append(i)

  while queue:
    vertex=queue.popleft()
    for adj_vertex in graph[vertex]:
      distance[adj_vertex]=max(distance[adj_vertex],weight[adj_vertex]+distance[vertex])
      indegrees[adj_vertex]-=1

      if indegrees[adj_vertex] ==0:
        queue.append(adj_vertex)
  return distance

v=0
graph,indegrees,weight=[],[],[]

with open("input3.txt","r") as file:
  v=int(file.readline())

  graph=[[] for _ in range(v+1)]
  weight=[[] for _ in range(v+1)]
  indegrees=[0]*(v+1)

  for i in range(1,v+1):
    input_data=list(map(int,file.readline().split()))
    weight[i]=input_data[0]

    for adj_vertex in input_data[1:-1]:
      graph[adj_vertex].append(i)
      indegrees[i]+=1

  result=topological_sort(v,graph,indegrees,weight)
  print(result[1:])
  