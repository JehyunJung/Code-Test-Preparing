import heapq, math

def prim(v,graph,start_node):
  MST=[[] for _ in range(v+1)]
  distance=[math.inf] * (v+1)
  path=[-1] * (v+1)

  visited=[False] * (v+1)
  result=0
  edges=[]

  distance[start_node]=0
  heapq.heappush(edges,(0,start_node))

  for _ in range(v):
    cost,vertex=heapq.heappop(edges)
    visited[vertex]=True
    for weight,adj_vertex in graph[vertex]:

      if visited[adj_vertex]:
        continue

      if distance[adj_vertex] > weight:
        distance[adj_vertex]=weight
        path[adj_vertex]=vertex
        heapq.heappush(edges,(weight,adj_vertex))
        
  result=sum(distance[2:])
  for i in range(2,v+1):
    weight,vertex=distance[i],path[i]
    MST[i].append((weight,vertex))
    MST[vertex].append((weight,i))

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
  