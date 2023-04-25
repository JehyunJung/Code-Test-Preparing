import sys
from collections import deque
def find_path(row,col,path):
    global visited,pipeline_count
    if col == (n_cols-1):
        pipeline_count+=1
        return True
        
    for dir in range(3):
        next_row=row + dy[dir]
        next_col=col + dx[dir]

        #격자를 벗어나는 경우
        if next_row < 0 or next_row >=n_rows or next_col < 0 or next_col >=n_cols:
            continue
        
        #벽인 경우
        if board[next_row][next_col]== "x":
            continue
            
        #이미 파이프 라인이 설치되어 있는 경우
        if visited[next_row][next_col]:
            continue
        visited[next_row][next_col]=True
        if find_path(next_row,next_col,path+[(next_row,next_col)]):
            return True
    return False

def solution():
    for start_row in range(n_rows):
        find_path(start_row,0,[(start_row,0)])
    
    print(pipeline_count)
if __name__ == "__main__":
    sys.stdin=open("input3109.txt","r")

    n_rows,n_cols=map(int,input().split())
    board=[list(input()) for _ in range(n_rows)]
    visited=[[False] * n_cols for _ in range(n_rows)]
    dy=[-1,0,1]
    dx=[1,1,1]
    pipeline_count=0
    solution()