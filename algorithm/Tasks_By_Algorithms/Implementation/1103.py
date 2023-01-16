from collections import deque
def dfs(row,col,count):
    global max_count,visited
    max_count=max(max_count,count)
    
    number=int(board[row][col])
    for dir in range(4):
        next_row=row+dy[dir]*number
        next_col=col+dx[dir]*number

        if 0<=next_row <n_rows and 0<=next_col<n_cols and board[next_row][next_col]!="H" and dp[next_row][next_col]<(count+1):
            # 다음 위치에 저장되어 있는 값보다 큰데, 해당 위치를 이전에 방문했다는 것은 사이클이 발생했다는 뜻이다.
            if visited[next_row][next_col]:
                print(-1)
                exit()
            else:
                dp[next_row][next_col]=count+1
                visited[next_row][next_col]=True
                dfs(next_row,next_col,count+1)
                visited[next_row][next_col]=False
    

if __name__ == "__main__":
    n_rows,n_cols=0,0
    board=[]
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input1103.txt","r") as file:
        n_rows,n_cols=map(int,file.readline().split())
        board=[list(file.readline().strip()) for _ in range(n_rows)]

    visited=[[False] * n_cols for _ in range(n_rows)]
    dp=[[0] * n_cols for _ in range(n_rows)]
    max_count=0

    dfs(1,0,0)

    for row in dp:
        print(row)
    print(max_count)