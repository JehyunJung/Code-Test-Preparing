from collections import deque

def bfs(idx,start_x,start_y):
  global visited,dy,dx,components
  
      

def solution():
  visited=[[False] * n for _ in range(n)]
  dy=[-1,0,1,0]
  dx=[0,1,0,-1]
  components=[]
  idx=0
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        visited[i][j]=True
        
        if graph[i][j]=='0':
          continue
        else:
          components.append(1)
          queue=deque()
          queue.append((i,j))
          while queue:
            
            y,x=queue.popleft()
            for dir in range(4):
              next_y,next_x=y+dy[dir],x+dx[dir]
              if next_y <0 or next_y >=n or next_x <0 or next_x >= n:
                continue
              if visited[next_y][next_x]:
                continue
          
              if graph[next_y][next_x] == '1':
                visited[next_y][next_x]=True
                components[idx]+=1
                queue.append((next_y,next_x))
          idx+=1
  print(components)
  components=[component for component in components if component >1]      
  components.sort()
  print(len(components))
  for component in components:
    print(component)
if __name__ =="__main__":
  n=0
  graph=[]
  with open("input2667.txt","r") as file:
    n=int(file.readline())
    for _ in range(n):
      graph.append(list(map(str,file.readline().strip())))

  solution()