def find_parent(parent,x):
  if parent[x] != x:
    return find_parent(parent,parent[x])
  return x

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


if __name__ == "__main__":
  v,e=0,0
  parent=[]
  with open("data.txt","r") as file:
    v,e=map(int,file.readline().split())
    parent=[0] * (v+1)

    for i in range(1,v+1):
      parent[i]=i
  
    for _ in range(e):
      v1,v2=map(int,file.readline().split())
      union_parent(parent,v1,v2)

  for i in range(e):
    find_parent_compressed(parent,i)

  print(parent)
