from collections import deque
from math import inf
def solution():
    start_row,start_col=0,0
    distances=[[inf] * n_cols for _ in range(n_rows)]
    walls=[]
    for row in range(n_rows):
        for col in range(n_cols):            
            #시작점
            if graph[row][col]==2:
                start_row,start_col=(row,col)
            
            #벽
            if graph[row][col]==0:
                walls.append((row,col))
    
    queue=deque([(start_row,start_col)])
    distances[start_row][start_col]=0
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    while queue:
        row,col=queue.popleft()
        
        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            if next_row < 0 or next_row >=n_rows or next_col < 0 or next_col>=n_cols:
                continue


            if distances[next_row][next_col]!=inf:
                continue
           
            #벽 회피
            if graph[next_row][next_col]==0:
                distances[next_row][next_col]=0
                continue

            
            #거리 값 갱신
            distances[next_row][next_col] = distances[row][col]+1
            queue.append((next_row,next_col))
        
    
    for row in distances:
        for col in row:
            print(col if col != inf else -1,end=" ")
        print()


if __name__ == "__main__":
    with open("input14940.txt","r") as file:
        n_rows,n_cols=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(n_rows)]
    
    solution()