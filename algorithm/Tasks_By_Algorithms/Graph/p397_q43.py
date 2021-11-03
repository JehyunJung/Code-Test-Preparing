import heapq

def find_parent(x):
  if x!= parents[x]:
    parents[x]=find_parent(parents[x])
  return parents[x]

def union(x,y):
  pre_x=parents[x]
  pre_y=parents[y]

  if pre_x < pre_y:
    parents[pre_y]=pre_x
  else:
    parents[pre_x]=pre_y

vertex,edge=0,0
parents=[]
edges=[]

sum_cost=0
with open("input43.txt","r") as file:
  vertex,edge=map(int,file.readline().split())
  graph=[[] for _ in range(vertex)]
  
  for _ in range(edge):
    vertex1,vertex2,cost=map(int,file.readline().split())
    heapq.heappush(edges,(cost,vertex1,vertex2))
    sum_cost+=cost

parents=[i for i in range(vertex)]
edge_count=0
result=0

while edge_count != vertex-1:
  cost,vertex1,vertex2=heapq.heappop(edges)

  if find_parent(vertex1) != find_parent(vertex2):
    union(vertex1,vertex2)
    edge_count+=1
    result+=cost

print(sum_cost-result)

