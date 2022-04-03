from collections import deque

def bfs(sharks):
    global answer
    dy=[-1,-1,-1,0,1,1,1,0]
    dx=[-1,0,1,1,1,0,-1,-1]
    queue=deque(sharks)
  
    while queue:
        current_row,current_col=queue.popleft()

        for dir in range(8):
            new_row,new_col=current_row+dy[dir],current_col+dx[dir]

            if new_row < 0 or new_row >=row or new_col < 0 or new_col >=col:
                continue

            if graph[new_row][new_col] !=0:
                continue
              
            graph[new_row][new_col]=graph[current_row][current_col]+1
          
            answer=max(answer,graph[new_row][new_col])-1
            queue.append((new_row,new_col))


if __name__ == "__main__":
  row,col=0,0
  graph=[]
  sharks=[]
  answer=0
  with open("input17086.txt","r") as file:
    row,col=map(int,file.readline().split())

    for i in range(row):
      graph.append(list(map(int,file.readline().split())))
      for j in range(col):
        if graph[i][j]==1:
          sharks.append((i,j))
    
    bfs(sharks)
    print(answer)
 
        
      
