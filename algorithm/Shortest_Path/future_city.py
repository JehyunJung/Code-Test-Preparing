from floyd_warshall_alogirthm import floyd_warshall_path
import math

n,m,x,k=0,0,0,0
graph=[]
with open("input.txt","r") as file:
  n,m=map(int,file.readline().split())
  graph=[[] for _ in range(n+1)]
  for a in range(m):
    vertex1,vertex2=map(int,file.readline().split())
    graph[vertex1].append((vertex2,1))
    graph[vertex2].append((vertex1,1))

  x,k=map(int,file.readline().split())

distance=floyd_warshall_path(graph,n)

cost=distance[1][k] + distance[k][x]

if cost >= math.inf:
  print(-1)
else:
  print(cost)
