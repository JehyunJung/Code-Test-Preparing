import heapq

def prim(v,graph,start_node):
  MST=[[] for _ in range(v+1)]
  visited=[False]*(v+1)
  result=0
  edge_count=0
  edges=[]

  visited[start_node]=True
  for weight,adj_vertex in graph[start_node]:
    heapq.heappush(edges,(weight,start_node,adj_vertex))

  while edge_count<v-1:
    cost,v1,v2=heapq.heappop(edges)

    if not visited[v2]:
      visited[v2]=True
      MST[v1].append((cost,v2))
      MST[v2].append((cost,v1))
      result+=cost
      edge_count+=1

      for weight,adj_vertex in graph[v2]:
        heapq.heappush(edges,(weight,v2,adj_vertex))
    else:
      continue

  return MST,result
    

if __name__ == "__main__":
  v,e=0,0
  graph=[]

  with open("data1.txt","r") as file:
    v,e=map(int,file.readline().split())
    graph=[[] for _ in range(v+1)]  
    for _ in range(e):
      v1,v2,cost=map(int,file.readline().split())
      graph[v1].append((cost,v2))
      graph[v2].append((cost,v1))
  MST,result=prim(v,graph,1)
  print(MST,result)
  