from collections import deque
from math import inf
def solution():
    time_map=[[inf] * n_cols for _ in range(n_rows)]
    end_row,end_col=0,0
    water_queue,animal_queue=deque(),deque()
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    
    for row in range(n_rows):
        for col in range(n_cols):
            #출발점
            if board[row][col]=="S":
                animal_queue.append((row,col,0))
            #도착점
            if board[row][col]=="D":
                end_row,end_col=row,col
            #물이 있는 자리의 좌표
            if board[row][col]=="*":
                water_queue.append((row,col,0))
    
    #물의 이동 수행
    visited=[[False] * n_cols for _ in range(n_rows)]
    while water_queue:
        row,col,time=water_queue.popleft()
        
        #이전에 방문한 경우
        if visited[row][col]:
            continue
        visited[row][col]=True
        #물이 해당 좌표에 도달하는 시간
        time_map[row][col]=time
        

        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]
            #범위를 넘어서는 경우
            if next_row < 0 or next_row>=n_rows or next_col<0 or next_col>=n_cols:
                continue
            #다음 좌표가 돌인 경우
            if board[next_row][next_col]=="X":
                continue
            #물은 목적지 좌표에 도달할 수 없다.
            if board[next_row][next_col]=="D":
                continue

            water_queue.append((next_row,next_col,time+1))
    
    #고슴도치의 이동 수행
    visited=[[False] * n_cols for _ in range(n_rows)]
    while animal_queue:
        row,col,time=animal_queue.popleft()
        #목적지에 도달한 경우
        if (row,col)==(end_row,end_col):
            print(time)
            return
        #이전에 방문한 경우
        if visited[row][col]:
            continue
        visited[row][col]=True

        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]
            #범위를 벗어나는 경우
            if next_row < 0 or next_row>=n_rows or next_col<0 or next_col>=n_cols:
                continue
            #다음 좌표가 돌인 경우
            if board[next_row][next_col]=="X":
                continue
            
            #해당 자리에 물이 먼저 도착하는 경우에는 다음 좌표로 이동 불가능
            if time_map[next_row][next_col] <= time+1:
                continue
            animal_queue.append((next_row,next_col,time+1))

    print("KAKTUS")


if __name__ == "__main__":
    with open("input3055.txt","r") as file:
        n_rows,n_cols=map(int,file.readline().split())
        board=[list(file.readline().strip()) for _ in range(n_rows)]
                
    solution()