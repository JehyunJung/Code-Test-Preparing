from collections import deque

graph=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited=[False] *9
queue=deque([1])
visited[1]=True

while queue:
  vertex=queue.popleft()
  print(vertex,end=" ")

  for adj_vertex in graph[vertex]:
    if not visited[adj_vertex]:
      queue.append(adj_vertex)
      visited[adj_vertex]=True
print()



