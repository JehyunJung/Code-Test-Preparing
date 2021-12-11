from math import inf
import heapq
vertices,edges=0,0
graph=[]

with open("input40.txt","r") as file:
  vertices,edges=map(int,file.readline().split())
  graph=[[] for _ in range(vertices+1)]
  for _ in range(edges):  
    vertex1,vertex2=map(int,file.readline().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

distances=[inf for _ in range(vertices+1)]

heap=[]
distances[1]=0
heapq.heappush(heap,(0,1))

while heap:
  cost,vertex=heapq.heappop(heap)

  if distances[vertex] < cost:
    continue

  new_cost=cost+1
  for adj_vertex in graph[vertex]:
    if distances[adj_vertex] > new_cost:
      distances[adj_vertex]=new_cost
      heapq.heappush(heap,(new_cost,adj_vertex))

longest_vertex=max(distances[1:])
print(distances.index(longest_vertex),longest_vertex,distances.count(longest_vertex))

