from collections import deque

def topological_sort(v,graph,indegree):
  queue=deque()
  sorted_list=[]

  for i in range(1,v+1):
    if indegree[i]==0:
      queue.append(i)
  
  while queue:
    vertex=queue.popleft()
    sorted_list.append(vertex)
    for adj_vertex in graph[vertex]:
      indegree[adj_vertex]-=1

      if indegree[adj_vertex]==0:
        queue.append(adj_vertex)

  return sorted_list


if __name__ == "__main__":
  v,e=0,0
  graph=[]
  indegree=[]
  with open("data2.txt") as file:
    v,e=map(int,file.readline().split())
    graph=[[] for _ in range(v+1)]
    indegree=[0]*(v+1)
    for _ in range(e):
      v1,v2=map(int,file.readline().split())
      graph[v1].append(v2)
      indegree[v2]+=1
      
  print(topological_sort(v,graph,indegree))