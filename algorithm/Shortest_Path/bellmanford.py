import math, heapq
def bellman_ford(graph,n,start_vertex,end_vertex):
  distance=[math.inf] * (n+1)

  distance[start_vertex]=0
  
  for i in range(n):
    for vertex in range(1,n+1):
      for adj_vertex,weight in graph[vertex]:
        if distance[adj_vertex] > weight+ distance[vertex]:
          distance[adj_vertex] = weight+ distance[vertex]

          if i==n-1:
            return False

  return distance

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

  distance=bellman_ford(graph,n,start,n)
  print(distance)

