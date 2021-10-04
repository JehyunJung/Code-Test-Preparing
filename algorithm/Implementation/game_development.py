maze = []
x,y,direction=0,0,0

with open("input.txt","r") as file:
  n, m = map(int, file.readline().split())
  x, y, direction = map(int, file.readline().split())
  for i in range(n):
    maze.append(list(map(int, file.readline().split())))

d = [[0] * m for _ in range(n)]

d[y][x]=1
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def turn():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_time = 0
while True:
  turn()
  ny = y + dy[direction]
  nx = x + dx[direction]    

  if d[ny][nx] == 0 and maze[ny][nx] == 0:
    d[ny][nx] = 1
    y = ny
    x = nx
    count += 1
    turn_time = 0
    continue

  else:
    turn_time += 1

  if turn_time == 4:
    ny = y - dy[direction]
    nx = x - dx[direction]
      
    if maze[ny][nx] == 0:
      y = ny
      x = nx

    else:
        break
    turn_time = 0

print(count)