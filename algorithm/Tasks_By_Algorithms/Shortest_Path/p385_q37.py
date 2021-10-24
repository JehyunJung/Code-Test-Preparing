import math

def floyd_warshall(v,graph):
  for k in range(1,v+1):
    for a in range(1,v+1):
      for b in range(1,v+1):
        graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

v,e=0,0
graph=[]

with open("input37.txt","r") as file:
  v=int(file.readline())
  e=int(file.readline())
  graph=[[math.inf for _ in range(v+1)] for _ in range(v+1)]
  for i in range(1,v+1):
    for j in range(1,v+1):
      if i==j:
        graph[i][j]=0

  for _ in range(e):
    v1,v2,cost=map(int,file.readline().split())
    if cost<graph[v1][v2]:
      graph[v1][v2]=cost

    
floyd_warshall(v,graph)

for i in range(1,v+1):
  for j in range(1,v+1):
    if graph[i][j]==math.inf:
      graph[i][j]=0
    print(graph[i][j],end=" ")
  print()