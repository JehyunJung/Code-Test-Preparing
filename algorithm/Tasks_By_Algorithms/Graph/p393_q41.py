def find_parent(parent,x):
  if parent[x] != x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union(parent,x,y):
  pre_x=find_parent(parent,x)
  pre_y=find_parent(parent,y)

  if pre_x < pre_y:
    parent[pre_y]=pre_x
  else:
    parent[pre_x]=pre_y

  
n,travel_cities=0,0
graph=[]
travel_route=[]

with open("input41.txt","r") as file:
  n,travel_cities=map(int,file.readline().split())
  for _ in range(n):
    graph.append(list(map(int,file.readline().split())))
  travel_route=list(map(int,file.readline().split()))

parent=[i for i in range(n+1)]

for i in range(n):
  for j in range(n):
    if i<j and graph[i][j]==1:
      union(parent,i+1,j+1)


result=True
main_city=find_parent(parent,travel_route[0])

for city in travel_route[1:]:
  if find_parent(parent,city) != main_city:
    result=False
    break

if result:
  print("YES")
else:
  print("NO")




