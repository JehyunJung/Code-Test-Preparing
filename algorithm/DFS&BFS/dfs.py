def dfs(vertex):
  visited[vertex]=True
  print(vertex,end=" ")

  for adj_vertex in graph[vertex]:
    if not visited[adj_vertex]:
      dfs(adj_vertex)

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
start_vertex=0

dfs(1)
print()



