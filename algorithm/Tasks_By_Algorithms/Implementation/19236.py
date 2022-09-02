from copy import deepcopy

def find_move_spots(graph,shark_info):
    shark_row,shark_col,shark_dir=shark_info
    candidates=[]
    for i in range(1,4):
        next_row=shark_row+ dy[shark_dir] * i
        next_col=shark_col+ dx[shark_dir] * i
        
        #범위를 벗어나는 경우
        if next_row < 0 or next_row >=4 or next_col < 0 or next_col>=4:
            break

        #물고기가 없는 칸
        if graph[next_row][next_col] ==0:
            continue
        
        candidates.append((next_row,next_col))
    
    return candidates


def fish_moves(board,fishes,dead,shark_info):
    shark_row,shark_col,shark_dir=shark_info

    for i in range(1,17):
        #죽은 물고기는 생략
        if i in dead:
            continue

        fish_row,fish_col,fish_dir=fishes[i]
        #최대 8번의 회전 수행 가능
        for iter in range(9):
            next_fish_dir=(fish_dir+iter)%8

            next_fish_row=fish_row + dy[next_fish_dir]
            next_fish_col=fish_col + dx[next_fish_dir]

            if next_fish_row < 0 or next_fish_row>=4 or next_fish_col<0 or next_fish_col>=4:
                continue
            #상어가 있는 칸에는 이동 하지 않는다.
            if next_fish_row == shark_row and next_fish_col == shark_col:
                continue

            target_fish_index=board[next_fish_row][next_fish_col]
            board[next_fish_row][next_fish_col],board[fish_row][fish_col]=board[fish_row][fish_col],board[next_fish_row][next_fish_col]
            fishes[i]=[next_fish_row,next_fish_col,next_fish_dir]  

            #물고기가 있는 칸으로 이동시
            if target_fish_index!=0:
                fishes[target_fish_index]=[fish_row,fish_col,fishes[target_fish_index][2]]   
            break


def dfs(board,fishes,shark_info,dead,result):
    global max_result
    
    #이동을 진행하고
    fish_moves(board,fishes,dead,shark_info)

    candidates=find_move_spots(board,shark_info)

    if len(candidates) ==0:
        max_result=max(max_result,result)
        return
    
    #먹이를 찾아서 이동한다.
    for row,col in candidates:
        temp_board=deepcopy(board)
        temp_fishes=deepcopy(fishes)
        target_index=temp_board[row][col]
        temp_board[row][col]=0
        dfs(temp_board,temp_fishes,[row,col,fishes[target_index][2]],dead+[target_index],result+target_index)      
    

def solution(board,fishes):
    first_index=board[0][0]
    shark_info=[0,0,fishes[first_index][2]]
    #첫 번째는 먹이는 잡아 먹히게 된다.
    board[0][0]=0
    dfs(board,fishes,shark_info,[first_index],first_index)


if __name__== "__main__":
    board=[[0]*4 for _ in range(4)]
    fishes=dict()

    dy=[-1,-1,0,1,1,1,0,-1]
    dx=[0,-1,-1,-1,0,1,1,1]
    max_result=0
    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input19236.txt","r") as file:
        
        for row in range(4):
            temp=list(map(int,file.readline().split()))

            for col in range(4):
                index,dir=temp[col*2],temp[col*2+1]-1
                fishes[index]=[row,col,dir]
                board[row][col]=index
    solution(board,fishes)
    print(max_result)    