from copy import deepcopy

def decrease_smell():
    global smell_graph
    for row in range(4):
        for col in range(4):
            if smell_graph[row][col] ==0:
                continue
            smell_graph[row][col]-=1

def fish_move():
    global graph
    temp_graph=[[[] for _ in range(4)] for _ in range(4)]

    for row in range(4):
        for col in range(4):
            if len(graph[row][col])==0:
                continue

            for fish_dir in graph[row][col]:
                flag=False
                for i in range(8):
                    next_fish_dir=(fish_dir-i)%8

                    next_row=row+fish_dy[next_fish_dir]
                    next_col=col+fish_dx[next_fish_dir]

                    if 0<=next_row<4 and 0<=next_col<4:
                        if smell_graph[next_row][next_col]==0 and not(next_row == shark_row and next_col == shark_col):    
                            flag=True
                            temp_graph[next_row][next_col].append(next_fish_dir)
                            break
                
                if not flag:
                    temp_graph[row][col].append(fish_dir)
    
    graph=temp_graph

def dfs(cnt,count,row,col,path):
    global max_count,selected_path
    if cnt==3:
        if count > max_count:
            max_count=count
            selected_path=deepcopy(path)
        return

    for i in range(4):
        next_row=row+dy[i]
        next_col=col+dx[i]
        if next_row < 0 or next_row>=4 or next_col < 0 or next_col >=4:
            continue
        #이미 방문한 노드이면 먹이를 먹지 않는다.
        if visited[next_row][next_col]:
            dfs(cnt+1,count,next_row,next_col,path+[i])
        else:
            #방문하는 노드의 경우 해당 자리에 있는 먹이를 먹는다.
            visited[next_row][next_col]=True
            dfs(cnt+1,count+len(graph[next_row][next_col]),next_row,next_col,path+[i])
            visited[next_row][next_col]=False


def shark_eat():
    global max_count,shark_row,shark_col,graph,smell_graph
    max_count=-1

    dfs(0,0,shark_row,shark_col,[])

    #상어는 이동하면서 물고기를 먹고 해당 자리에는 냄새가 들어가게 된다.
    for dir in selected_path:
        shark_row+=dy[dir]
        shark_col+=dx[dir]
        #원래 먹이가 없는 자리였으면 넘어간다.
        if len(graph[shark_row][shark_col])==0:
            continue
        graph[shark_row][shark_col]=[]
        smell_graph[shark_row][shark_col]=3


def solution():

    for _ in range(S):
        #복제할 물고기 목록을 뽑아낸다.
        fishes=deepcopy(graph)
        #물고기의 이동
        fish_move()

        #상어의 먹이활동 + 냄새
        shark_eat()

        #냄새 1씩 감소
        decrease_smell()
        
        #물고기 복제
        for row in range(4):
            for col in range(4):
                graph[row][col].extend(fishes[row][col])


    count=0
    for row in range(4):
        for col in range(4):
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
    dx=[0,-1,0,1]
    max_count=[]
    selected_path=[]
    graph=[[[] for _ in range(4)] for _ in range(4)]
    smell_graph=[[0]*4 for _ in range(4)]
    visited=[[False]*4 for _ in range(4)]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input23290.txt","r") as file:
        M,S=map(int,file.readline().split())
        for _ in range(M):
            row,col,dir=map(int,file.readline().split())
            graph[row-1][col-1].append(dir-1)
        
        shark_row,shark_col=map(int,file.readline().split())
        shark_row-=1
        shark_col-=1

    print(solution())