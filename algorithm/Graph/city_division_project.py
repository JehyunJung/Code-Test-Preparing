from disjoin_sets import union_parent, find_parent_compressed
import heapq

def kruskal(v,edges):
  parents=[i for i in range(v+1)]
  MST=[[] for _ in range(v+1)]
  result,max_weight=0,0
  edge_count=0

  while edge_count < v-1:
    cost,vertex1,vertex2=heapq.heappop(edges)

    if find_parent_compressed(parents,vertex1) != find_parent_compressed(parents,vertex2):
      union_parent(parents,vertex1,vertex2)
      MST[vertex1].append(vertex2)
      MST[vertex2].append(vertex1)
      result+=cost
      max_weight=max(cost,max_weight)
      edge_count+=1

    else:
      continue
  
  result-=max_weight
  return MST,result


v,e=0,0
edges=[]
result,weight=0,0
with open("input2.txt","r") as file:
  v,e=map(int,file.readline().split())

  for _ in range(e):
    vertex1,vertex2,cost=map(int,file.readline().split())
    heapq.heappush(edges,(cost,vertex1,vertex2))

MST,result=kruskal(v,edges)
print(result)
