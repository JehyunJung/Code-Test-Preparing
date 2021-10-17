import math
def dijkstra_path(graph,n,start_vertex,end_vertex):
  visited=[False] * (n+1)
  distance=[math.inf] * (n+1)

  distance[start_vertex]=0

  for i in range(n-1):
    min_distance=math.inf
    min_index=1

    for vertex in range(1,n+1):
      if not visited[vertex] and min_distance> distance[vertex]:
        min_index=vertex
        min_distance=distance[vertex]

    visited[min_index]=True
    for adj_vertex,weight in graph[min_index]:
      temp=distance[min_index] + weight
      if distance[adj_vertex] > temp:
        distance[adj_vertex]=temp

  return distance[end_vertex]

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

  distance=dijkstra_path(graph,n,start,n)

  if distance == math.inf:
    print("NO path")
  else:
    print("Shortest path: ", distance)