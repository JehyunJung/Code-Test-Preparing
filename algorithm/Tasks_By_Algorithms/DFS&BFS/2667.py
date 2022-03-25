from collections import deque

def bfs(graph,start_x,start_y):
  dy=[-1,0,1,0]
  dx=[0,1,0,-1]
  count=1
  queue=deque()
  graph[start_x][start_y]=0
  queue.append((start_x,start_y))
  while queue:
    x,y=queue.popleft()
    
    for dir in range(4):
      next_x,next_y=x+dx[dir],y+dy[dir]
      
      if next_y <0 or next_y >=n or next_x <0 or next_x >= n:
        continue
      
      if graph[next_x][next_y] == 1:
        graph[next_x][next_y]=0
        count+=1
        queue.append((next_x,next_y))
  
  return count   

def solution():
  components=[]
  for i in range(n):
    for j in range(n):
      if graph[i][j]==1:
        components.append(bfs(graph,i,j))
  
  components.sort()
  print(len(components))
  for component in components:
    print(component)
    
if __name__ =="__main__":
  n=0
  graph=[]
  with open("input2667.txt","r") as file:
    n=int(file.readline())
    for i in range(n):
      graph.append(list(map(int,file.readline().strip())))
      print(graph[i])                   

  solution()