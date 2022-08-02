from math import inf
from collections import deque
import os
def move(n,board,pos,state):
    results=[]
    
    #parallel movement
    head=pos[0]
    tail=pos[1]
    movement=[(0,1),(1,0),(0,-1),(-1,0)]
    for dir in range(4):
        new_head=(head[0]+movement[dir][0],head[1]+movement[dir][1])
        new_tail=(tail[0]+movement[dir][0],tail[1]+movement[dir][1])
        
        if new_head[0]<=0 or new_head[0]>n or new_head[1]<=0 or new_head[1]>n or new_tail[0]<=0 or new_tail[0]>n or new_tail[1]<=0 or new_tail[1]>n:
            continue
        if board[new_head[0]-1][new_head[1]-1]==1 or board[new_tail[0]-1][new_tail[1]-1]==1:
            continue
        
        results.append(([new_head,new_tail],state))
        
    #state,axis,direction
    dy=[[[1,-1],[-1,1]],[[0,0],[0,0]]]
    dx=[[[0,0],[0,0]],[[-1,1],[1,-1]]]
    for axis in range(2):
        for direction in range(2):
            #회전한 이후의 좌표
            row,col=pos[axis]
            new_row=row+dy[state][axis][direction]
            new_col=col+dx[state][axis][direction]
            new_pos=(new_row,new_col)
            
            #회전 반경에 있는 좌표
            non_axis_row,non_axis_col=pos[1-axis]
            temp_row=non_axis_row+dy[state][axis][direction]
            temp_col=non_axis_col+dx[state][axis][direction]
            temp_pos=(temp_row,temp_col)
            
            #회전 이후의 좌표가 맵을 넘어서는 경우
            if new_row <=0 or new_row > n or new_col <=0 or new_col>n:
                continue
            if temp_row <=0 or temp_row > n or temp_col <=0 or temp_col>n:
                continue
                
            #회전 반경에 벽이 있는 경우
            if board[new_row-1][new_col-1]==1:
                continue
            if board[temp_row-1][temp_col-1]==1:
                continue
            
            results.append(([pos[axis],new_pos],1-state))
    return results
        
    
def solution(board):
    answer = 0
    n=len(board)
    
    queue=deque([([(1,1),(1,2)],0,0)])
    visited=[[(1,1),(1,2)]]
    
    while True:
        current_position,state,count=queue.popleft()
        if (n,n) in current_position:
            answer=count
            break
        
        candidate_movements=move(n,board,current_position,state)
        for candidate_position,state in candidate_movements:
            if candidate_position in visited:
                continue
            queue.append((candidate_position,state,count+1))
            visited.append(candidate_position)
    
    return answer

if __name__ == "__main__":
    board=[]
    with open("E:\\Codes\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\inputp60063.txt","r") as file:
        n=int(file.readline())
        board=[list(map(int,file.readline().split())) for _ in range(n)]
    print(solution(board))
