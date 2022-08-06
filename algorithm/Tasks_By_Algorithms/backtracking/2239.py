def is_true(num,row,col):
    #해당 행 검사
    for i in range(9):
        if board[row][i]==num:
            return False
    #해당 열 검사
    for i in range(9):
        if board[i][col]==num:
            return False
    
    start_row=(row//3)*3
    start_col=(col//3)*3

    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if board[i][j] == num:
                return False
    
    return True   


def dfs(blank_points,index):
    global candidates
    if index == len(blank_points):
        for i in range(9):
            print("".join(map(str,board[i])))
        exit(0)
    
    row,col=blank_points[index]

    for i in range(1,10):
        if is_true(i,row,col):
            board[row][col]=i
            dfs(blank_points,index+1)
            board[row][col]=0


def solution():
    blank_points=[]
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                blank_points.append((row,col))

    dfs(blank_points,0)


if __name__ == "__main__":
    board=[]
    
    candidates=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\backtracking\\input2239.txt","r") as file:
        board=[(list(map(int,file.readline().strip()))) for _ in range(9)]
    solution()
