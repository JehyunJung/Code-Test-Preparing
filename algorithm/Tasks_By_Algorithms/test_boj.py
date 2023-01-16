from os.path import dirname,join

#물고기의 이동
def fish_move(board,smell_graph):
    temp_board=[[[] for _ in range(4)] for _ in range(4)]

    for row in range(4):
        for col in range(4):
            if len(board[row][col])==0:
                continue
            for dir in board[row][col]:
                #이동할 수 없는 경우, 이동할 수 있는 칸을 찾을 때까지 방향이동을 수행한다.
                for i in range(9):
                    next_dir=(dir-i)%8
                    next_row=row+dy[next_dir]
                    next_col=col+dx[next_dir]

                    if next_row<0 or next_row >=4 or next_col < 0 or next_col>=4:
                        continue

                    if next_row==shark_row and next_col==shark_col:
                        continue

                    if smell_graph[next_row][next_col]!=0:
                        continue
                    temp_board[next_row][next_col].append(next_dir)
                    break
                else:
                    temp_board[row][col].append(dir)
    
    return temp_board

#상어의 이동 가능한 부분 체크
def shark_candidates(cnt,board,path,visited,fish_kills,row,col):
    global possible_shark_locations
    if cnt==3:
        possible_shark_locations.append((fish_kills,path))
        return
    
    for dir in range(4):
        next_row=row+shark_dy[dir]
        next_col=col+shark_dx[dir]

        if next_row < 0 or next_row>=4 or next_col< 0 or next_col>=4:
            continue
        #이미 방문한 칸이라면 물고리를 또다시 잡아먹을 수는 없다.
        if (next_row,next_col) in visited:
            shark_candidates(cnt+1,board,path+str(dir),visited,fish_kills,next_row,next_col)
        else:
            shark_candidates(cnt+1,board,path+str(dir),visited+[(next_row,next_col)],fish_kills+len(board[next_row][next_col]),next_row,next_col)
    
def shark_move(path,board,smell_graph,row,col):
    shark_row,shark_col=row,col
    for dir in path:
        dir=int(dir)
        shark_row+=shark_dy[dir]
        shark_col+=shark_dx[dir]

        length=len(board[shark_row][shark_col])
        
        #해당 칸에 물고기가 있으면 잡아 먹고 냄새를 생성한다.
        if length >0:
            smell_graph[shark_row][shark_col]=3
            board[shark_row][shark_col]=[]

    return shark_row,shark_col

def decrease_smell(smell_graph):
    for row in range(4):
        for col in range(4):
            if smell_graph[row][col] >0:
                smell_graph[row][col]-=1
    
def copy_fish(temp_board,board):
    for row in range(4):
        for col in range(4):
            temp_board[row][col].extend(board[row][col])
    
    return temp_board


def solution():
    global possible_shark_locations,shark_row,shark_col
    board=[[[] for _ in range(4)] for _ in range(4)]
    
    #냄새 정보
    smell_graph=[[0] * 4 for _ in range(4)]
    #초기 물고기 배치
    for row,col,dir in fishes:
        board[row][col].append(dir)
    
    for _ in range(s):
        temp_board=fish_move(board,smell_graph)
        possible_shark_locations=[]
        shark_candidates(0,temp_board,"",[],0,shark_row,shark_col)

        possible_shark_locations.sort(key=lambda x: (-x[0],x[1]))
        shark_row,shark_col=shark_move(possible_shark_locations[0][1],temp_board,smell_graph,shark_row,shark_col)
    
        decrease_smell(smell_graph)

        board=copy_fish(temp_board,board)

    count=0
    for row in range(4):
        for col in range(4):
            count+=len(board[row][col])
    
    return count

if __name__ == "__main__":
    scriptpath = dirname(__file__)
    filename = join(scriptpath, 'input.txt')

    #predefined globals
    
    shark_dy=[-1,0,1,0]
    shark_dx=[0,-1,0,1]
 
    m,s=map(int,input().split())
    fishes=[list(map(lambda x: int(x)-1,input().split())) for _ in range(m)]

    shark_row,shark_col=map(lambda x: int(x)-1,input().split())
    
    possible_shark_locations=[]
    print(solution())
