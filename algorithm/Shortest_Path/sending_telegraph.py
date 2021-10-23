import math,heapq
def dijkstra_path(graph,n,start_vertex):
  distance=[math.inf] * (n+1)

  heap=[]
  distance[start_vertex]=0
  heapq.heappush(heap,(0,start_vertex))
  while heap:
    weight,vertex=heapq.heappop(heap)

    if weight > distance[vertex]:
      continue
    for adj_vertex, weight in graph[vertex]:
      cost=distance[vertex] + weight
      
      if cost< distance[adj_vertex]:
        distance[adj_vertex]=cost
        heapq.heappush(heap,(cost,adj_vertex))

  return distance


n,m,start=0,0,0
graph=[]
with open("input2.txt","r") as file:
  n,m,start=map(int,file.readline().split())
  graph=[[] for _ in range(n+1)]

  for _ in range(m):
    vertex1, vertex2, weight=map(int,file.readline().split())
    graph[vertex1].append((vertex2,weight))

distance=dijkstra_path(graph,n,start)

count,max_cost=0,0

for vertex in range(1,n+1):
  temp=distance[vertex]
  if temp!=0 and temp !=math.inf:
    count+=1
    max_cost=max(max_cost,temp)

print(count, max_cost)

