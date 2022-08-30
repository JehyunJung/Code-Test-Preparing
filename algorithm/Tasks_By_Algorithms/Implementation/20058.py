from collections import deque

def rotation(L):
    global graph
    length=2**L
    iteration=2**(N-L)

    for row_index in range(iteration):
        for col_index in range(iteration):
            start_row=row_index*length
            start_col=col_index*length
            
            #회전을 진행한 이후의 부분 배열
            sub_graph=[[0] * length for _ in range(length)]
            for dy in range(length):
                for dx in range(length):
                    sub_graph[dx][length-dy-1]=graph[start_row+dy][start_col+dx]
            
            #생성된 부분 배열을 기존 배열에 배치
            for dy in range(length):
                for dx in range(length):
                    graph[start_row+dy][start_col+dx]=sub_graph[dy][dx]

def melt_ices():
    global graph
    decreasing_targets=[]
    for row in range(2**N):
        for col in range(2**N):
            if graph[row][col] ==0:
                continue

            if not check_if_adjacent(row,col):
                decreasing_targets.append((row,col))
    
    for row,col in decreasing_targets:
        graph[row][col]-=1
                    


def check_if_adjacent(row,col):
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    count=0

    for dir in range(4):
        next_row=row+dy[dir]
        next_col=col+dx[dir]

        if next_row < 0 or next_row >= 2**N or next_col < 0 or next_col >= 2**N:
            continue

        if graph[next_row][next_col] ==0:
            continue
        count+=1
    #해당 칸에서 인접하는 칸 중에 얼음이 있는 칸이 3칸 이상인 경우 True 반환
    if count >=3:
        return True
    else:
        return False

def bfs(visited,start_row,start_col):
    queue=deque([(start_row,start_col)])

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    components=[]

    while queue:
        row,col=queue.popleft()

        if visited[row][col]:
            continue
        visited[row][col]=True
        components.append((row,col))
        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]
            #범위를 벗어나는 경우
            if next_row < 0 or next_row >=2**N or next_col < 0 or next_col >= 2**N:
                continue
            #얼음이 없는 경우
            if graph[next_row][next_col] ==0:
                continue

            queue.append((next_row,next_col))

    
    return components

def solution():
    for L in magics:
        if L!=0:
            rotation(L)
        #인접하는 3칸에 대해 얼음이 없는 칸들에 대해서 얼음의 양을 1씩 줄이는 함수
        melt_ices()

    visited=[[False] * (2**N) for _ in range(2**N)]
    max_size=0
    sum_size=0
    for row in range(2**N):
        for col in range(2**N):
            sum_size+=graph[row][col]
            if graph[row][col] ==0 or visited[row][col]:
                continue

            max_size=max(max_size,len(bfs(visited,row,col)))
    
    print(sum_size)
    print(max_size)
if __name__ == "__main__":
    N,Q=0,0
    graph=[]

    magics=[]

    with open("E:\\Codes\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input20058.txt","r") as file:
        N,Q=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(2**N)]
        magics=list(map(int,file.readline().split()))
    
    solution()