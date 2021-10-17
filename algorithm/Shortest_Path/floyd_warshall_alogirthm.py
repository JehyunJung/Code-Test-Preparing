import math
def floyd_warshall_path(graph,n):
  distance=[[math.inf] * (n+1) for _ in range(n+1)]

  for a in range(1,n+1):
    distance[a][a]=0

  for vertex in range(1,n+1):
    for adj_vertex,weight in graph[vertex]:
      distance[vertex][adj_vertex]=weight
        
  for k in range(1,n+1):
    for a in range(1,n+1):
      for b in range(1,n+1):
        distance[a][b]=min(distance[a][b],distance[a][k] + distance[k][b])
  
  return distance

def print_weight(distance):
  for a in range(1,n+1):
    print(distance[a][1:])


if __name__ =="__main__":
  n=0
  graph=[]
  start=0
  with open("data1.txt","r") as file:
    n,m=map(int,(file.readline().split()))
    graph=[[] for _ in range(n+1)]
    for vertex in range(m):
      vertex1, vertex2, weight=map(int,file.readline().split())
      graph[vertex1].append((vertex2, weight))

  print_weight(floyd_warshall_path(graph,n))