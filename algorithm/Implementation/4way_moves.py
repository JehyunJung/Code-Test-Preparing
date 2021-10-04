n=0
moves=[]
with open("input.txt","r") as file:
  n=int(file.readline())
  moves=list(file.readline().split())

dy=[0, 0, -1, 1]
dx=[-1, 1, 0, 0]
move_types=['L','R','U','D']
x,y=1,1

for move in moves:
  for i in range(4):
    if move==move_types[i]:
      ny=y+dy[i]
      nx=x+dx[i]

      if ny == 0 or ny == n+1 or nx == 0 or nx == n+1:
        break
      y=ny
      x=nx
      
print(y,x)

