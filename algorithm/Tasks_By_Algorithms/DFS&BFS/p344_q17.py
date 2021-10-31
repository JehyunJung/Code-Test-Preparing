from collections import deque
def bfs(n,graph,time_passed):
  dy=[-1,0,1,0]
  dx=[0,1,0,-1]
  queue=[]
  for i in range(n):
    for j in range(n):
      if graph[i][j]!=0:
        queue.append((graph[i][j],0,i,j))
  queue.sort()
  queue=deque(queue)

  while queue:
    virus,current_time,y,x=queue.popleft()
    if current_time == time_passed:
      break
    for i in range(4):
      new_y=y+dy[i]
      new_x=x+dx[i]

      if new_y < 0 or new_y >=n or new_x < 0 or new_x >=n:
        continue
      
      if graph[new_y][new_x]==0:
        graph[new_y][new_x]=virus
        queue.append((virus,current_time+1,new_y,new_x))
        

n,k=0,0
graph=[]

time_passed,target_y,target_x=0,0,0

with open("input17.txt","r") as file:
  n,k=map(int,file.readline().split())
  for _ in range(n):
    graph.append(list(map(int,file.readline().split())))
  time_passed,target_y,target_x=map(int,file.readline().split())

bfs(n,graph,time_passed)

print(graph[target_y-1][target_x-1])

  
