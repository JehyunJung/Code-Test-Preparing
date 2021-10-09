from collections import deque
graph=[]
n,m=0,0

"""
with open("input.txt","r") as file:
  n,m=map(int,file.readline().split())

  for row in range(n):
    graph.append(list(map(int,file.readline().split())))
"""

n,m=map(int,input().split())
for row in range(n):
  graph.append(list(map(int,input())))

weight=[[999]*m for _ in range(n)]
dy=[-1,0,1,0]
dx=[0,1,0,-1]

weight[0][0]=1
queue=deque()
queue.append((0,0))

while queue:
  vertex=queue.popleft()
  for i in range(4):
    ny=vertex[0]+dy[i]
    nx=vertex[1]+dx[i]

    if ny<0 or ny >=n or nx < 0 or nx >=m :
      continue

    if graph[ny][nx]==0:
      continue

    if weight[ny][nx] > weight[vertex[0]][vertex[1]] + 1:
      weight[ny][nx] = weight[vertex[0]][vertex[1]] + 1
      queue.append((ny,nx))

print(weight[n-1][m-1])
    
    
