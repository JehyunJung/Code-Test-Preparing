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

gate_num,plane_num=0,0
result=0

with open("input42.txt","r") as file:
  gate_num=int(file.readline())
  plane_num=int(file.readline())
  Gates=[i for i in range(gate_num+1)]
  for _ in range(plane_num):
    parking_gate=int(file.readline())
    if Gates[parking_gate]==0:
      continue
    else:
      union(Gates,parking_gate,parking_gate-1)
      result+=1

print(result)

