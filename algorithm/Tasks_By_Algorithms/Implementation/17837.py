def solution():
    horse_board=[[[] for _ in range(N)] for _ in range(N)]
    
    dy=[0,0,-1,1]
    dx=[1,-1,0,0]
    change_direction=[1,0,3,2]

    #초기 말의 위치 배치
    for index in range(K):
        row,col,height,dir=horses[index]
        horse_board[row][col].append((index))
        
    for i in range(1,1001):
        check=False

        #턴 진행
        for index in range(K):
            horse=horses[index]
            row,col,horse_height,dir=horse

            next_row=row+dy[dir]
            next_col=col+dx[dir]

            #벗어나는 경우 or 파란색인 경우
            if next_row <0 or next_row >=N or next_col < 0 or next_col>=N or board[next_row][next_col]==2:
                #방향을 바꿔준다.
                dir=change_direction[dir]
                horses[index][3]=dir
                #바뀐 방향으로 한 칸 이동한다.
                next_row=row+dy[dir]
                next_col=col+dx[dir]

                #이동하고 나서도, 벗어난 경우이거나 파란색인 경우 이동을 하지 않는다.
                if next_row <0 or next_row >=N or next_col < 0 or next_col>=N or board[next_row][next_col]==2:
                    continue
                #만약 이동할 수 있는 경우이면 아래의 빨간색, 흰색 경우를 고려한다.
  
            #빨간색인 경우
            if board[next_row][next_col]==1:
                #이전 위치에 있던 말을 옮기게 되는데, 이때 역순으로 해서 옮겨야한다.
                horse_board[next_row][next_col].extend(horse_board[row][col][horse_height:][::-1])
                
            #흰색인 경우
            elif board[next_row][next_col]==0:
                horse_board[next_row][next_col].extend(horse_board[row][col][horse_height:])


            #말의 위치 정보를 새롭게 저장한다.
            height=0
            for index in horse_board[next_row][next_col]:
                horses[index][0]=next_row
                horses[index][1]=next_col
                horses[index][2]=height
                height+=1

            horse_board[row][col]=horse_board[row][col][:horse_height]
            
            #4개 이상 쌓였는 지 파악
            if len(horse_board[next_row][next_col])>=4:
                check=True
                break
            
        #턴 진행중에 쌓인 경우
        if check:
            return i

    return -1

if __name__== "__main__":
    N,K=0,0
    board=[]
    horses=dict()

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input17837.txt","r") as file:
        N,K=map(int,file.readline().split())
        board=[list(map(int,file.readline().split())) for _ in range(N)]
        for i in range(K):
            row,col,dir=map(int,file.readline().split())
            horses[i]=[row-1,col-1,0,dir-1] #row,col,놓인 층 수(높이),방향
    
    print(solution())

