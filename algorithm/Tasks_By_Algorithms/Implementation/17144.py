def find_dust_spaces():
    dust_spaces=[]
    for row in range(n_rows):
        for col in range(n_cols):
            if graph[row][col] <=0:
                continue
            dust_spaces.append((row,col,graph[row][col]))
    
    return dust_spaces

def spread_dust(dust_spaces):
    global graph
    temp_graph=[[0] *n_cols for _ in range(n_rows)]

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    
    for row,col,dust_size in dust_spaces:
        spreaded_dust_size=dust_size//5
        count=0
        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]
            if next_row < 0 or next_row>=n_rows or next_col <0 or next_col>=n_cols:
                continue
            #공기청정기가 있는 칸으로는 미세먼지가 넘어가지 않는다.
            if graph[next_row][next_col] == -1:
                continue
            temp_graph[next_row][next_col] += spreaded_dust_size
            count+=1
        temp_graph[row][col]+=(dust_size-spreaded_dust_size*count)
    
    #공기청정기 위치 표시
    temp_graph[purifier_location[0]][0]=-1
    temp_graph[purifier_location[1]][0]=-1
    graph=temp_graph

def spread_fresh_air():
    
    upper_movement=[(-1,0),(0,1),(1,0),(0,-1)]
    below_movement=[(1,0),(0,1),(-1,0),(0,-1)]

    #공기청정기 위쪽 부분 처리
    row,col=purifier_location[0]-1,0
    for dir in range(4):
        movement=upper_movement[dir]
        while True:
            next_row,next_col=(row+movement[0],col+movement[1])
            if next_row < 0 or next_row>purifier_location[0] or next_col <0 or next_col>=n_cols:
                break
            #공기 청정기까지 다시 돌아오는 경우
            if graph[next_row][next_col]==-1:
                graph[row][col]=0
                break
            graph[row][col]=graph[next_row][next_col]
            row,col=next_row,next_col

    #공기청정기 아래쪽 부분 처리
    row,col=purifier_location[1]+1,0
    for dir in range(4):
        movement=below_movement[dir]
        while True:
            next_row,next_col=(row+movement[0],col+movement[1])
            if next_row < purifier_location[1] or next_row>=n_rows or next_col <0 or next_col>=n_cols:
                break
            #공기 청정기까지 다시 돌아오는 경우
            if graph[next_row][next_col]==-1:
                graph[row][col]=0
                break
            graph[row][col]=graph[next_row][next_col]
            row,col=next_row,next_col


def print_graph():
    print("GRAPH")
    for row in range(n_rows):
        print(graph[row])

def solution():
    for _ in range(T):
        spread_dust(find_dust_spaces())
        print_graph()
        spread_fresh_air()
        print_graph()


    count=0
    for row in range(n_rows):
        for col in range(n_cols):
            if graph[row][col] <=0:
                continue
            count+=graph[row][col]
    return count
if __name__ == "__main__":
    n_rows,n_cols,T=0,0,0
    graph=[]
    purifier_location=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input17144.txt","r") as file:
        n_rows,n_cols,T=map(int,file.readline().split())
        for i in range(n_rows):
            row=list(map(int,file.readline().split()))
            graph.append(row)
            for data in row:
                if data==-1:
                    purifier_location.append(i)
    print(solution())