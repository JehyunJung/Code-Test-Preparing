from collections import deque
def dfs(start,visited):
  visited[start]=True
  print(start,end=" ")
  
  for adj_vertex in graph[start]:
    if visited[adj_vertex]:
      continue
    dfs(adj_vertex,visited)
    
def bfs(start,visited):
  queue=deque()
  queue.append(start)
  visited[start]=True

  while queue:
    vertex=queue.popleft()
    print(vertex,end=" ")
    for adj_vertex in graph[vertex]:
      if visited[adj_vertex]:
        continue
      visited[adj_vertex]=True
      queue.append(adj_vertex)

if __name__ =="__main__":
  v,e,start=0,0,0
  graph=[]
  with open("input1260.txt","r") as file:
    v,e,start=map(int,file.readline().split())
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
      v1,v2=map(int,file.readline().split())
      graph[v1].append(v2)
      graph[v2].append(v1)

  graph=[sorted(nodes) for nodes in graph]
  dfs(start,[False for _ in range(v+1)])
  print()
  bfs(start,[False for _ in range(v+1)])
  print()
  