from heapq import heappush,heappop

def find_parent_compressed(parent,x):
  if parent[x] != x:
    parent[x]=find_parent_compressed(parent,parent[x])
  return parent[x]

def union_parent(parent,x,y):
  pre_x=find_parent_compressed(parent,x)
  pre_y=find_parent_compressed(parent,y)

  if pre_x < pre_y:
    parent[pre_y]=pre_x
  else:
    parent[pre_x]=pre_y


num=0
x=[]
y=[]
z=[]

with open("input44.txt","r") as file:
  num=int(file.readline())
  for i in range(1,num+1):
    data=list(map(int,file.readline().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))

x.sort()
y.sort()
z.sort()

heap=[]
parents=[i for i in range(num+1)]
result=0
edge_count=0

for i in range(num-1):
  heappush(heap,(x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
  heappush(heap,(y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
  heappush(heap,(z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

while edge_count < num-1:
  cost,vertex1,vertex2=heappop(heap)

  if find_parent_compressed(parents,vertex1) != find_parent_compressed(parents,vertex2):
    union_parent(parents,vertex1,vertex2)
    result+=cost
    edge_count+=1

print(result)

    
    
