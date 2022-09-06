from copy import deepcopy

def rotation(dir):
    if dir == 0:
        dir=8
    return dir-1

def decrease_smell(smell_graph):
    for row in range(4):
        for col in range(4):
            if smell_graph[row][col] ==0:
                continue
            smell_graph[row][col]-=1

def fish_move(graph,smell_graph):
    temp_graph=[[[] for _ in range(4)] for _ in range(4)]

    for row in range(4):
        for col in range(4):
            if len(graph[row][col])==0:
                continue

            for fish_dir in graph[row][col]:
                #처음 회전 방지
                target_row,target_col=row,col
                fish_dir+=1
                for _ in range(8):
                    fish_dir=rotation(fish_dir)

                    next_row=row+fish_dy[fish_dir]
                    next_col=col+fish_dx[fish_dir]

                    #격자 외부
                    if next_row < 0 or next_row>=4 or next_col < 0 or next_col >=4:
                        continue
                    #냄새가 있는 칸
                    if smell_graph[next_row][next_col] != 0:
                        continue
                    #상어가 있는 칸
                    if next_row == shark_row and next_col == shark_col:
                        continue
                    target_row,target_col=next_row,next_col
                    break
                temp_graph[target_row][target_col].append(fish_dir)
    
    return temp_graph

def shark_eat(graph,smell_graph):
    global shark_row,shark_col,candidates
    candidates=[]
    
    def dfs(cnt,moves,count,graph,row,col):
        global candidates
        if cnt==3:
            candidates.append((count,moves))
            return

        for i in range(4):
            next_row=row+dy[i]
            next_col=col+dx[i]
            if next_row < 0 or next_row>=4 or next_col < 0 or next_col >=4:
                continue

            temp_graph=deepcopy(graph)
            temp_graph[next_row][next_col]=[]
            dfs(cnt+1,moves+str(i),count+len(graph[next_row][next_col]),temp_graph,next_row,next_col)
    
    dfs(0,"",0,graph,shark_row,shark_col)

    #물고기가 많은 순서대로, 이동이 사전순으로 정렬
    candidates.sort(key=lambda x:(-x[0],x[1]))
    count,moves=candidates[0]

    #상어가 이동한 경로에 있는 물고기는 모두 죽게 된다.
    for move in moves:
        dir=int(move)
        shark_row+=dy[dir]
        shark_col+=dx[dir]

        if len(graph[shark_row][shark_col]) !=0:
            graph[shark_row][shark_col]=[]
            #물고기가 죽은 칸에서는 냄새가 생긴다.
            smell_graph[shark_row][shark_col]=3

def extract_fishses(graph):
    fishes=[]
    for row in range(4):
        for col in range(4):
            if len(graph[row][col]) ==0:
                continue
            for fish_dir in graph[row][col]:
                fishes.append((row,col,fish_dir))
    return fishes        

def solution(fishes):
    graph=[[[] for _ in range(4)] for _ in range(4)]
    smell_graph=[[0]*4 for _ in range(4)]

    #처음으로 물고기를 생성한다.
    for row,col,dir in fishes:
        graph[row][col].append((dir))


    for _ in range(S):
        #복제할 물고기 목록을 뽑아낸다.
        fishes=extract_fishses(graph)
        #물고기의 이동
        graph=fish_move(graph,smell_graph)

        #상어의 먹이활동 + 냄새
        shark_eat(graph,smell_graph)

        #냄새 1씩 감소
        decrease_smell(smell_graph)
        
        #물고기 복제
        for row,col,dir in fishes:
            graph[row][col].append((dir))

    count=0
    for row in range(4):
        for col in range(4):

            if len(graph[row][col]) ==0:
                continue

            #냄새
            count+=len(graph[row][col])

    return count   

if __name__ == "__main__":
    M,S=0,0
    fishes=[]
    shark_row,shark_col=0,0

    fish_dy=[0,-1,-1,-1,0,1,1,1]
    fish_dx=[-1,-1,0,1,1,1,0,-1]
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    candidates=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input23290.txt","r") as file:
        M,S=map(int,file.readline().split())
        for _ in range(M):
            row,col,dir=map(int,file.readline().split())
            fishes.append((row-1,col-1,dir-1))
        
        shark_row,shark_col=map(int,file.readline().split())
        shark_row-=1
        shark_col-=1

    print(solution(fishes))