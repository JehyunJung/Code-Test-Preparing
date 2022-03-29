from collections import deque
def bfs(row,col,visited):
  dy=[-1,0,1,0]
  dx=[0,1,0,-1]
  
  color=graph[row][col]
  count=1
  queue=deque()
  visited[row][col]=True
  queue.append((row,col))
  
  while queue:
    row,col=queue.popleft()
    for dir in range(4):
      new_row,new_col=row+dy[dir],col+dx[dir]
      if new_row < 0 or new_row >=m or new_col < 0 or new_col>=n:
        continue
        
      if visited[new_row][new_col]:
        continue

      if graph[new_row][new_col] != color:
        continue
        
      visited[new_row][new_col]=True
      queue.append((new_row,new_col))
      count+=1 
  return count

def solution(graph):
  blue=[]
  white=[]
  visited=[[False]*n for _ in range(m)]

  for i in range(m):
    for j in range(n):
      if visited[i][j]:
        continue
      if graph[i][j] == 'B':
        blue.append(bfs(i,j,visited))
      else:
        white.append(bfs(i,j,visited))

  white_power=0
  blue_power=0

  for component in white:
    white_power+=component**2
  for component in blue:
    blue_power+=component**2

  print(white_power,blue_power)
if __name__ == "__main__":
  n,m=0,0
  graph=[]
  with open("input1303.txt","r") as file:
    n,m=map(int,file.readline().split())
    for _ in range(m):
      graph.append(list(file.readline().strip()))
  
  solution(graph)
      