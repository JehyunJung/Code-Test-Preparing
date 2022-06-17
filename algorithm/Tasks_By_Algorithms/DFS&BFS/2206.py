from math import inf
from collections import deque

def solution():
    visited=[[[0]*2 for _ in range(m)] for _ in range(n)]
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    queue=deque([(0,0,0)]);
    visited[0][0][0]=1
    
    while queue:
        row,col,crushed=queue.popleft()

        if row==n-1 and col == m-1:
            return visited[row][col][crushed]

        for dir in range(4):
            new_row=row+dy[dir]
            new_col=col+dx[dir]

            if new_row < 0 or new_row >=n or new_col < 0 or new_col >=m:
                continue

            if graph[new_row][new_col] ==0 and visited[new_row][new_col][crushed] == 0:
                queue.append((new_row,new_col,crushed))
                visited[new_row][new_col][crushed]=visited[row][col][crushed]+1
            
            if graph[new_row][new_col] ==1 and crushed ==0:
                queue.append((new_row,new_col,crushed+1))
                visited[new_row][new_col][crushed+1]=visited[row][col][crushed]+1
                

    return -1

if __name__ == "__main__":
    n,m=0,0
    graph=[]

    with open("input2206.txt","r") as file:
        n,m=map(int,file.readline().split())
        graph=[list(map(int,file.readline().strip())) for _ in range(n)]
    print(solution())