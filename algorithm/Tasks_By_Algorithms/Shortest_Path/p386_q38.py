from math import inf
vertex,edges=0,0
graph=[]

with open("input38.txt","r") as file:
  vertex,edges=map(int,file.readline().split())
  graph=[[inf]*(vertex+1) for _ in range(vertex+1)]
  for _ in range(edges):
    v1,v2=map(int,file.readline().split())
    graph[v1][v2]=1

for i in range(1,vertex+1):
  graph[i][i]=0

for k in range(1,vertex+1):
  for a in range(1,vertex+1):
    for b in range(1,vertex+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

result=0
for i in range(1,vertex+1):
  count=0
  for j in range(1,vertex+1):
    if i!=j and graph[i][j]!=inf or graph[j][i]!=inf:
      count+=1
  if count==vertex:
    result+=1

print(result)