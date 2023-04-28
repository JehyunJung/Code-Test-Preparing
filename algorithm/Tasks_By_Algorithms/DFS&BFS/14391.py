import sys
from os.path import dirname,join

def check_visited(row,col,max_dy,max_dx):
    for dy in range(max_dy+1):
        for dx in range(max_dx+1):
            if visited[row+dy][col+dx]:
                return True
    return False

def solution(index,total_point):
    global max_point,visited
    
    #모든 점을 다 탐색한 경우
    if index == (n_rows * n_cols):
        max_point=max(max_point,total_point)
        return
    
    row=index // n_cols
    col=index % n_cols

    #이미 방문한 좌표인 경우
    if visited[row][col]:
        solution(index+1,total_point)

    #가능한 직사각형의 경우를 모두 대입해본다.
    for max_dy,max_dx in rectangle_types:
        next_row=row+max_dy
        next_col=col+max_dx

        #격자 범위를 벗어나는 경우
        if next_row >= n_rows or next_col >= n_cols:
            continue
            
        #이미 처리된 경우
        if check_visited(row,col,max_dy,max_dx):
            continue
        
        rectangle_point=""
        #해당 직사각형을 이루는 점을 모두 방문 처리하고, 직사각형을 이루는 수를 구한다.
        for dy in range(max_dy+1):
            for dx in range(max_dx+1):
                visited[row+dy][col+dx]=True
                rectangle_point+=str(board[row+dy][col+dx])

        rectangle_point=int(rectangle_point)
        
        solution(index+1,total_point+rectangle_point)
        
        #해당 직사각형을 이루는 점을 모두 방문해제 처리한다.
        for dy in range(max_dy+1):
            for dx in range(max_dx+1):
                visited[row+dy][col+dx]=False

                
if __name__ == "__main__":
    scriptpath = dirname(__file__)
    filename = join(scriptpath, 'input14391.txt')

    sys.stdin=open(filename,"r")
    n_rows,n_cols=map(int,input().split())
    board=[list(map(int,list(input()))) for _ in range(n_rows)]
    max_point=0

    rectangle_types=[(0,0)]
   #세로 모양
    for i in range(1,n_rows):
        rectangle_types.append((i,0))
    #가로 모양
    for i in range(1,n_cols):
        rectangle_types.append((0,i)) 
    

    visited=[[False] * n_cols for _ in range(n_rows)]
    solution(0,0)
    print(max_point)
