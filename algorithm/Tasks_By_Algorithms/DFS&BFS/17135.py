from collections import deque
from itertools import combinations
from copy import deepcopy
from os import kill
def bfs(graph,start_col):
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    queue=deque([(N-1,start_col,1)])
    visited=[[False]*M for _ in range(N)]
    enemies=[]
    while queue:
        row,col,count=queue.popleft()
        if count > D:
            continue
        if visited[row][col]:
            continue

        visited[row][col]=True

        if graph[row][col]==1:
            enemies.append((count,row,col))
        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            if next_row < 0 or next_row>=N or next_col < 0 or next_col>=M:
                continue
            
            queue.append((next_row,next_col,count+1))
    
    enemies.sort(key=lambda x: (x[0],x[2]))
    return enemies

def check_if_all_enemy_died(graph):
    for row in graph:
        for data in row:
            if data !=0:
                return False
    return True

def move_all_enemies_down(graph,i):
    for row in range(N-2,i-1,-1):
        for col in range(M):
            graph[row+1][col]=graph[row][col]
    
    #첫행은 사라지게 된다.
    for col_index in range(M):
        graph[i][col_index]=0

def print_board(graph):
    for row in graph:
        print(row)
    print()

def solution():
    max_enemy=0
    for combination in combinations(range(M),3):
        temp_board=deepcopy(board)
        enemy=0
        print(combination)
        for i in range(N):
            #모든 적을 다 죽인 경우
            if check_if_all_enemy_died(temp_board):
                break

            killed_enemies=[]
            for col in combination:
                
                enemies=bfs(temp_board,col)
                if len(enemies) > 0:
                    killed_enemies.append((enemies[0][1],enemies[0][2]))

            #죽일 수 있는 적에 대해서 죽인다.
            for row,col in killed_enemies:
                temp_board[row][col]=0
                
            #중복해서 죽이는 경우가 존재하기 때문에
            enemy+=len(set(killed_enemies))
            #죽이는 행위를 진행한 이후에는 모든 적을 한칸 씩아래로 옮긴다.
            move_all_enemies_down(temp_board,i)

        max_enemy=max(max_enemy,enemy)
        
        
    return max_enemy

if __name__ == "__main__":
    N,M,D=0,0,0
    board=[]

    with open("input17135.txt","r") as file:
        N,M,D=map(int,file.readline().split())

        board=[list(map(int,file.readline().split())) for _ in range(N)]
    
    print(solution())