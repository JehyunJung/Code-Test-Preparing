def check_if_shark_alive():
    for row in range(N):
        for col in range(N):
            if graph[row][col]==0:
                continue

            elif graph[row][col] != 1:
                return True
    return False

def shark_move(smell_graph):
    global graph
    temp_graph=[[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            #빈칸 생략
            if graph[row][col]==0:
                continue
            shark_index=graph[row][col]
            
            #기존 위치에는 냄새를 남긴다.
            smell_graph[row][col]=[shark_index,K]

            checked=False
            
            #빈칸이 있는 지 먼저 확인한다.
            for dir in range(4):
                next_direction=shark_priorities[shark_index-1][current_shark_direction[shark_index-1]-1][dir]
                next_row=row+dy[next_direction-1]
                next_col=col+dx[next_direction-1]     


                if next_row < 0 or next_row >= N or next_col < 0 or next_col >=N:
                    continue

                #냄새가 있는 경우 아직은 넣지 않는다.
                if smell_graph[next_row][next_col] != None:
                    continue
                
                
                #기존의 방향을 변경해줘야한다.
                current_shark_direction[shark_index-1]=next_direction
                #아직 상어가 없는 경우
                if temp_graph[next_row][next_col]==0:
                    temp_graph[next_row][next_col]=shark_index
                #번호가 작은 상어가 우세를 차지한다.
                else:
                    temp_graph[next_row][next_col]=min(temp_graph[next_row][next_col],shark_index)
                
                checked=True
                break

            #빈칸이 없는 경우에는 자기 냄새가 있는 칸으로 간다.
            if not checked:
                for dir in range(4):
                    next_direction=shark_priorities[shark_index-1][current_shark_direction[shark_index-1]-1][dir]
                    next_row=row+dy[next_direction-1]
                    next_col=col+dx[next_direction-1]     

                    if next_row < 0 or next_row >= N or next_col < 0 or next_col >=N:
                        continue

                    #냄새가 없는 경우 
                    if smell_graph[next_row][next_col] == None:
                        continue
                    
                    index,count=smell_graph[next_row][next_col]
                    
                    #자기 냄새가 인 경우
                    if index == shark_index: 
                        #기존의 방향을 변경해줘야한다.
                        current_shark_direction[shark_index-1]=next_direction
                        temp_graph[next_row][next_col]=shark_index
                        break

    #이동이 완료된 그래프 저장
    graph=temp_graph

def smell_decrease(smell_graph):
    global graph
    for row in range(N):
        for col in range(N):
            if smell_graph[row][col] == None:
                continue
            shark_index,count=smell_graph[row][col]

            #냄새가 1인 경우 1 감소하면 0이 되므로 제거한다. 또한 냄새가 사라지면 빈칸이 되므로 이에대한 처리를 수행한다.
            if count ==1:
                smell_graph[row][col] = None   
            else:
                smell_graph[row][col]=[shark_index,count-1]  

def print_board(graph):
    print("GRAPH")
    for row in graph:
        print(row)

def solution():
    #냄새에 대한 그래프 
    smell_graph=[[None] * N for _ in range(N)]

    for i in range(0,1000):
        if not check_if_shark_alive():
            return i

        #상어 이동
        shark_move(smell_graph)
        #냄새에 대해 1씩 감소
        smell_decrease(smell_graph)

        

    return -1

if __name__ == "__main__":

    N,M,K=0,0,0
    graph=[]
    current_shark_direction=[]
    shark_priorities=[]
    
    #0:위/1:아래/2:왼쪽/3:오른쪽
    dy=[-1,1,0,0]
    dx=[0,0,-1,1]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input19237.txt","r") as file:
        N,M,K=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(N)]
        current_shark_direction=list(map(int,file.readline().split()))
        shark_priorities=[[] for _ in range(M)]

        for i in range(M):
            for _ in range(4):
                shark_priorities[i].append(list(map(int,file.readline().split())))
        
    print(solution())

    