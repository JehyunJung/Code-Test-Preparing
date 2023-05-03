import sys
from collections import deque

#외부와 연결되어 있는 공기 좌표 구하기
def check_outer_air(boundaries):
    visited=[[False] * n_cols for _ in range(n_rows)]
    cheese_map=[[0] * n_cols for _ in range(n_cols)]
    
    queue=deque()
    
    #모서리에 대해서, 치즈가 없는 좌표들을 찾는다.
    for row,col in boundaries:
        if board[row][col] == 0:
            queue.append((row,col))

    #모서리와 연결되어 있는 좌표를 구하기 위한 bfs
    while queue:
        row,col = queue.popleft()
        #이미 방문한 경우
        if visited[row][col]:
            continue

        visited[row][col]=True

        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]
            #격자 범위를 벗어나는 경우
            if next_row < 0 or next_row >=n_rows or next_col < 0 or next_col >=n_cols:
                continue

            #이미 방문한 경우
            if visited[next_row][next_col]:
                continue
            
            #치즈가 있는 경우
            if board[next_row][next_col] == 1:
                cheese_map[next_row][next_col]+=1
                continue

            queue.append((next_row,next_col))
    
    return cheese_map

#치즈를 제거하기 위한 함수
def delete_cheese(cheese_map):
    global board,cheese_count

    for row in range(n_rows):
        for col in range(n_cols):
            #치즈가 있는 공간
            if cheese_map[row][col]>=2:
                board[row][col]=0
                cheese_count-=1

def solution():
    global cheese_count
    #외부 격자 좌표
    boundaries=[]

    for col in range(1,n_cols):
        boundaries.append((0,col))
    
    for row in range(1,n_rows):
        boundaries.append((row,n_cols-1))

    for col in range(1,n_cols):
        boundaries.append((n_rows-1,col))
    
    for row in range(1,n_rows):
        boundaries.append((row,0))

    #초기 치즈 갯수 구하기
    for row in range(n_rows):
        for col in range(n_cols):
            if board[row][col]==1:
                cheese_count+=1

    time=0
    while cheese_count!=0:
        cheese_map=check_outer_air(boundaries)
        delete_cheese(cheese_map)
        time+=1
    
    print(time)

    

if __name__ == "__main__":
    sys.stdin=open("input2638.txt","r")
    n_rows,n_cols=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(n_rows)]

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    cheese_count=0
    
    solution()