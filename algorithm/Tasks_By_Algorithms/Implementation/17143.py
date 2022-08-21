def print_graph():
    print("GRAPH")
    for row in range(n_rows):
        print(graph[row])

def find_closest_shark(col):
    for row in range(n_rows):
        if graph[row][col]!=-1:
            return row +1
    return False


def shark_move():
    global graph

    dy=[-1,1,0,0]
    dx=[0,0,1,-1]

    change_direction=[1,0,3,2]

    temp_graph=[[-1] * n_cols for _ in range(n_rows)]

    for start_row in range(n_rows):
        for start_col in range(n_cols):
            if graph[start_row][start_col] !=-1:
                #속도,방향,크기
                shark_index=graph[start_row][start_col]
                row,col=start_row,start_col
                #상어의 속력만큼 이동
                times=0
                
                while times < sharks[shark_index][0]:
                    next_row,next_col=row+dy[sharks[shark_index][1]],col+dx[sharks[shark_index][1]]
                    if next_row < 0 or next_row >=n_rows or next_col < 0 or next_col >=n_cols:
                        #방향 전환
                        sharks[shark_index][1]=change_direction[sharks[shark_index][1]]
                        #전단계로 다시 돌아가는 과정
                    else:
                        row,col=next_row,next_col
                        times+=1
                #이동을 마친 이후, 해당 칸에 더 큰 상어가 있는 경우, 해당 상어에게 잡아먹히게 된다.
                if temp_graph[row][col] !=-1:
                    if sharks[temp_graph[row][col]][2] >= sharks[graph[start_row][start_col]][2]:
                        continue
                
                temp_graph[row][col]=graph[start_row][start_col]
            
    graph=temp_graph                   


def solution():
    catched_amount=0
    for col in range(n_cols):
        #잡을 수 있는 상어 찾기
        result=find_closest_shark(col)
        #잡을 수 있는 상어가 있는 경우 잡는다.
        if result:
            catched_amount+=sharks[graph[result-1][col]][2]
            #해당 상어 제거
            graph[result-1][col]=-1
        
        #상어의 이동
        shark_move()

    return catched_amount

if __name__ == "__main__":
    n_rows,n_cols,n_sharks=0,0,0
    graph=[]
    sharks=[]
    

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input17143.txt","r") as file:
        n_rows,n_cols,n_sharks=map(int,file.readline().split())
        graph=[[-1]*n_cols for _ in range(n_rows)]
        for i in range(n_sharks):
            row,col,speed,direction,size=map(int,file.readline().split())
            #해당 속력만큼 모두 이동을 수행하면 시간 초과가 발생하게 된다 
            #이동 과정에 있어 사이클이 있음을 알 수 있다.
            if direction <=2: #상하 이동인경우
                speed %= (2*n_rows-2)
            else:
                speed %= (2*n_cols-2)
            sharks.append([speed,direction-1,size])
            graph[row-1][col-1]=i
            
    print(solution())