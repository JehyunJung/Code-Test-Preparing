from collections import deque
def solution():
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    fire_queue=deque()
    jihoon_queue=deque()

    fire_visited=[[-1]*n_cols for _ in range(n_rows)]
    jihoon_visited=[[-1]*n_cols for _ in range(n_rows)]

    for row in range(n_rows):
        for col in range(n_cols):
            if board[row][col]=="F":
                fire_visited[row][col]=0
                fire_queue.append((row,col))
            if board[row][col]=="J":
                jihoon_visited[row][col]=0
                jihoon_queue.append((row,col))
    
    #각 좌표에 대해 불이 퍼지는데 걸리는 시간을 측정한다.
    while fire_queue:
        row,col=fire_queue.popleft()

        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            #범위를 넘어서는 경우
            if next_row < 0 or next_row >=n_rows or next_col < 0 or next_col>=n_cols:
                continue
            #이전에 방문한 위치인 경우
            if fire_visited[next_row][next_col] != -1:
                continue
            #벽인 경우
            if board[next_row][next_col] == "#":
                continue

            fire_visited[next_row][next_col]=fire_visited[row][col]+1
            fire_queue.append((next_row,next_col))

    #지훈이를 움직이면서 미로를 탈출할 수 있는 지 여부를 판단한다.
    while jihoon_queue:
        row,col=jihoon_queue.popleft()

        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            #범위 밖으로 이동하는 경우는 미로를 탈출할 수 있는 경우이다.
            if next_row < 0 or next_row >=n_rows or next_col < 0 or next_col>=n_cols:
                print(jihoon_visited[row][col]+1)
                return
            #이전에 방문한 경우
            if jihoon_visited[next_row][next_col] != -1:
                continue
            #벽인 경우
            if board[next_row][next_col] == "#":
                continue
            #지훈이 보다 불이 먼저 도착하는 경우
            if fire_visited[row][col] != -1 and jihoon_visited[row][col] +1 >= fire_visited[next_row][next_col]:
                continue

            jihoon_visited[next_row][next_col]=jihoon_visited[row][col]+1
            jihoon_queue.append((next_row,next_col))
            
    print("IMPOSSIBLE")
if __name__ == "__main__":
    with open("input4179.txt","r") as file:
        n_rows,n_cols=map(int,file.readline().split())
        board=[list(file.readline().strip()) for _ in range(n_rows)]
    solution()
    