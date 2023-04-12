from collections import deque

def check_range(row,col):
    if row < 0 or row >=n or col < 0 or col >=n:
        return False
    return True
#사무실 온도 확인
def check_office_temperature(fresh_map,offices):
    for row,col in offices:
        if fresh_map[row][col] < k:
            return False
    
    return True

#에어컨 작동
def run_airconditioner(fresh_map,wall_map,air_conditioners):
    for start_row,start_col,air_dir in air_conditioners:
        next_row=start_row+dy[air_dir]
        next_col=start_col+dx[air_dir]

        #처음 전파되는 좌표
        fresh_map[next_row][next_col]+=5
        
        queue=deque([(next_row,next_col,4)])
        visited=[[False]*n for _ in range(n)]
        #오른쪽 방향을 기준으로 주석 달았음
        while queue:
            row,col,power=queue.popleft()

            #파워가 0이면 더 이상 전파되지 않는다.
            if power==0:
                continue

            #대각선 왼쪽 처리

            #윗쪽 방향
            up_air_dir=(air_dir-1)%4
            
            #위 좌표
            up_row=row+dy[up_air_dir]
            up_col=col+dx[up_air_dir]
            
            #오른쪽 위의 좌표
            up_right_row=up_row+dy[air_dir]
            up_right_col=up_col+dx[air_dir]

            #왼쪽 대각선 위의 좌표가 격자를 벗어나지 않는지 확인
            if check_range(up_row,up_col) and check_range(up_right_row,up_right_col):
                #가는 방향에 벽이 있는 확인
                if not wall_map[row][col][up_air_dir] and not wall_map[up_row][up_col][air_dir]:
                    #해당 자리를 이전에 처리했는지 확인
                    if not visited[up_right_row][up_right_col]:
                        fresh_map[up_right_row][up_right_col]+=power
                        visited[up_right_row][up_right_col]=True
                        queue.append((up_right_row,up_right_col,power-1))
            
            #정방향
            right_row=row+dy[air_dir]
            right_col=col+dx[air_dir]

            #왼쪽 대각선 위의 좌표가 격자를 벗어나지 않는지 확인
            if check_range(right_row,right_col):
                #가는 방향에 벽이 있는 확인
                if not wall_map[row][col][air_dir]:
                    #해당 자리를 이전에 처리했는지 확인
                    if not visited[right_row][right_col]:
                        fresh_map[right_row][right_col]+=power
                        visited[right_row][right_col]=True
                        queue.append((right_row,right_col,power-1))

            #대각선 오른쪽 처리
            down_air_dir=(air_dir+1)%4
            
            #아래 좌표
            down_row=row+dy[down_air_dir]
            down_col=col+dx[down_air_dir]
            
            #오른쪽 아래의 좌표
            down_right_row=down_row+dy[air_dir]
            down_right_col=down_col+dx[air_dir]

            #오른쪽 대각선 아래의 좌표가 격자를 벗어나지 않는지 확인
            if check_range(down_row,down_col) and check_range(down_right_row,down_right_col):
                #가는 방향에 벽이 있는 확인
                if not wall_map[row][col][down_air_dir] and not wall_map[down_row][down_col][air_dir]:
                    #해당 자리를 이전에 처리했는지 확인
                    if not visited[down_right_row][down_right_col]:
                        fresh_map[down_right_row][down_right_col]+=power
                        visited[down_right_row][down_right_col]=True
                        queue.append((down_right_row,down_right_col,power-1))


#시원함 퍼짐
def spread_fresh_air(fresh_map,wall_map):
    new_fresh_map=[[0] *n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            value=fresh_map[row][col]
            total_spread_value=0
            for dir in range(4):
                next_row=row+dy[dir]
                next_col=col+dx[dir]
                
                #범위를 벗어나는 경우
                if not check_range(next_row,next_col):
                    continue
                
                #해당 진행방향에 벽이 있는 경우 퍼지지 않는다.
                if wall_map[row][col][dir]:
                    continue
                
                #현재 좌표의 시원함이 인접한 좌표의 시원함보다 4 차이 이상 나지 않는 경우 퍼지지 않는다.
                if value +4 <= fresh_map[next_row][next_col]:
                    continue

                spread_value=(value-fresh_map[next_row][next_col])//4
                new_fresh_map[next_row][next_col]+=(spread_value)
            
            #다 퍼지고 남은 만큼은 원래 좌표에 넣는다.
            new_fresh_map[row][col]=value-total_spread_value
    
    #시원함이 퍼진이후의 갱신
    for row in range(n):
        for col in range(n):
            fresh_map[row][col]=new_fresh_map[row][col]


#외벽에 맞다있는 좌표에 대해 시원함 감소
def lose_fresh(fresh_map):
    #가로줄
    for col in range(n):
        if fresh_map[0][col] > 0:
            fresh_map[0][col]-=1
        if fresh_map[n-1][col] > 0:
            fresh_map[n-1][col]-=1
    
    #세로줄
    for row in range(1,n-1):
        if fresh_map[row][0]> 0:
            fresh_map[row][0]-=1
        if fresh_map[row][n-1]>0:
            fresh_map[row][n-1]-=1

def print_board(title,board):
    print(title)

    for row in board:
        print(*row)

def solution():
    fresh_map=[[0] * n for _ in range(n)]
    wall_map=[[[False]*4 for _ in range(n)] for _ in range(n)]

    offices=[]
    air_conditioners=[]
    
    for row in range(n):
        for col in range(n):
            #빈칸인 경우
            if board[row][col]==0:
                continue
            #사무실
            if board[row][col]==1:
                offices.append((row,col))
            #에어컨
            else:
                air_conditioners.append((row,col,board[row][col]-2))

    #벽의 좌표 표시
    for row,col,wall_dir in walls:
        row-=1
        col-=1
        #윗쪽으로 나있으면
        if wall_dir==0:
            wall_map[row][col][1]=True
            #위의 좌표의 아랫쪽에 벽이있음을 표시
            if row -1 >=0:
                wall_map[row][col][3]=True

        #왼쪽으로 나있으면
        else:
            wall_map[row][col][0]=True
            #왼쪽 좌표의 오른쪽에 벽이있음을 표시
            if col-1>=0:
                wall_map[row][col-1][2]=True
    
    air_conditioners.pop()
    time=0
    while True:
        print(f"time: {time}")
        if check_office_temperature(fresh_map,offices):
            break
        run_airconditioner(fresh_map,wall_map,air_conditioners)
        print_board("after_aircondition",fresh_map)
        spread_fresh_air(fresh_map,wall_map)
        print_board("after spreading_air",fresh_map)
        lose_fresh(fresh_map)
        print_board("after losing fresh",fresh_map)
        time+=1        
    
    print(time)
if __name__ == "__main__":
    n,m,k=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(n)]
    walls=[list(map(int,input().split())) for _ in range(m)]
    dy=[0,-1,0,1]
    dx=[-1,0,1,0]

    solution()

