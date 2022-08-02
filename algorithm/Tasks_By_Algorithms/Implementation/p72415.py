from math import inf
from collections import deque,defaultdict
from itertools import permutations
from copy import deepcopy

def bfs(board,row,col,target_row,target_col):
    visited=[[False] *4  for _ in range(4)]   
    queue=deque([(row,col,0)])
    movements=[(-1,0),(0,1),(1,0),(0,-1)]
    
    while queue:
        row,col,count=queue.popleft()       
        if row==target_row and col==target_col:
            return count + 1
        
        if visited[row][col]:
            continue
            
        visited[row][col]=True

        #칸 이동
        for direction in range(4):
            #한 칸 이동
            target_movement=movements[direction]   
            new_row=row+target_movement[0]
            new_col=col+target_movement[1]
            
            if new_row < 0 or new_row >=4 or new_col < 0 or new_col>=4:
                continue
            queue.append((new_row,new_col,count+1))
            
            #여러칸 이동
            for times in range(1,5):
                new_row=row+target_movement[0]*times
                new_col=col+target_movement[1]*times
            
                if new_row < 0 or new_row >=4 or new_col < 0 or new_col>=4:
                    new_row=row+target_movement[0]*(times-1)
                    new_col=col+target_movement[1]*(times-1)
                    queue.append((new_row,new_col,count+1))
                    break
            
                if board[new_row][new_col] != 0:
                    queue.append((new_row,new_col,count+1))
                    break
                
def solution(board, r, c):    
    answer = 0
    card_positions=defaultdict(list)
    
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0:
                card_positions[board[i][j]].append((i,j))
    
    card_types=list(card_positions.keys())
    
    min_count=inf
    for card_permutation in permutations(card_types):
        count=0
        row,col=r,c
        temp_board=deepcopy(board)
        for card_type in card_permutation:    
            prev_card=card_positions[card_type][0]
            post_card=card_positions[card_type][1]
            
            #앞 카드 먼저
            prev_count=bfs(temp_board,row,col,prev_card[0],prev_card[1])+bfs(temp_board,prev_card[0],prev_card[1],post_card[0],post_card[1])
            #뒷 카드 먼저
            post_count=bfs(temp_board,row,col,post_card[0],post_card[1])+bfs(temp_board,post_card[0],post_card[1],prev_card[0],prev_card[1])

            if prev_count < post_count:
                row,col=post_card
                count+=prev_count
            else:
                row,col=prev_card
                count+=post_count
                
            temp_board[prev_card[0]][prev_card[1]]=0
            temp_board[post_card[0]][post_card[1]]=0

        min_count=min(min_count,count)
        answer=min_count
            
    return answer
if __name__ == "__main__" :
    board=[]
    r,c=0,0

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\inputp72415.txt") as file:
        board=[list(map(int,file.readline().split())) for _ in range(4)]
        r,c=map(int,file.readline().split())
    
    print(solution(board,r,c))