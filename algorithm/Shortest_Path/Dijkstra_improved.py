import math, heapq
def dijkstra_path(graph,n,start_vertex,end_vertex):
  distance=[math.inf] * (n+1)
  path=[-1] * (n+1)

  heap=[]
  heapq.heappush(heap,(0,start_vertex))
  distance[start_vertex]=0

  while heap:
    weight,vertex=heapq.heappop(heap)
    if distance[vertex] < weight:
      continue
    for adj_vertex,weight in graph[vertex]:
      temp=distance[vertex] + weight
      if distance[adj_vertex] > temp:
        distance[adj_vertex]=temp
        path[adj_vertex]=vertex
        heapq.heappush(heap,(temp,adj_vertex))
  print(distance) 
  return distance[end_vertex],path

def print_path(path,node):
  if node != -1:
    print_path(path,path[node])
    print(node,end=" ")

if __name__ =="__main__":
  n=0
  graph=[]
  start=0
  with open("data.txt","r") as file:
    n,m=map(int,(file.readline().split()))
    start=int(file.readline())
    graph=[[] for _ in range(n+1)]
    for vertex in range(m):
      vertex1, vertex2, weight=map(int,file.readline().split())
      graph[vertex1].append((vertex2, weight))

  distance,path=dijkstra_path(graph,n,start,n)

  if distance == math.inf:
    print("NO path")
  else:
    print("Shortest path: ", distance)
  
  print("path: ",end=" ")
  print_path(path,n)
  print()
