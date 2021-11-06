def rotation(dir,rot_info):
  new_dir=0
  if rot_info =='D':
    new_dir=(dir+1)%4
  if rot_info=='L':
    new_dir=(dir-1)%4
  return new_dir

n,k,l=0,0,0
graph=[]
turns=[]
with open("input11.txt","r") as file:
  n=int(file.readline())
  k=int(file.readline())
  graph=[[0] * (n+1) for _ in range(n+1)]
  for _ in range(k):
    row,col=map(int,file.readline().split())
    graph[row][col]=2
  l=int(file.readline())
  for _ in range(l):
    sec,dir=file.readline().split()
    turns.append((int(sec),dir))
  
graph[1][1]=1

result=0
dy=[0,1,0,-1]
dx=[1,0,-1,0]
x=1
y=1
dir=0
snakes=[(1,1)]
index=0

while True:
  print("result",result)
  for i in range(n):
    print(graph[i])
  print()  

  new_y=y+dy[dir]
  new_x=x+dx[dir]
  
  result+=1
  if new_y <1 or new_x <1 or new_y >n or new_x >n:
    break

  if graph[new_y][new_x] ==1:
    break

  if graph[new_y][new_x] ==0:  
    tail_y,tail_x=snakes.pop(0)
    graph[tail_y][tail_x]=0

  graph[new_y][new_x]=1
  snakes.append((new_y,new_x))
    
  if index<l and result==turns[index][0]:
    print("rotate")
    dir=rotation(dir,turns[index][1])
    index+=1
  
  y=new_y
  x=new_x

print(result)