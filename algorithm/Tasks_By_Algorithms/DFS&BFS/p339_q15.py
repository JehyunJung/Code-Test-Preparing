from collections import deque

def bfs(v,graph,start_node):
  visited=[False] * (v+1)
  distance=[0] * (v+1)
  queue=deque()

  distance[start_node]=0
  visited[start_node]=True
  queue.append(start_node)

  while queue:
    vertex=queue.popleft()
    for adj_vertex in graph[vertex]:
      if not visited[adj_vertex]:
        distance[adj_vertex]=distance[vertex]+1
        visited[adj_vertex]=True
        queue.append(adj_vertex)
  
  return distance


v,e,k,start_node=0,0,0,0
graph=[]

with open("input15.txt","r") as file:
  v,e,k,start_node=map(int,file.readline().split())
  graph=[[] for _ in range(v+1)]
  for _ in range(e):
    v1,v2=map(int,file.readline().split())
    graph[v1].append(v2)
  
distance=bfs(v,graph,start_node)
count=0

for i in range(1,v+1):
  if distance[i] == k:
    count+=1
    print(i)
    
if count==0:
    print(-1)