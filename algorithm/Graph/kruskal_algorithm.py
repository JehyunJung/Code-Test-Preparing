import heapq
from disjoin_sets import find_parent_compressed, union_parent

def kruskal(v,edges):
  MST=[[] for _ in range(v+1)]
  parents=[0] * (v+1)
  for i in range(1,v+1):
    parents[i]=i
  result=0
  edge_count=0
  while edge_count<v-1:
    cost,v1,v2=heapq.heappop(edges)

    if find_parent_compressed(parents,v1) != find_parent_compressed(parents,v2):
      union_parent(parents,v1,v2)
      result+=cost
      MST[v1].append(v2)
      MST[v2].append(v1)
      edge_count+=1
    else:
      continue
  return MST,result
    

if __name__ == "__main__":
  v,e=0,0
  edges=[]

  with open("data1.txt","r") as file:
    v,e=map(int,file.readline().split())

    for _ in range(e):
      v1,v2,cost=map(int,file.readline().split())
      heapq.heappush(edges,(cost,v1,v2))
  
  MST,result=kruskal(v,edges)
  print(MST,result)
  